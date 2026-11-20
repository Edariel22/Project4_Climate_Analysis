from pathlib import Path
import json, pandas as pd

R = Path(__file__).resolve().parents[1]
O = R / "outputs/phase1"
f = json.loads((R / "outputs/report_facts.json").read_text())
h = pd.read_csv(O / "phase3_twelve_month_forecasts.csv")
lead = pd.read_csv(O / "phase3_lead_summary.csv").sort_values("MAE_12m")
pred = pd.read_csv(O / "phase3_twelve_month_predictions.csv")
sel = pred[pred.selected_by_cv]
annual = pd.read_csv(O / "global_annual_anomalies_1951_1980.csv")
heat = pd.read_csv(O / "phase5_annual_heat_days.csv")
summary = (
    h.groupby("model")[["cv_mean", "MAE", "RMSE", "R2", "MAE_skill"]]
    .mean()
    .sort_values("MAE")
    .reset_index()
)
demo = (
    sel[(sel.city == "New York") & sel.target_date.str.startswith("2012")]
    .head(4)
    .copy()
)
demo["absolute_error"] = (demo.actual - demo.prediction).abs()
demo.to_csv(O / "recorded_prediction_demo.csv", index=False)
data = {
    "facts": f,
    "lead": lead.to_dict("records"),
    "horizon": summary.to_dict("records"),
    "annual": annual.to_dict("records"),
    "annual_heat": heat.to_dict("records"),
    "rain": pd.read_csv(O / "phase5_rain_comparison.csv").to_dict("records"),
    "heat": pd.read_csv(O / "phase5_heat_comparison.csv").to_dict("records"),
    "hac": pd.read_csv(O / "phase2_warming_slopes_HAC.csv").to_dict("records"),
    "demo": demo.to_dict("records"),
    "forecasts": {
        city: sel[sel.city == city].head(30).to_dict("records")
        for city in ["New York", "Cairo", "Cape Town"]
    },
}
(R / "slides/presentation_data.json").write_text(
    json.dumps(data, indent=2, allow_nan=True)
)
print("Presentation source tables written")
