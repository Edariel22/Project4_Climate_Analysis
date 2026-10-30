# Project 4 — Climate Analysis and Prediction

**Team 4 · Introduction to Machine Learning with Python · UAGM Gurabo**  
Miguel De Jesus Rosa and Elias (surname to confirm).

Analyze warming and CO₂, forecast temperatures for ten cities, discover climate groups, and predict Australian rain and local heat events using observed data.

[**Open main notebook**](notebooks/ProjectX_Team4.ipynb) · [**Run in Google Colab**](https://colab.research.google.com/github/Edariel22/Project4_Climate_Analysis/blob/main/notebooks/ProjectX_Team4.ipynb) · [**Assignment**](Project4_Climate_Analysis.pdf) · [**Rubric alignment**](docs/RUBRIC_ALIGNMENT.md)

## Nine notebook sections

| # | Section | Contents |
|---|---|---|
| 1 | Title, team and summary | Research scope, authors and results-summary status |
| 2 | Imports, configuration and data loading | Downloads, four sources, ten cities and station 78526 |
| 3 | Exploratory data analysis | Seven plots, missingness and 1951–1980 anomalies |
| 4 | Preprocessing and splits | Pipelines, chronological train/test periods and temporal CV |
| 5 | Unsupervised analysis | 1961–1990 normals, PCA, K-Means and cluster diagnostics |
| 6 | Supervised models | Warming models, ten regressors and eight rain/heat classifiers |
| 7 | Comparison tables and plots | Scores, CV, hyperparameters, timings and forecast/ROC plots |
| 8 | Interpretation and error analysis | Computed model summaries and discussion prompts |
| 9 | Conclusions and limitations | Constraints, reproducibility and final conclusions |

## Run

**Colab:** open the link above, select a Python 3 runtime and run all cells. Downloads require internet access. The notebook installs acquisition packages; model libraries are available in Colab. See [data instructions](data/README.md) for source links and the additional Köppen reference requirement.

**Local Jupyter:** use Python 3.12 or 3.13 and the pinned dependencies:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyterlab notebooks/ProjectX_Team4.ipynb
```

Run from top to bottom. Files are written relative to the kernel's working directory: `data/raw/`, `figures/` and `outputs/phase1/` (including later-phase comparison CSVs). Save the executed notebook and copy final figures/tables into the repository before submission. The notebook's `%pip` setup uses unpinned package names; `requirements.txt` is the pinned local environment, not a captured lock of the team's Colab run.

## Repository guide

| Path | Purpose |
|---|---|
| `notebooks/ProjectX_Team4.ipynb` | Current integrated notebook; nine sections in assignment order |
| `notebooks/Project4_TeamTBD.ipynb` | Earlier executed Phase 1 checkpoint, retained for reference |
| `data/README.md` | Download instructions; raw data are excluded |
| `figures/` | Existing EDA figures; update from the final run |
| `docs/RUBRIC_ALIGNMENT.md` | Evidence and remaining requirements, mapped to the handout |
| `report/` | Existing IEEE draft and source; final PDF still required |
| `slides/` | Presentation destination; final PDF still required |
| `src/`, `scripts/`, `tests/` | Earlier setup utilities and checks; not required by the integrated notebook |

**Submission status:** the team reports successful execution. The uploaded integrated notebook has no saved outputs. Structure and code syntax were checked; a new full model run was not performed for this repository update. The final results summary, several analytical requirements, IEEE report and slides remain outstanding; see the [rubric checklist](docs/RUBRIC_ALIGNMENT.md). Earlier planning documents describe historical checkpoints.
