"""Download and profile Phase 1 data. Run from the repository root."""
from pathlib import Path
import json
import sys
import argparse
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.project_setup import acquire_data, load_core, scan_cities, coverage, city_coverage

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--station", help="Confirmed Meteostat station identifier")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    paths = acquire_data(root, station_id=args.station)
    glob, co2, rain, station = load_core(paths)
    cities, climatology, city_summary, city_missing = scan_cities(paths["cities"])
    import pandas as pd
    rows = {"global": coverage(glob, "dt"), "co2": coverage(co2, "dt"),
            "rain": coverage(rain, "Date", "Location"), "cities_full_file": city_summary}
    if station is not None:
        rows["station"] = coverage(station, "time")
    pd.DataFrame(rows).T.to_csv(root / "docs/data_coverage.csv", index_label="dataset")
    city_coverage(cities).to_csv(root / "docs/city_coverage.csv", index=False)
    city_missing.to_csv(root / "docs/city_missingness.csv")
    for name, frame in [("global", glob), ("co2", co2), ("rain", rain)]:
        frame.isna().mean().rename("missing_fraction").to_csv(root / f"docs/{name}_missingness.csv")
    processed = root / "data/processed"
    processed.mkdir(parents=True, exist_ok=True)
    cities.to_csv(processed / "selected_cities.csv", index=False)
    climatology.to_csv(processed / "city_climatologies.csv")
    print(pd.DataFrame(rows).T.to_string())
    print(city_coverage(cities).to_string(index=False))
    print("Eligible cities for climatology:", len(climatology))
    print("Station status:", "loaded" if station is not None else "pending campus confirmation")

if __name__ == "__main__":
    main()
