# Data acquisition

The integrated notebook downloads data into `data/raw/` relative to its kernel working directory. Internet access is required. Keep raw data out of GitHub.

| Source | Files / selection | Access |
|---|---|---|
| Berkeley Earth / Kaggle | `GlobalTemperatures.csv`, `GlobalLandTemperaturesByCity.csv`; version 2 | https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data |
| NOAA Mauna Loa | `co2_mm_mlo.csv`; negative sentinel values become missing | https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv |
| Rain in Australia / Kaggle | `weatherAUS.csv`; version 2 | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package |
| Meteostat | Station `78526`, daily 2000–2025, `meteostat_78526_2000-2025.csv` | https://meteostat.net/ ; see [station audit](../docs/STATION_SELECTION.md) |

Kaggle downloads use `kagglehub`. If acquisition fails, obtain the source files above and place them in the notebook's `data/raw/` folder. Do not commit API keys or credentials. Meteostat download errors are printed; confirm the local station is available before treating Phase 5 as complete. See each provider for attribution, license and redistribution conditions.

**Forecasting cities:** New York, London, Paris, Cairo, Bombay (historical Mumbai identifier), Tokyo, Sydney, Cape Town, São Paulo and La Plata. La Plata replaces Buenos Aires, which is absent from the selected file.

**Additional PCA/K-Means cities:** Los Angeles, Chicago, Berlin, Moscow, Beijing, Bangkok, Singapore, Melbourne, Lima and Nairobi. Confirm all 20 have complete reference climatologies.

**Köppen reference:** the notebook does not download this file. Supply an independently verified `data/raw/koppen_reference.csv` with `City,Country,Koppen` columns matching all 20 cities exactly. Record a source citation and classification reference period for each entry, either in additional columns or accompanying documentation. Without it, the notebook prints a pending comparison message.

Global anomalies use 30 complete years in 1951–1980. Climate profiles use 1961–1990. City training ends in 2000 (test 2001–2013); rain training ends in 2015 (test from 2016). Local heat holds out the final five years. Source periods differ; do not describe all series as extending to the current year.

Generated audit and comparison CSVs are written under `outputs/phase1/`; PNGs under `figures/`. Existing repository figures are from the earlier EDA checkpoint. Replace or supplement them only with actual outputs from the final executed analysis.
