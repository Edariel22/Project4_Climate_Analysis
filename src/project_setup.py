"""Reproducible Phase 1 acquisition and diagnostics; embedded in the Colab notebook.

Sources and methodological choices are documented in data/README.md and docs/.
No synthetic observations or model results are substituted for missing downloads.
"""
from pathlib import Path
from datetime import datetime, timezone, date
import hashlib
import json
import shutil
import urllib.request
import numpy as np
import pandas as pd

SEED = 42
GLOBAL_SERIES = "LandAndOceanAverageTemperature"
CITY_PAIRS = [
    ("New York", "United States"), ("London", "United Kingdom"),
    ("Paris", "France"), ("Cairo", "Egypt"), ("Bombay", "India"),
    ("Tokyo", "Japan"), ("Sydney", "Australia"),
    ("Cape Town", "South Africa"), ("S\u00e3o Paulo", "Brazil"),
    ("La Plata", "Argentina"),
]

def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def acquire_data(root, station_id=None, start="2000-01-01", end="2025-12-31"):
    """Cache source data locally. A station must be explicitly selected by ID."""
    import kagglehub
    root = Path(root)
    raw = root / "data/raw"
    raw.mkdir(parents=True, exist_ok=True)
    records = []
    paths = {}
    files = [
        ("global", "berkeleyearth/climate-change-earth-surface-temperature-data/versions/2", "GlobalTemperatures.csv"),
        ("cities", "berkeleyearth/climate-change-earth-surface-temperature-data/versions/2", "GlobalLandTemperaturesByCity.csv"),
        ("rain", "jsphyg/weather-dataset-rattle-package/versions/2", "weatherAUS.csv"),
    ]
    for key, handle, filename in files:
        target = raw / filename
        cache_path = None
        if not target.exists():
            cache_path = Path(kagglehub.dataset_download(handle, path=filename))
            shutil.copy2(cache_path, target)
        paths[key] = target
        records.append(dict(dataset=key, source=f"https://www.kaggle.com/datasets/{handle}", version=2,
                            file=filename, sha256=sha256(target), bytes=target.stat().st_size,
                            resolved_cache_path=str(cache_path) if cache_path else None))
    url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"
    target = raw / "co2_mm_mlo.csv"
    if not target.exists():
        with urllib.request.urlopen(url, timeout=90) as response:
            content = response.read()
        if b"year,month" not in content.replace(b" ", b""):
            raise ValueError("NOAA response is not the expected monthly CSV")
        target.write_bytes(content)
    paths["co2"] = target
    records.append(dict(dataset="co2", source=url, file=target.name,
                        sha256=sha256(target), bytes=target.stat().st_size))
    if station_id:
        import meteostat as ms
        target = raw / f"meteostat_{station_id}_{start}_{end}.csv"
        if not target.exists():
            daily = ms.daily(ms.Station(id=str(station_id)), date.fromisoformat(start),
                             date.fromisoformat(end), providers=[ms.Provider.DAILY]).fetch()
            if daily.empty:
                raise ValueError(f"No daily observations for station {station_id}")
            daily.to_csv(target, index_label="time")
        paths["station"] = target
        records.append(dict(dataset="station", source="https://meteostat.net/", station_id=station_id,
                            provider="daily",
                            requested_start=start, requested_end=end,
                            file=target.name, sha256=sha256(target), bytes=target.stat().st_size))
    manifest_path = raw / "manifest.json"
    # Preserve the original retrieval metadata when reusing an unchanged snapshot.
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    previous_records = {r["file"]: r for r in previous.get("files", [])}
    now = datetime.now(timezone.utc).isoformat()
    for record in records:
        old = previous_records.get(record["file"], {})
        record["retrieved_utc"] = old.get("retrieved_utc", now) if old.get("sha256") == record["sha256"] else now
        if old.get("sha256") == record["sha256"] and not record.get("resolved_cache_path"):
            record["resolved_cache_path"] = old.get("resolved_cache_path")
    manifest_path.write_text(json.dumps({"files": records}, indent=2), encoding="utf-8")
    return paths

def coverage(df, date_column, location_column=None):
    dates = pd.to_datetime(df[date_column])
    return {"rows": len(df), "columns": len(df.columns),
            "first_date": str(dates.min().date()), "last_date": str(dates.max().date()),
            "locations": int(df[location_column].nunique()) if location_column else 1,
            "missing_cells": int(df.isna().sum().sum())}

def load_core(paths):
    glob = pd.read_csv(paths["global"], parse_dates=["dt"])
    co2 = pd.read_csv(paths["co2"], comment="#", skipinitialspace=True)
    co2.columns = co2.columns.str.strip()
    co2["dt"] = pd.to_datetime(dict(year=co2.year, month=co2.month, day=1))
    # NOAA uses negative sentinel values for absent measurements.
    for column in ["average", "deseasonalized", "ndays", "sdev", "unc"]:
        if column in co2:
            co2[column] = co2[column].mask(co2[column] < 0)
    rain = pd.read_csv(paths["rain"], parse_dates=["Date"])
    rain = rain.sort_values(["Date", "Location"]).reset_index(drop=True)
    station = pd.read_csv(paths["station"], parse_dates=["time"]) if "station" in paths else None
    return glob, co2, rain, station

def scan_cities(path, pairs=CITY_PAIRS):
    """Scan all rows in chunks; retain all dates for the 10 specified city/country pairs.

    Aggregate 1961-1990 climatologies for all cities (no random downsampling).
    Geographic key includes coordinates, avoiding accidental merging of namesakes.
    """
    keys = ["City", "Country", "Latitude", "Longitude"]
    chosen, grouped, missing = [], [], None
    locations = set()
    n = 0
    first, last = None, None
    for chunk in pd.read_csv(path, parse_dates=["dt"], chunksize=250_000):
        n += len(chunk)
        missing = chunk.isna().sum() if missing is None else missing.add(chunk.isna().sum(), fill_value=0)
        cmin, cmax = chunk.dt.min(), chunk.dt.max()
        first = cmin if first is None else min(first, cmin)
        last = cmax if last is None else max(last, cmax)
        locations.update(map(tuple, chunk[keys].drop_duplicates().to_numpy()))
        mask = pd.MultiIndex.from_frame(chunk[["City", "Country"]]).isin(pairs)
        chosen.append(chunk.loc[mask])
        base = chunk.loc[chunk.dt.between("1961-01-01", "1990-12-31")].copy()
        base["month"] = base.dt.dt.month
        grouped.append(base.groupby(keys + ["month"])["AverageTemperature"].agg(["sum", "count"]))
    selected = pd.concat(chosen, ignore_index=True)
    matched = set(map(tuple, selected[["City", "Country"]].drop_duplicates().to_numpy()))
    absent = set(pairs) - matched
    if absent:
        raise ValueError(f"Selected city/country pairs missing from this source: {sorted(absent)}")
    stats = pd.concat(grouped).groupby(level=list(range(5))).sum()
    stats["mean"] = stats["sum"].div(stats["count"].replace(0, np.nan))
    climatology = stats["mean"].unstack("month")
    counts = stats["count"].unstack("month")
    # Require at least 24 of 30 years for every calendar month.
    climatology = climatology.loc[(counts >= 24).all(axis=1)].copy()
    climatology["annual_range"] = climatology.max(axis=1) - climatology.min(axis=1)
    climatology["latitude"] = [float(k[2][:-1]) * (-1 if k[2][-1] == "S" else 1) for k in climatology.index]
    summary = dict(rows=n, columns=len(missing), first_date=str(first.date()),
                   last_date=str(last.date()), locations=len(locations), missing_cells=int(missing.sum()))
    return selected, climatology, summary, (missing / n).rename("missing_fraction")

def annual_anomalies(glob, column=GLOBAL_SERIES):
    monthly = glob.set_index("dt")[column].sort_index().loc["1850":]
    annual = monthly.resample("YS").agg(["mean", "count"])
    annual.loc[annual["count"] < 12, "mean"] = np.nan
    baseline = annual.loc["1951":"1980", "mean"]
    if len(baseline.dropna()) != 30:
        raise ValueError("The 1951-1980 baseline needs 30 complete annual means")
    annual["anomaly"] = annual["mean"] - baseline.mean()
    annual["rolling_10y"] = annual["anomaly"].rolling(10, min_periods=10).mean()
    return annual

def city_coverage(cities):
    rows = []
    for key, df in cities.groupby(["City", "Country", "Latitude", "Longitude"]):
        valid = df.dropna(subset=["AverageTemperature"])
        test = valid.loc[valid.dt.between("2001-01-01", "2013-12-31")]
        rows.append(dict(city=key[0], country=key[1], latitude=key[2], longitude=key[3],
                         rows=len(df), valid_months=len(valid),
                         first_valid=str(valid.dt.min().date()), last_valid=str(valid.dt.max().date()),
                         test_valid_months=len(test), test_expected_months=156))
    return pd.DataFrame(rows)
