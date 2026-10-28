# What the students should do next

The assignment controls the work sequence. The current goal is to finish the proposal and the Week 2 EDA/preprocessing checkpoint, then begin Phase 2 trend models.

| Action | Why it matters | Concrete result |
|---|---|---|
| Sign into Google, open the shared Colab notebook, and run it in a fresh runtime. | The assignment requires a clean Colab/Kaggle run; local execution alone does not verify the hosted environment. | Record success or the exact failing cell/error. |
| Both students review the data tables and seven figures; revise interpretations in your own words after checking the evidence. | Both must explain the analysis and present. | Explain what each plot shows and one limitation without relying on the caption. |
| Make a small, genuine code contribution each, then review each other's work. Suggested additions: a temperature sanity-check diagnostic and a monthly missingness summary. | Both students must write code and appear in commit history. | Each student's own understandable code commit; do not duplicate existing checks or fabricate contributions. |
| Complete team number, full names, course details and deadline; provide the teammate's Google email and instructor's GitHub username. | These finish naming, the one-page proposal, Colab editing and instructor repository access. | Completed proposal identity fields and correct sharing. |
| Review the station and city decisions in the proposal. | Choices must be justified and documented. | Note station 78526, its approximate 21.3 km distance, the incomplete 2009 record, coastal/inland limitation and La Plata replacing unavailable Buenos Aires. |

Do not upload raw datasets to GitHub. Keep the report's results as pending until models are actually evaluated. Both students should make meaningful commits at least twice a week, as the handout specifies.

Next technical work: complete data-cleaning decisions and implement chronological splits/preprocessing pipelines. Then Phase 2 fits global linear/polynomial trends, confidence intervals, pre/post-1975 slopes, and Ridge/Lasso with and without CO2. Having plots does not mean the entire Week 2 checkpoint is complete.
