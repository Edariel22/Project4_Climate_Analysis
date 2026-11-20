# What was checked

The final notebook is `notebooks/Project4_Team4.ipynb`. Its saved analytical run completed all 27 code cells in a fresh in-process IPython session with no saved errors. A normal TCP Jupyter kernel could not start on that host, so this is not a claim that the notebook was run on Google's Colab runtime.

## Model and data checks

- Ten cities were tested with ten regressors and a seasonal baseline at both one- and twelve-month leads: 220 forecast rows in total.
- Seven global prediction rows, sixteen event-classifier rows, and two climate-summary rows bring the master table to 245 rows.
- Twelve-month temperature inputs stop at the forecast origin. Date checks prevent training labels from extending beyond the first validation origin. Forecast issue and target dates are saved.
- One- and twelve-month errors use the same target months for each city.
- Rain and heat models use date-ordered validation. All locations from the same date stay on one side of each rain split. Rain subsampling affects training only.
- The heat label uses the full-record percentile required by the assignment. It happens to equal the training-only percentile in this saved dataset.
- The global trends include ordinary and five-lag Newey–West HAC intervals. The comparison at 1975 allows separate intercepts and slopes.
- Package versions, source hashes, settings, predictions, plots, and convergence checks are saved with the results.

## Readability edit

The explanations were rewritten in plain English. Compressed Python statements were expanded and comments were added. Each reformatted cell and helper script was checked against its earlier Python syntax tree. The calculations, settings, execution counts, and saved outputs were preserved. This edit did not repeat the model training.

`outputs/final_validation.json` records the earlier analysis and document checks. `outputs/readability_validation.json` records the later text and formatting checks. Keeping these separate makes it clear what was run and what was edited afterward.

## Team review still needed

Run the final notebook in Colab, check the individual contribution statement, review the report and slides, rehearse the talk, and confirm that the professor can open the repository. Submission and presentation are still team actions.
