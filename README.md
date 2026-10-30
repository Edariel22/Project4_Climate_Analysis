# Project 4 — Climate Analysis and Prediction

**Team 4 · Introduction to Machine Learning with Python · UAGM Gurabo**  
Miguel De Jesus Rosa and Elias D. Medina Galan

Historical warming and CO₂, one- and twelve-month city forecasts, climate clustering, and next-day rain/heat prediction.

[**Executed notebook**](notebooks/ProjectX_Team4.ipynb) · [**Run in Colab**](https://colab.research.google.com/github/Edariel22/Project4_Climate_Analysis/blob/main/notebooks/ProjectX_Team4.ipynb) · [**Results table**](outputs/phase1/master_model_comparison.csv) · [**Assignment**](Project4_Climate_Analysis.pdf)

| Section | Contents |
|---|---|
| 1. Title, team and summary | Actual measured findings and research questions |
| 2. Imports, configuration and data | Source downloads, coverage, missingness and class balance |
| 3. EDA | Seven plots, each interpreted from observed data |
| 4. Preprocessing and splits | Training pipelines, chronological splits and date-grouped CV |
| 5. Unsupervised analysis | PCA, K-Means, world map and sourced 20-city Köppen comparison |
| 6. Supervised models | Model-specific subsections, tuning, ten-city forecasts, eight rain/heat classifiers |
| 7. Comparison | One task-labelled master table, baseline skill, forecast/ROC plots and confusion matrices |
| 8. Interpretation | Permutation importance, residuals, event errors and research-question answers |
| 9. Conclusions | Measured conclusions, limitations, citations and reproducibility |

## Reproduce

Colab: open the link, choose Python 3 CPU, run all. Downloads require internet. Cached files are reused; the final cell offers a results ZIP. The notebook installs compatible version ranges; `requirements.txt` pins the exact analysis packages used in the saved run.

Local Python 3.12:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyterlab notebooks/ProjectX_Team4.ipynb
```

Run cells in order. Data and outputs are relative to the kernel working directory. The recorded validation used a clean in-process IPython namespace and cached source files; a fresh Google-hosted Colab acquisition run has not been independently verified in this update.

## Evidence and deliverables

- `notebooks/ProjectX_Team4.ipynb`: current notebook with saved outputs; the older `Project4_TeamTBD.ipynb` is retained as historical Phase 1 work.
- `outputs/phase1/`: all phase tables, CV/timing evidence, baseline skill, residuals, coverage and convergence audits. Despite the directory name, it includes Phases 1–5.
- `outputs/report_facts.json`: measured values for writing the report; `outputs/tested_versions.json`: executed package versions.
- `figures/`: generated EDA, forecasts, clustering world map, ROC, feature-importance and error-analysis PNGs.
- [Data instructions](data/README.md), [rubric alignment](docs/RUBRIC_ALIGNMENT.md), [validation](docs/VALIDATION.md).
- `report/` and `slides/`: existing drafts/destinations; the final IEEE report and presentation are separate remaining deliverables.

The heat label uses the handout's full-record 90th percentile. The station is San Juan International, a regional coastal reference rather than a campus sensor. Rain uses at most 24,000 time-spaced training rows and the full holdout. Twelve-month Ridge is a separate experiment from the ten-model one-month comparison. Descriptive climate diagnostics and predictive held-out scores are labelled separately; CV selects reporting models. See the notebook for source/provenance limitations and convergence evidence.

Notebook corrections and this repository update were prepared with Codex assistance. Both students must verify names, contributions and course-policy compliance before final submission.
