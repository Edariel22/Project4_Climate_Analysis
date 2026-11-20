# Team 4: Final project check

**Team members:** Miguel De Jesus Rosa and Elias D Medina Galan
**Date:** October 30, 2026

The saved analysis completed all 27 code cells without errors. It covers the four main source groups and follows the nine required notebook sections. Each of the ten cities was tested with ten regression models plus a seasonal baseline at both one- and twelve-month leads. Eight classifiers were evaluated separately for rain and heat. The comparison table contains 245 rows.

The selected twelve-month city models average 0.922°C MAE and 21.0% mean per-city error reduction relative to the seasonal baseline. Global trend models start in 1850, and temperature anomalies use 1951–1980. The city grouping compares twenty profiles with published Köppen classes. The station heat-frequency analysis includes 25 years meeting the 90% maximum-temperature coverage rule.

The report has twelve pages, and the presentation has twelve slides. Source hashes, package versions, predictions, and validation records are included.

The readability revision rewrites the notebook explanations and project guides, adds a reading guide and metric definitions, and expands compressed code. Python syntax-tree comparisons confirm that the calculations were preserved. Saved outputs and execution counts are unchanged. The formatting edit did not repeat model training.

The analytical run used a fresh in-process IPython session. A Google-hosted Colab run still needs independent verification. GitHub write attempts returned 403, so the prepared revision has not been published. The repository-backed Colab link still opens an older notebook with 155 rows and only Ridge plus the baseline at twelve months. The separate Drive-hosted Colab notebook has now been updated in place and downloaded again to verify an exact byte match with the revised file. The Colab link is unchanged. This upload verification does not claim a new Google-hosted model run.

Before submission, both students should check the final notebook in Colab, confirm their actual individual contributions, review the written work, rehearse, and verify the professor's access.
