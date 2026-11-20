# Week 1 proposal draft

**Project:** Machine Learning in Climate Analysis and Prediction
**Team 4:** Miguel De Jesus Rosa and Elias D Medina Galan
**Campus:** UAGM Gurabo

We plan to study long-term warming, forecast monthly temperatures in ten cities, group cities with similar climates, and predict next-day rain and heat. The main sources are Berkeley Earth temperatures, NOAA Mauna Loa CO₂, Rain in Australia, and daily Meteostat station weather.

Our forecasting cities are New York, London, Paris, Cairo, Mumbai (Bombay in the dataset), Tokyo, Sydney, Cape Town, São Paulo, and La Plata. La Plata replaces Buenos Aires because the latter is absent from the city file.

For the local task, we selected San Juan International station 78526, about 21.3 km from campus. Its 2000–2025 record has 25 years with at least 90% valid daily maximum temperatures. It provides a regional coastal reference rather than campus measurements; see `STATION_SELECTION.md`.

We will keep the dates in order when training and testing models. City testing covers available 2001–2013 observations, and rain testing begins in 2016. We will compare city forecasts with the temperature from the same month of the previous year and report both useful results and limitations.

This file preserves the proposal stage of the project. The final analysis is in the main notebook. Proposal submission has not been confirmed. Before using this as a Week 1 submission, add the required data-shape and first-row screenshots and check the one-page format.
