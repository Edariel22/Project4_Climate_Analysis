"""Check nearby Meteostat daily records against an explicit calendar.

Raw candidate records stay in ignored data/raw/station_candidates. Published CSVs
contain only station metadata and annual coverage counts, not daily observations.
"""
from datetime import date
from pathlib import Path
import json
import meteostat as ms
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CAMPUS = ms.Point(18.24197, -66.00743)
START, END = date(2000, 1, 1), date(2025, 12, 31)

def main():
    raw = ROOT / 'data/raw/station_candidates'
    raw.mkdir(parents=True, exist_ok=True)
    stations = ms.stations.nearby(CAMPUS, radius=50000, limit=20)
    stations.to_csv(ROOT / 'docs/station_candidates.csv')
    calendar = pd.date_range(START, END, freq='D')
    results = []
    for station_id, station in stations.iterrows():
        path = raw / f'{station_id}.csv'
        if not path.exists():
            ms.daily(ms.Station(id=station_id), START, END,
                     providers=[ms.Provider.DAILY]).fetch().to_csv(path, index_label='time')
        data = pd.read_csv(path, parse_dates=['time']).set_index('time').sort_index()
        if not data.index.is_unique:
            raise ValueError(f'Duplicate dates: {station_id}')
        daily = data.reindex(calendar)
        valid = daily.tmax.notna()
        annual = pd.DataFrame({'valid_tmax': valid.resample('YS').sum(),
                               'expected_days': valid.resample('YS').size()})
        annual['coverage'] = annual.valid_tmax / annual.expected_days
        annual.to_csv(ROOT / f'docs/station_coverage_{station_id}.csv', index_label='year_start')
        daily.isna().mean().rename('missing_fraction_calendar').to_csv(
            ROOT / f'docs/station_missingness_{station_id}.csv')
        results.append(dict(station_id=station_id, name=station['name'],
            distance_km=float(station.distance)/1000, provider='daily',
            start=str(START), end=str(END), returned_rows=len(data),
            expected_days=len(calendar), valid_tmax=int(valid.sum()),
            coverage=float(valid.mean()), years_at_least_90_percent=int((annual.coverage >= .9).sum())))
    (ROOT / 'docs/station_audit.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(pd.DataFrame(results).to_string(index=False))

if __name__ == '__main__':
    main()
