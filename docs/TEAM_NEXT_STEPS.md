# Your next steps, in order

## Already done on this computer

- [x] Imported Miguel's final package, including the notebook, saved results, report, and slides.
- [x] Preserved the earlier local checkpoint and created branch `codex/project4-setup`.
- [x] Created the Anaconda environment `climate-team4`, installed dependencies, and tested a real Jupyter kernel.
- [x] Added `Start_Project.cmd` and `Check_Setup.cmd` in the project folder.
- [x] Created an editable personal Colab copy named `Project4_Team4_Personal_Practice.ipynb`.

These checks establish setup readiness. They do not establish a fresh full run of the climate experiments or completion of course submission requirements.

## Do next

1. [ ] **Send Miguel the message below.** Confirm the final deadline, authoritative notebook, editing access, and division of remaining work. The current Google account can view the team notebook but cannot save edits there.
2. [ ] **Read the twelve-slide presentation first** (`slides/Project4_Team4_Presentation.pdf`), then `docs/READING_GUIDE.md`. Write one sentence answering each of the four research questions in notebook Section 1.
3. [ ] **Open the notebook.** For local work, double-click `Start_Project.cmd` and use kernel **Python (Climate Team 4)**. For practice in the cloud, open `Open_Personal_Colab.url`. Choose one place for each work session; local files and Colab do not synchronize automatically.
4. [ ] **Trace one example before editing.** Follow one city's data, date split, seasonal baseline, trained model, MAE, and prediction plot. Then follow one rain or heat classifier through its confusion matrix and F1 score.
5. [ ] **Agree on your actual contribution.** Page 5 of the assignment requires both students to write code, appear in the commit history, and present; page 6 asks for commits at least twice weekly. First identify code you already contributed. If you have not contributed code, agree with Miguel on a genuine, useful coding task you can implement, test, commit, and explain. Clean-run verification, checking report/slide numbers, and presentation preparation are useful additional work, but do not automatically replace the coding requirement. Do not invent or backdate contributions.
6. [ ] **Perform one clean full run in the practice copy.** In Colab select a Python 3 CPU runtime, restart the session, then run all cells from the top. Allow time for downloads and model searches. Record the date, runtime, first failing cell if any, and whether every code cell finishes. Download the generated results ZIP if the final cell offers it. Do not overwrite the team's saved evidence until you compare the results together.
7. [ ] **Reconcile results with Miguel.** Compare the 245-row master comparison table, principal metrics, plots, and report/slide claims. Investigate differences before merging. Record what was actually run and any remaining limits.
8. [ ] **Record your real work.** Review the contribution table together. Commit work you actually performed under your own identity; preserve the history and do not invent past activity. The import pull request identifies the supplied package and setup assistance separately from individual analytical contributions.
9. [ ] **Confirm the final repository together.** Review the import pull request and agree that its package is the version to submit. The repository is public, so reading it does not require an invitation; the course submission and any required instructor acknowledgment still need confirmation. Exclude raw datasets and credentials from future commits.
10. [ ] **Rehearse the 12-minute presentation with both speakers.** Agree slide ownership and transitions. Be ready to explain chronological splits, the seasonal baseline, MAE/F1, the weak cluster agreement, and why these models are not validated for live warnings.
11. [ ] **Verify the course submission page.** Confirm the actual due date, file/link requirements, milestone submissions, and AI/citation policy. Submit the agreed deliverables and keep the receipt. Existing files alone do not prove anything was submitted.

## Message to send Miguel

> Hey Miguel, thanks for sending the package. I now have Anaconda/Jupyter set up and an editable personal Colab copy for practice. I can open the team Colab, but my current Google account only has viewing access. Can you give Editor access to the Google account I confirm with you, and confirm which notebook and GitHub branch we should treat as the final version?
>
> I see the package already includes all five analysis phases, saved results, the IEEE report, and the 12-slide presentation. My setup test passed, but I have not independently rerun all the models yet. I can take responsibility for the clean-run check, comparing the results against the report/slides, documenting any issues, and preparing my presentation sections. Does that division work for you, and what remains on your side?
>
> Please also confirm the submission deadline, what has already been submitted, and whether GitHub has the latest files. Let's review the contribution table so it reflects what each of us actually did, agree on the final version, and schedule one rehearsal before submitting.

This is a draft for you to send; no message or access request has been sent automatically.

## Final submission review

Local setup is recorded in `LOCAL_SETUP_STATUS.json`. Use `Start_Project.cmd` for local JupyterLab or the local `Open_Personal_Colab.url` shortcut for practice. Start by understanding the existing results before changing the experiments. A setup smoke test is separate from the required clean full run.

The analysis, IEEE report, and presentation have been prepared. The saved run and its limits are described in `VALIDATION.md`.

1. Publish the prepared final notebook and files to GitHub. Check `PUBLISHING_STATUS.md` for the current sync status.
2. Open the final notebook in Colab and run it from top to bottom.
3. Review the report's contribution table together and describe each person's actual work.
4. Review the twelve slides and prediction example. Rehearse the 12-minute talk and prepare for questions.
5. Confirm the professor can open the repository, then submit the requested files and link.

Keep the weaker findings in the discussion: low agreement with Köppen classes, negative global test R², and errors in heat and rain prediction. They help explain what the models can and cannot tell us.
