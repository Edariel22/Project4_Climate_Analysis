# Week 1 proposal — working draft, not yet submitted

**Project:** Machine Learning in Climate Analysis and Prediction
**Students / team:** awaiting full names and team number
**Accounts:** Edariel22 and pologram1
**Campus / local station:** UAGM Gurabo; Meteostat 78526 (San Juan International Airport), about 21.3 km away. Period 2000-2025; 25 years with >=90% valid daily maximum temperatures. See STATION_SELECTION.md for limitations.

We will estimate global warming per decade and compare trends before and after 1975; evaluate 12-month city-temperature forecasts against a seasonal-naive baseline; discover city climate groups with PCA and k-Means; and predict next-day rain and local heat events while measuring local heat-frequency trends. We will use Berkeley Earth monthly temperatures, NOAA Mauna Loa CO2, Rain in Australia, and one nearby Meteostat station.

The ten working cities are New York, London, Paris, Cairo, Mumbai (historical dataset label Bombay), Tokyo, Sydney, Cape Town, Sao Paulo and La Plata. La Plata replaces the report's suggested Buenos Aires, which is absent from this CSV. Forecasts train through 2000 and test on available observations in 2001-2013; Australian rain models train through 2015 and test from 2016. Preprocessing stays inside cross-validation Pipelines. The shared notebook records download provenance, missingness and chronological partitions.

**Before submission:** insert confirmed names/team and review the selected station, review `docs/data_coverage.csv` and city coverage, and capture notebook outputs showing `df.shape` and `df.head()` for all four sources. Export the finished proposal to one page. This draft is not a completed Week 1 submission.
