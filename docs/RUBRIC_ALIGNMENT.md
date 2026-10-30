# Team 4 — notebook alignment

Source: `Project4_Climate_Analysis.pdf`, D1 and sections 5–11. The final execution evidence and measured counts are in `outputs/run_summary.json` and `docs/VALIDATION.md`.

| Requirement | Implementation / evidence |
|---|---|
| Nine sections in prescribed order | Main notebook: title, setup, EDA, splits, unsupervised, supervised, comparison, interpretation, conclusions |
| Actual results summary | Measured title paragraph, Section 9 and `outputs/report_facts.json` |
| ≥6 labelled interpreted EDA plots | Seven plots with computed, figure-specific explanations; coverage/missingness/class balance |
| Training-fold preprocessing | sklearn Pipelines; calendar-grouped rain/heat CV with date gaps; chronological city CV |
| All required model families | Ten regressors for each city; eight classifiers for each event task; model-specific subsections |
| Warming and CO₂ | Three descriptive slopes with intervals; held-out linear/polynomial/Ridge/Lasso results |
| Twelve-month forecast question | Separate purged Ridge/seasonal-naive experiment for all ten cities; not mislabelled as the full ten-model comparison |
| PCA, K-Means and Köppen | 20 profiles, PCA loadings, elbow/silhouette, Natural Earth world map, independently sourced raster classes and ARI |
| Required metrics and comparison | Single task-labelled master CSV; CV mean/SD, held-out metrics, search/prediction timings and baseline skill; descriptive clustering rows labelled separately |
| Event metrics | Precision, recall, F1, ROC-AUC, ROC curves, both confusion matrices and rain per-location accuracy |
| Full-record heat threshold | tmax full-record 90th percentile; annual count and observed-day rate trends; ≥90% coverage filter |
| Feature importance/error analysis | Held-out permutation importance, monthly residual diagnostics, event error counts and research/discussion answers |
| MLP warnings | Larger iteration budgets; all search warnings and selected-model iteration-limit status exported |
| Reproducibility | Saved outputs, exact analysis dependency pins, seed 42, explicit sampling and source/provenance limitations |

## Remaining submission work

- Confirm Elias's full surname and both students' preferred author names.
- Write the IEEE report: 8–12 pages, 150–200-word abstract, ≥4 related works, methods/results/discussion, references and truthful contribution statement.
- Prepare 10–12 slides as PDF, prediction demo and the shared 12-minute presentation plus Q&A.
- Both students must review code/results, contribute code and appear in history; confirm instructor access and follow course AI policy.
- Independently test fresh Colab acquisition if required; this validation reuses cached source files and executes in an IPython process.

## Interpretation constraints

Low Köppen ARI is a result, not a failed execution. Heat F1/recall limitations and false alerts must remain visible. Warming intervals assume ordinary regression errors; they are not autocorrelation-adjusted. The handout's full-record heat definition is retrospective and is not an operational past-only threshold. San Juan station results are regional evidence, not exact campus conditions. Meteostat's aggregate provider does not guarantee every value is directly observed. Unsupervised diagnostics and predictive scores are not interchangeable.
