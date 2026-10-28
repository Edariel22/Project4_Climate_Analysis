# Decisions and unresolved inputs

## Confirmed
- Private GitHub repository, owner `Edariel22`; teammate `pologram1`.
- Google Colab for the shared Jupyter notebook.
- Preserve the supplied five-page report draft and its LaTeX source.
- Follow the assignment's five phases; present the final notebook in its mandated nine-section order.

## Pending user input
- Team number, both students' full names and institutional details.
- Campus (or campus coordinates), to choose a nearby station with at least 20 years of usable observations.
- Teammate Google email for edit access to the shared Colab file.
- Instructor GitHub username and final submission date.
- Course policy on AI assistance, so the contribution statement accurately discloses assistance.

## Method choices
- Global primary series: `LandAndOceanAverageTemperature`, matching the handout's starter code. Retain land-only as a sensitivity analysis. The report currently says land-only; update its prose before final submission.
- Require 12 observed months for an annual temperature mean. Baseline: mean of 30 complete years, 1951-1980. Report actual coverage, never label historical Kaggle data as extending to the present.
- Ten city candidates follow the supplied report, with one measured-data replacement: Buenos Aires is absent from the city CSV, so use La Plata, Argentina. Mumbai is named Bombay. Nine original candidates were verified; La Plata completes the selection. Most valid test series stop in August 2013 (New York in September); do not fabricate September-December observations.
- Clustering uses all qualifying cities, not just the ten forecasting cities. Require >=24 observations per calendar month in 1961-1990; disclose exclusions.
- Keep the required lag features strictly retrospective. A true 12-month forecast must not read observed future test temperatures. Use direct-horizon targets or recursive predictions; purge overlapping future targets at CV boundaries. This implementation remains a later phase.
- Forecast holdout: target dates 2001-2013, train target dates through 2000. Rain holdout: dates 2016 onward, train through 2015. Split rain CV by unique dates, keeping all locations from the same day together.
- Heat threshold: full-record 90th percentile for the required descriptive task; additionally evaluate a threshold fixed from training data as a sensitivity check. Preserve missing future temperatures as missing labels, not negative labels. Reindex to a daily calendar before shifting.
- Use temporal CV, fixed seed 42, and preprocessing inside each model's Pipeline. Never tune on the held-out test data.
- Use autocorrelation-aware confidence intervals for warming trends; station annual heat counts must report observed-day coverage and rates.

## Report review
The supplied PDF has five pages; the final requirement is 8-12 pages. It still contains author, data, result and contribution placeholders. Related work needs at least four substantive cited papers/reports. It says the workflow is public, which must be revised for the confirmed private repository. Preserve the original draft as provenance; do not invent findings or author contributions.
