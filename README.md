# Project 4 — Climate Analysis and Prediction

Private course project for **Edariel22** and **pologram1**. Team number, full names, campus and instructor access are pending. This is the setup / Phase 1 checkpoint, not a finished analysis.

## Start here

- Main notebook: `notebooks/Project4_TeamTBD.ipynb` (nine required sections; self-contained for Colab).
- [Open the working Google Colab notebook](https://colab.research.google.com/drive/1bxJwRP9GDeVZaYjFXlZ26LtowNxhBNil). Uploaded with executed outputs; teammate edit access is pending their Google email.
- [Open the versioned GitHub notebook in Colab](https://colab.research.google.com/github/Edariel22/Project4_Climate_Analysis/blob/main/notebooks/Project4_TeamTBD.ipynb). Private-repository access may require signing into GitHub in Colab.
- [Full assignment checklist](docs/PROJECT_CHECKLIST.md), [decisions and pending inputs](docs/DECISIONS.md), [proposal draft](docs/PROPOSAL_DRAFT.md), [collaboration workflow](docs/COLLABORATION.md).
- [Data download instructions](data/README.md). Do not commit raw data or credentials.

## Local setup (Windows PowerShell)

Use Python 3.12 or 3.13. A virtual environment avoids modifying your other projects.

`requirements.txt` pins portable direct dependencies; `requirements-lock-windows.txt` records every installed package in the tested Windows/Python 3.13 environment. Use the portable file in Colab because the Windows lock includes platform-specific packages.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/prepare_data.py
.\.venv\Scripts\python.exe -m jupyterlab notebooks/Project4_TeamTBD.ipynb
```

On macOS/Linux use `.venv/bin/python`. In a fresh Colab runtime, Run all installs the pinned packages and downloads data directly. Campus/station configuration remains an explicit pending input; the notebook prints that status rather than fabricating local results. The full assignment cannot be considered complete until that dataset and later phases are finished.

## Work sequence

1. **Setup / EDA:** acquire and profile all four sources; global temperature/CO₂/city/rain plots; 1951–1980 anomalies.
2. **Trend models:** global linear/polynomial fits, pre/post-1975 slopes and CI, Ridge/Lasso with and without CO₂.
3. **Forecasting:** ten cities, temporal CV, all ten regressors and a seasonal-naive baseline, 2001–2013 holdout and true 12-month horizons.
4. **Climate zones:** 1961–1990 climatologies, PCA, k-Means, world map and 20-city Köppen comparison.
5. **Events:** all eight classifiers for Australian rain and local heat; annual heat-frequency trend.

## Repository layout

```text
requirements.txt       pinned direct dependencies
notebooks/             single main notebook
src/                   helper functions embedded in notebook
scripts/               download/profile and notebook build utilities
data/README.md         source instructions; raw/processed files ignored
figures/               generated figures for report/slides
docs/                  requirements, decisions, proposal, measured coverage
report/                supplied IEEE draft PDF and LaTeX source
slides/                final presentation destination
```

The existing report has five pages and pending experiments. Preserve it as a starting point; the final report must be 8–12 pages. Rename the notebook/repository to `Project4_Team##` when the team number is known. Both students must contribute real code commits and present.

## Verified first checkpoint

The notebook executed all 13 code cells without errors on Windows/Python 3.13.2, generated seven EDA plots, and retained all nine required sections. `pip check` and three baseline/coverage unit tests passed. See [validation notes](docs/VALIDATION.md).

The source scan covered 8,599,212 city rows and 3,510 city/geography keys. The ten working cities include La Plata as a documented replacement for Buenos Aires, which is absent from this source. Global monthly data end in 2015; city data end in 2013; Australian rain data end in 2017. Three sources are downloaded; Meteostat awaits the campus. Later model phases are explicitly pending.
