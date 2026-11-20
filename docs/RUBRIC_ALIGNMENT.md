# Where the requirements are covered

This table connects the professor's requirements to the notebook and supporting files. The assignment is `Project4_Climate_Analysis.pdf`. Run counts are saved in `outputs/run_summary.json`; the scope of the checks is explained in `docs/VALIDATION.md`.

| Requirement | Where to find it |
|---|---|
| Nine sections in prescribed order | Main notebook: title, setup, EDA, splits, unsupervised, supervised, comparison, interpretation, conclusions |
| Actual results summary | Measured title paragraph, Section 9 and `outputs/report_facts.json` |
| ≥6 labelled interpreted EDA plots | Seven plots with computed, figure-specific explanations; coverage/missingness/class balance |
| Training-fold preprocessing | sklearn Pipelines; calendar-grouped rain/heat CV with date gaps; chronological city CV |
| All required model families | Ten regressors for each city; eight classifiers for each event task; model-specific subsections |
| Warming and CO₂ | Three descriptive slopes with intervals; held-out linear/polynomial/Ridge/Lasso results |
| Twelve-month forecast question | All ten regression families plus seasonal naive for all ten cities, with purged CV, explicit origin dates and matching test months |
| PCA, K-Means and Köppen | 20 profiles, PCA loadings, elbow/silhouette, Natural Earth world map, independently sourced raster classes and ARI |
| Required metrics and comparison | Single task-labelled master CSV; CV mean/SD, held-out metrics, search/prediction timings and baseline skill; descriptive clustering rows labelled separately |
| Event metrics | Precision, recall, F1, ROC-AUC, ROC curves, both confusion matrices and rain per-location accuracy |
| Full-record heat threshold | tmax full-record 90th percentile; annual count and observed-day rate trends; ≥90% coverage filter |
| Feature importance/error analysis | Held-out permutation importance, monthly residual diagnostics, event error counts and research/discussion answers |
| MLP warnings | Larger iteration budgets; all search warnings and selected-model iteration-limit status exported |
| Reproducibility | Saved outputs, exact analysis dependency pins, seed 42, explicit sampling and source/provenance limitations |

## Deliverables

- Final notebook: `notebooks/Project4_Team4.ipynb`, all nine sections and saved measured outputs.
- IEEE report: `report/Project4_Team4_IEEE_Report.pdf`, with LaTeX source, related work, numbered figures/tables and the four discussion answers.
- Presentation: 12-slide PDF and editable PPTX in `slides/`, with suggested 12-minute speaker timing and a recorded prediction example.
- Final measured validation: `outputs/final_validation.json`. Independent Google-hosted Colab execution remains the user's requested review.
- Confirm the truthful contribution allocation; rehearse and verify instructor access.

## How to read the results

The weak Köppen agreement and the event models' errors are findings to discuss. Warming intervals include ordinary and five-lag HAC results. The heat label uses the full record because the assignment requires it; a live system would need a past-only threshold. San Juan station results describe the regional record rather than exact campus conditions. Meteostat combines sources, and a nonmissing value need not be a direct observation. Climate-grouping measures and prediction scores answer different questions.
