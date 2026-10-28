# Project 4 requirements tracker

Source: Project4_Climate_Analysis.pdf, sections 3-13. This tracker records requirements, not completed results.

## Phase 1 — Weeks 1-2
- [x] Acquire all four datasets, including station 78526 for UAGM Gurabo (2000-2025).
- [ ] Report years, locations, shape/head, missingness and uncertainty columns for every source.
- [x] Validate ten cities across continents and >=20 years of local daily station coverage (25 years >=90% tmax coverage; source limitations documented).
- [x] Plot global annual temperature since 1850 with a 10-year rolling mean.
- [x] Plot CO2, monthly cycles for three contrasting cities, rain frequency by Australian location.
- [x] Calculate 1951-1980 temperature anomalies; include >=6 labelled, interpreted EDA figures (seven saved in first checkpoint).
- [ ] Submit a one-page proposal with names, research questions, cities/station and shape/head screenshots.

## Phase 2 — Week 3
- [ ] Linear and degree-2/3 polynomial global temperature models from 1850.
- [ ] Warming rate per decade with 95% CI; separate 1850-1974 / 1975-latest slopes.
- [ ] Annual CO2 from 1958; Ridge and Lasso comparisons with and without CO2.

## Phase 3 — Weeks 3-4
- [ ] Ten city forecasts; lags 1/2/3/12, shifted 12-month rolling mean, month sin/cos and year.
- [ ] Train through 2000, holdout 2001-2013; TimeSeriesSplit within training only.
- [ ] Tune linear, Ridge, Lasso, polynomial, kNN, tree, random forest, gradient boosting, SVR and MLP regressors.
- [ ] True 12-month forecast evaluation; seasonal-naive baseline on identical targets.
- [ ] RMSE, MAE, R2 and skill against seasonal naive; forecast-versus-actual plots for 3 cities.

## Phase 4 — Week 4
- [ ] 1961-1990 monthly climatologies, annual range and latitude; PCA and loadings interpretation.
- [ ] k-Means with elbow and silhouette selection, world map with latitude/longitude.
- [ ] Compare against sourced Koppen classes for 20 well-known cities.

## Phase 5 — Weeks 4-5
- [ ] Rain numeric/categorical preprocessing in Pipelines; date split through 2015 vs 2016 onward.
- [ ] Tune logistic, kNN, naive Bayes, SVM, tree, random forest, gradient boosting and MLP classifiers for BOTH rain and heat.
- [ ] Handle imbalance using training folds only; full-record 90th percentile heat definition; next-calendar-day target.
- [ ] Precision, recall, F1, ROC-AUC, confusion matrices and ROC curves; rain per-location accuracy.
- [ ] Annual heat-day counts, observed-day rates and linear frequency trend.

## Deliverables and milestones
- [ ] D1: one Project4_Team##.ipynb, all nine sections in required order, clean full run.
- [ ] One master comparison table: model, best hyperparameters, CV mean/SD, held-out metrics, training and prediction time.
- [ ] D2: IEEE report, 8-12 pages, 150-200-word abstract, >=4 substantive related works, all four discussion questions, references and contribution table.
- [ ] D3: 10-12 slides exported to PDF, 12-minute talk + 3-minute Q&A, both speakers, prediction demo.
- [ ] D4: repository with prescribed directories, pinned requirements, instructions, no raw datasets; instructor access.
- [ ] Week 1 proposal; Week 2 EDA/splits; Week 3 >=4 CV models; Week 4 all tuned models; Week 5 report sections 1-5 draft; Week 6 final submission.
- [ ] Both students write code, appear in commit history, commit >=twice weekly, and can explain all results.
- [ ] Cite data, papers, tutorials and reused code; follow course AI policy.
