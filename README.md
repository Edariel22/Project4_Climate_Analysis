# Project 4: Climate Analysis and Prediction

## Your starting point

Use this folder as the local working project. Miguel's supplied final package was imported on November 19, 2026, on branch `codex/project4-setup`; the earlier checkpoint is preserved in Git and the original ZIP remains in Downloads.

1. **Work locally:** double-click `Start_Project.cmd`. It opens the final notebook with the dedicated Anaconda environment `climate-team4`. If asked for a kernel, select **Python (Climate Team 4)**.
2. **Check the installation:** double-click `Check_Setup.cmd`. This tests imports and a real Jupyter kernel without repeating the climate experiments.
3. **Understand the project:** read the twelve-slide presentation, then [the reading guide](docs/READING_GUIDE.md), then notebook sections 1, 3, 7 and 8.
4. **Know exactly what to do next:** use [your ordered checklist and message to Miguel](docs/TEAM_NEXT_STEPS.md).

| Tool | Purpose |
|---|---|
| Anaconda / `climate-team4` | Keeps this project's Python packages separate from other courses |
| JupyterLab | Opens and runs the notebook on this computer |
| Google Colab | Opens a separate notebook copy and runs it on Google's computers |
| Git / GitHub | Records reviewed changes and shares the agreed team version |

Local files, Colab copies and GitHub do **not** synchronize automatically. See [the team workflow](docs/COLLABORATION.md). The submitted notebook should remain `Project4_Team4.ipynb`; personal practice copies should be clearly labelled.

To recreate the environment on another computer, open Anaconda Prompt in this folder and run `conda env create -f environment.yml`, then `conda run -n climate-team4 python -m ipykernel install --user --name climate-team4 --display-name "Python (Climate Team 4)"`.

The recorded project results are imported evidence. A successful setup check is not a new full model run. Re-running the main notebook writes new tables and figures; use a personal Colab copy for practice or save a Git checkpoint first.

**Team 4 · Introduction to Machine Learning with Python · UAGM Gurabo**

Miguel De Jesus Rosa and Elias D Medina Galan

We use climate and weather records to study warming, forecast temperatures for ten cities, group cities by their climate, and predict rain and heat events. The notebook follows the professor's nine-section order and includes the saved tables and figures.

## Where to start

- [Main notebook](notebooks/Project4_Team4.ipynb): the analysis, code, explanations, and saved results.
- [IEEE report](report/Project4_Team4_IEEE_Report.pdf): the written discussion of the methods and findings.
- [Presentation](slides/Project4_Team4_Presentation.pdf): twelve slides, including a prediction example. An [editable PowerPoint](slides/Project4_Team4_Presentation.pptx) is also included.
- [Reading guide](docs/READING_GUIDE.md): a short route through the project and the main terms.
- [Assignment](Project4_Climate_Analysis.pdf): the original requirements.

## Run the notebook

1. Open the [updated shared notebook in Colab](https://colab.research.google.com/drive/1RuUMDKWYnloyxGTN7VvgyQ9vIT4PtUXs).
2. Choose a Python 3 CPU runtime and select **Runtime → Run all**. The first cells install the packages and download the data. The large city file and model searches take time.
3. Read the results in order. The last cell offers a ZIP of the generated tables and figures.

For local Jupyter, install the packages in `requirements.txt` and open `notebooks/Project4_Team4.ipynb`. Run the cells from top to bottom. Downloads are stored in `data/raw/` and reused when available.

This revision imports Miguel's supplied final package and reconciles it with the existing GitHub history. See [publication and verification status](docs/PUBLISHING_STATUS.md) for the exact scope. A Drive copy and a GitHub notebook do not automatically synchronize.

## What we found

The global temperature record has a steeper warming slope after 1975. For city forecasts, the selected models average 0.855°C error at one month and 0.922°C at twelve months. At twelve months, the average error reduction across cities is 21.0% compared with using last year's temperature for the same month.

The city groups agree only weakly with detailed Köppen classes (ARI 0.0596). Rain prediction has an F1 score of 0.640; heat prediction has an F1 score of 0.493. Missed events and false alarms remain an important limit. These are tests on historical data, not evidence that the models are ready for live warnings.

## Notebook sections

| Section | What it covers |
|---|---|
| 1 | Team, research questions, and results overview |
| 2 | Packages, downloads, and data checks |
| 3 | Seven plots and what they show |
| 4 | How training, validation, and testing are separated |
| 5 | PCA, K-Means, and the twenty-city climate comparison |
| 6 | Global trends, ten city regressors at both lead times, and eight rain/heat classifiers |
| 7 | Scores, model settings, running times, and comparison plots |
| 8 | Forecast errors, useful inputs, missed events, and research answers |
| 9 | Conclusions, limitations, sources, and the results package |

## Data, results, and checks

The four main source groups are Berkeley Earth temperatures, NOAA CO₂, Rain in Australia, and Meteostat station weather. Global trend models start in 1850. The Puerto Rico station is San Juan International, a regional reference about 21.3 km from campus. [Data notes](data/README.md) explain the sources and coverage.

`outputs/phase1/` contains results from all five phases despite its older folder name. The [master comparison](outputs/phase1/master_model_comparison.csv) has 245 rows. Source hashes and package versions are saved in `outputs/`. Figures are in `figures/`.

The saved calculations ran through all 27 code cells in a fresh in-process IPython session. They have not been independently verified on a Google-hosted Colab runtime. The readability edit changes explanations, comments, and formatting; the Python calculations and saved outputs are preserved. See [validation notes](docs/VALIDATION.md) and [requirement mapping](docs/RUBRIC_ALIGNMENT.md).

Codex assisted with revisions, analysis checks, and preparation of the report and slides. Both students still need to confirm their individual contributions, review the work, rehearse, and submit it under the professor's course policy.
