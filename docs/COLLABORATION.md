# Working together

## Daily workflow

1. Start with the final `Project4_Team4.ipynb`, locally or in the agreed team Colab file. Use the personal Colab copy for experiments and learning.
2. Agree who is editing the team notebook. The other person can review results, write explanations, or practice the presentation.
3. Before changing calculations, save a Git checkpoint. Re-running writes new outputs and figures; a practice notebook is the easiest place to explore without changing the report evidence.
4. After a useful change, explain what you changed and why, check the affected cells, and save a meaningful commit under your own identity.
5. Review the change together. Transfer the agreed notebook deliberately between Colab and the repository. Do not assume they synchronize.

The import branch is `codex/project4-setup`. It imports Miguel's supplied package and configures the computer; it does not establish who originally authored each analysis. The accompanying pull request records publication and preserves both contributors' earlier commits. See `PUBLISHING_STATUS.md` for verification limits.

## Suggested review order

- First session: read all twelve slides; explain the four research questions in your own words.
- Second session: notebook sections 2-4; identify the sources, missing data, train dates, and test dates.
- Third session: sections 5-6; trace one city's forecast and one event classifier from inputs to predictions.
- Fourth session: sections 7-9; explain MAE, the seasonal baseline, confusion matrices, and the weak findings.
- Before submission: complete a clean run, confirm actual individual contributions, check instructor access, and rehearse the 12-minute presentation.

Current browser access was checked on November 19, 2026: the signed-in account could view Miguel's team Colab notebook but could not save edits there. A personal editable copy was created for practice. Team editing requires Miguel to grant the intended Google account Editor access; no access request or message was sent automatically.

Team 4 consists of Miguel De Jesus Rosa and Elias D Medina Galan.

Use `notebooks/Project4_Team4.ipynb` as the main notebook. Earlier files in `notebooks/archive/` are checkpoints. When editing in Colab, agree on one editor at a time and save meaningful changes back to GitHub from your own account.

A notebook opened from a GitHub link and a copy saved in Google Drive are separate files. Updating one does not automatically update the other. Reopen the repository link to see published GitHub changes, or deliberately update the shared Drive copy.

Keep raw downloads in the ignored `data/raw/` folder. Colab runtimes are temporary, so a new runtime may need to download the data again. Never put a password or access token in a notebook cell.

Before submission, both students should review the code and results and record their actual work in the report's contribution table. Use each student's own commits for work they actually did. The report and slides should use the same saved results as the notebook.
