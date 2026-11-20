# Data sources

The notebook downloads the source files to `data/raw/`. Large raw files are kept out of GitHub. Tables describing coverage and missing values are saved with the results in `outputs/phase1/`.

| Source | Selection | Access |
|---|---|---|
| Berkeley Earth / Kaggle v2 | `GlobalTemperatures.csv`, `GlobalLandTemperaturesByCity.csv` | https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data |
| NOAA GML | `co2_mm_mlo.csv` | https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv |
| Rain in Australia / Kaggle v2 | `weatherAUS.csv` | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package |
| Meteostat | Daily station 78526, 2000–2025 | https://meteostat.net/en/station/78526 |
| Köppen-Geiger | Beck et al. 2023; historical 1961–1990, 0.1° raster; Figshare 21789074 v2 | https://doi.org/10.1038/s41597-023-02549-6 |
| GeoNames | City-centre coordinates, city names/country codes | https://download.geonames.org/export/dump/cities15000.zip |
| Natural Earth | 1:110m country world basemap | https://www.naturalearthdata.com/ |

The notebook downloads the supporting map data and looks up published Köppen classes at documented city coordinates. The small twenty-city reference table is included; the large source archives remain local. The Beck climate raster and GeoNames data use CC BY 4.0, and Natural Earth is public domain. The original providers describe the terms for their data.

Forecasting cities: New York, London, Paris, Cairo, Bombay (Mumbai), Tokyo, Sydney, Cape Town, São Paulo and La Plata (documented replacement for absent Buenos Aires). Additional clustering cities: Los Angeles, Chicago, Berlin, Moscow, Peking (Beijing), Bangkok, Singapore, Melbourne, Lima and Nairobi.

Temperature anomalies use the 1951–1980 average. City climate profiles use 1961–1990. One-month city training ends in December 2000; twelve-month training labels end in January 2000 to respect the first forecast origin. Both are tested on the available 2001–2013 months. Rain testing starts in 2016, and heat testing uses 2021–2025. The source records do not all end in the same year.

Station 78526 is San Juan International (TJSJ), at 18.4333 N, 66.0000 W in Meteostat metadata. It is about 21.3 km from campus. Meteostat combines provider products; a nonmissing value does not guarantee a direct observation. Missing temperatures stay missing. Annual heat trends use years with at least 90% valid maximum temperatures and show both hot-day counts and their share of valid days. The heat threshold follows the assignment: the 90th percentile of maximum temperature over the full record.

Never commit credentials, raw CSVs or unrelated Colab `sample_data/` examples.
