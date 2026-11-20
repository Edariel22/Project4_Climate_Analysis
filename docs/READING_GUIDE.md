# Reading the project

Start with the notebook's Section 1 for the questions and results. Section 3 shows the data patterns before modeling. Sections 4 and 6 explain how the models are evaluated. Sections 7 and 8 contain the comparisons and discussion of errors. Section 9 brings the findings and limitations together.

## Five phases and nine sections

The five phases describe the analysis tasks. The nine sections organize the notebook for submission.

| Phase | Task | Notebook locations |
|---|---|---|
| 1 | Download, inspect, and plot the data | Sections 2–4 |
| 2 | Estimate global warming and compare CO₂ models | Section 6.1 |
| 3 | Forecast ten cities one and twelve months ahead | Sections 6.2–6.3 |
| 4 | Group twenty cities and compare climate classes | Section 5 |
| 5 | Predict rain and heat and examine hot-day frequency | Sections 6.4–6.5 |

## Terms used in the results

- **Training:** data the model learns from.
- **Validation / CV:** earlier time splits used to choose model settings.
- **Test / held-out period:** later data reserved for the final evaluation.
- **MAE:** the average size of a temperature prediction error, in °C. A 0.9°C MAE is an average, not a maximum error.
- **Seasonal naive:** predict the temperature from the same month in the previous year.
- **MAE skill:** how much a model reduces error relative to that seasonal baseline. A positive value means improvement.
- **Precision and recall:** precision asks how many predicted events happened; recall asks how many actual events were found.
- **F1:** combines precision and recall into one score.
- **PCA and K-Means:** PCA summarizes patterns in the city measurements; K-Means groups similar profiles.
- **ARI:** measures agreement between the groups and the published climate classes. The low score here means the agreement is weak.
- **HAC interval:** an uncertainty calculation that allows nearby years' regression errors to be related.

## Points to discuss

Why did we keep dates in order? Why use last year's same-month temperature as a baseline? Why does the twelve-month forecast need older inputs? Why might temperature-only groups differ from Köppen classes? What do the event models miss, and what does the airport station tell us about campus conditions?

The report discusses these questions. The saved outputs provide the numbers behind each answer.
