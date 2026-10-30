# Data and provenance

Run the main notebook to acquire sources into `data/raw/` relative to its working directory. Raw datasets are excluded from GitHub; `outputs/phase1/` contains aggregate results and audits.

| Source | Selection | Access |
|---|---|---|
| Berkeley Earth / Kaggle v2 | `GlobalTemperatures.csv`, `GlobalLandTemperaturesByCity.csv` | https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data |
| NOAA GML | `co2_mm_mlo.csv` | https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv |
| Rain in Australia / Kaggle v2 | `weatherAUS.csv` | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package |
| Meteostat | Daily station 78526, 2000–2025 | https://meteostat.net/en/station/78526 |
| Köppen-Geiger | Beck et al. 2023; historical 1961–1990, 0.1° raster; Figshare 21789074 v2 | https://doi.org/10.1038/s41597-023-02549-6 |
| GeoNames | City-centre coordinates, city names/country codes | https://download.geonames.org/export/dump/cities15000.zip |
| Natural Earth | 1:110m country world basemap | https://www.naturalearthdata.com/ |

Downloads, GeoNames aliases and sampling of the Köppen raster are implemented in the notebook. The final results package includes the derived 20-city reference; the large reference raster and source city archive remain local. Attribution: Beck raster CC BY 4.0; GeoNames CC BY 4.0; Natural Earth public domain. Consult original providers for source-data terms.

Forecasting cities: New York, London, Paris, Cairo, Bombay (Mumbai), Tokyo, Sydney, Cape Town, São Paulo and La Plata (documented replacement for absent Buenos Aires). Additional clustering cities: Los Angeles, Chicago, Berlin, Moscow, Peking (Beijing), Bangkok, Singapore, Melbourne, Lima and Nairobi.

Anomalies use 1951–1980; profiles use 1961–1990. City training ends in 2000 and testing covers available 2001–2013 data. Rain training ends in 2015 and testing begins in 2016. Heat holds out the final five calendar years. Source records end at different dates.

Station 78526 is San Juan International (TJSJ), 18.4333 N, 66.0000 W in Meteostat metadata. It is not an on-campus instrument. See the existing station audit for campus-distance assumptions. `Provider.DAILY` is an aggregated product and does not establish observation-only provenance. Missing temperatures stay missing; annual heat trends retain years with ≥90% observed maximum-temperature coverage and report observed-day rates alongside counts. The retrospective target threshold is the full-record tmax 90th percentile required by the handout.

Never commit credentials, raw CSVs or unrelated Colab `sample_data/` examples.
