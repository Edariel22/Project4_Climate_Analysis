# Project choices

## Team and scope

Team 4: Miguel De Jesus Rosa and Elias D Medina Galan. The campus reference is UAGM Gurabo. The project follows the assignment's five analysis phases and nine notebook sections.

The individual contribution split, instructor access, submission date, and course requirements for disclosing assistance still need team confirmation. Any shared Google Drive notebook needs to be synchronized deliberately with GitHub.

## Data choices

- Global trends use Berkeley Earth's `LandAndOceanAverageTemperature` from 1850 onward. Annual means require all twelve months. Anomalies use the 30 complete annual means from 1951–1980.
- City forecasts use ten cities across continents. Mumbai is labeled Bombay in the source. La Plata replaces Buenos Aires, which is absent from this file. Most city records stop in August 2013; New York stops in September.
- Climate grouping uses twenty city profiles from 1961–1990. A profile needs at least 24 valid observations for each calendar month. Published Köppen classes are sampled separately at documented city coordinates.
- San Juan International station 78526 was selected because it is the closer of the two catalog results and has sufficient daily temperature coverage. It is about 21.3 km from campus and is a regional reference.

## Modeling choices

Earlier dates train the models and later dates test them. Cross-validation stays within training, and preprocessing is fitted inside each fold. The seed is 42.

All ten regressors are tested at one and twelve months. The twelve-month experiment uses older temperature inputs and a validation gap. Both lead times are compared on the same target months.

Rain training ends in 2015 and testing begins in 2016. Tuning uses at most 24,000 evenly spaced training rows. All locations on a calendar date stay together during validation. The full test set is retained.

Heat testing uses 2021–2025. The event threshold is the full-record 90th percentile required by the assignment. Missing temperatures remain missing labels. Annual trends retain years with at least 90% valid maximum temperatures and show counts as well as observed-day rates.

Warming trends include ordinary and autocorrelation-aware intervals. The CO₂ models use observed test-year concentrations, so they are conditional estimates. No causal claim follows from their association alone.

## Written work

The final report and slides use the saved measured results. The original report draft and earlier notebooks are retained as reference material. Codex assistance is disclosed, and the contribution table still needs the team's account of individual tasks.
