# Station selection for UAGM Gurabo

Audit date: 2026-10-28. Selected working station: **San Juan / Int., Puerto Rico**, Meteostat **78526**, ICAO **TJSJ** (San Juan International Airport).

## Location and search

Campus reference: 18.24197 N, 66.00743 W, the campus amphitheater location published by the event organizer at https://simposiopttoday2023.eventsmart.com/venues/. The university identifies the Gurabo campus at https://uagm.edu/es/recinto-de-gurabo. Distances are approximate straight-line distances from this campus reference, not driving distances.

Meteostat's nearby-station query (50 km radius, limit 20) returned two stations. This is a search of the Meteostat catalog, not proof that no closer weather instruments exist.

| Station | Distance | Requested period | Valid daily maximum temperatures | Years with >=90% temperature coverage |
|---|---:|---|---:|---:|
| 78526 — San Juan International | 21.3 km | 2000-2025 | 9,278 of 9,497 calendar days (97.7%) | 25 |
| TJIG0 — San Juan / Puerta de Tierra | 25.7 km | 2000-2025 | 1,804 of 9,497 calendar days | 5 |

Select 78526 because it is the closer catalog result and provides more than the assignment's required 20 years. Its coordinates are 18.4333, -66.0000; elevation 3 m; timezone America/Puerto_Rico. Metadata: https://meteostat.net/en/station/78526.

## Coverage and limitations

- The downloaded station series has 9,445 returned rows; reindexing to all 9,497 calendar dates exposes 52 entirely absent dates and 167 additional missing maximum temperatures. Never count only returned rows when assessing completeness.
- 2009 has only 242/365 valid maximum temperatures (66.3%). For later annual trend analysis, report counts and observed-day rates; flag/exclude years below the predeclared 90% coverage criterion and show sensitivity. This quality threshold is our methodological choice, not a number imposed by the assignment.
- The coastal airport is a regional reference near Gurabo, not an on-campus measurement. Do not claim that station heat-day trends describe exact campus conditions.
- Precipitation and several other fields are incomplete; peak wind gust is entirely absent. Choose predictors after inspecting missingness; do not treat missing rain or missing temperatures as zero.
- Retrieval uses Meteostat 2.1.5 `Provider.DAILY`, an aggregated product. No application-level interpolation or gap filling was applied. Meteostat warns that products may combine observations and model-derived values; observational provenance is not guaranteed by a nonmissing value. Provider documentation: https://dev.meteostat.net/providers and https://dev.meteostat.net/quality.
- A separate `Provider.GHCND` retrieval for this station yielded only 2,002 dates in 2000-2005 and is insufficient alone for the 20-year task. Do not silently substitute that short record for the selected daily product. A provenance/observation-only sensitivity check remains a limitation to address before final scientific conclusions.

## Reproduction

Run `python scripts/audit_station.py` to reproduce the candidate comparison and calendar-based completeness tables. Run `python scripts/prepare_data.py` to acquire the selected station along with the other sources. Raw daily files remain in ignored `data/raw/`; the repository contains only code, metadata and aggregate diagnostics.

The original assignment places station choice in the proposal (page 2) and requires >=20 years of daily data for Phase 5 (page 3). Heat is defined by maximum temperature above the 90th percentile of the full selected record; modeling remains pending.
