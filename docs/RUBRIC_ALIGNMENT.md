# Assignment alignment — Team 4

Source: [original handout](../Project4_Climate_Analysis.pdf), sections 5–11. Reviewed against `notebooks/ProjectX_Team4.ipynb` on 2026-10-30. “Implemented” describes code present, not verified numerical results. The team reports a successful run, but this uploaded copy has 20 unexecuted code cells and no saved outputs.

## D1: nine required sections

| Section | Evidence present | Work before final submission |
|---|---|---|
| 1. Title, team and results summary | Team 4, project overview | Confirm Elias's surname; replace overview with a paragraph of actual findings |
| 2. Imports/configuration/data | Four sources, automatic acquisition, ten cities, station 78526 | Record exact runtime versions and retain coverage audits; verify station download |
| 3. EDA | Seven labelled figures, anomalies, missingness and uncertainty | Add a 1–2 sentence interpretation beside each plot, including observed values and class balance |
| 4. Preprocessing and splits | Training-only scaling/imputation in pipelines; temporal CV | Audit date boundaries: rain rows share dates across locations, so no date should span training and validation |
| 5. PCA and K-Means | Normals, loadings, elbow, silhouette, latitude/longitude plot | Supply independently sourced Köppen labels for 20 matched cities; interpret PCs; add world-map geography |
| 6. Supervised models | Phase 2 trends; ten city regressors; eight classifiers for both tasks | Add one subsection per required model with tuning rationale; implement genuine 12-month forecasts; finalize held-out trend evaluation |
| 7. Comparison and figures | Per-task tables, CV mean/SD, parameters, timings, city plots, ROC plots | Export one master table, baseline skill, all required confusion matrices and per-location scores |
| 8. Interpretation | Computed winning-model summaries and prompts | Add feature importance, residual/error analysis, four research-question answers and report discussion answers |
| 9. Conclusions and limitations | Limitations and reproducibility notes | Write evidence-based conclusions from saved outputs |

## Phase-specific checks

- [x] Phase 1 code: source acquisition, chunked city loading, coverage and missingness, seven EDA plots, 1951–1980 baseline.
- [x] Phase 2 code: linear/polynomial trend fits, pre/post-1975 slopes with 95% intervals, Ridge/Lasso with and without CO₂.
- [ ] Phase 2 evaluation: in-sample polynomial RMSE is descriptive; add held-out RMSE/MAE/R², CV and timings to the master table. Review serial correlation when interpreting slope intervals.
- [x] Phase 3 code: lags 1/2/3/12, shifted rolling mean, month sin/cos, year; train through 2000 and test 2001–2013; ten regressors and seasonal-naive baseline.
- [ ] Phase 3: the existing experiment uses observed recent lags and is a rolling one-month forecast. Add a separate 12-month-ahead evaluation using only information available at its forecast origin, and quantify skill against the baseline on identical target dates.
- [x] Phase 4 code: 1961–1990 profiles, PCA/loadings, K-Means diagnostics and geographical scatter.
- [ ] Phase 4: require 20 complete matched cities (current code only enforces at least 10); add sourced Köppen reference and agreement score. Current plotting is a coordinate scatter without a world-map baselayer.
- [x] Phase 5 code: rain date split through 2015 vs 2016 onward, categorical/numeric pipelines and all eight classifier families; local daily heat classifiers, full-record 90th percentile as specified and annual heat-day slope.
- [ ] Phase 5: verify temporal CV never separates observations from the same date across folds; add confusion matrices for both tasks and save per-location accuracy. Current matrix/per-location output is only for the rain model selected by test F1; choose the final model by CV and evaluate it once on test data.
- [ ] Phase 5: justify or extend class-imbalance handling for models without class weights; any resampling belongs inside training folds. Current Australian training is uniformly subsampled to at most 24,000 chronological rows for every classifier; document this approximation.
- [ ] Phase 5: report observed-day coverage alongside heat-day counts; count trends can be affected by missing days. Keep the required full-record heat threshold clearly labelled and distinguish it from an operational training-only threshold.
- [ ] All experiments: save outputs, warnings, final parameter selections and a single comparison table; keep test data untouched for tuning/model choice.

## D2–D4 deliverables

| Deliverable | Assignment requirement | Current repository status |
|---|---|---|
| D1 notebook | Single `ProjectX_Team##.ipynb`, nine ordered sections, clean full run | `ProjectX_Team4.ipynb` organized; save the final executed outputs and close checks above |
| D2 report | IEEE PDF, 8–12 pages; 150–200-word abstract; ≥4 related works; methods/results/discussion/references/contributions | Existing draft retained; final report not supplied in this update |
| D3 presentation | 10–12 slides as PDF, 12-minute talk + 3-minute Q&A; both presenters and prediction demo | Final slides/demo not supplied |
| D4 repository | README, pinned requirements, notebooks/src/data instructions/figures/report/slides; no raw datasets; instructor access | Required directories and instructions present; final outputs and instructor access still require confirmation |

## Grading weights

| Criterion | Weight |
|---|---:|
| Data understanding and EDA | 15% |
| Preprocessing and validation | 15% |
| Implementation and tuning of all models | 25% |
| Evaluation, comparison and interpretation | 20% |
| Written report | 15% |
| Presentation and individual questions | 10% |

## Report discussion and team requirements

Answer the handout's four questions using measured evidence: CO₂ association versus causation; degradation at longer forecast horizons; instrument/station/missing-data bias; and regional public-health or energy applications. Both students must contribute code, appear in commit history, present, and understand all results. Include a truthful contribution table, cite datasets and reused material, and follow the professor's AI policy. This organization update was prepared with Codex assistance.
