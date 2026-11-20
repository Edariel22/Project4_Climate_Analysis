"""Validate final notebook evidence and report constraints without rerunning models."""

from pathlib import Path
import json, re, hashlib, subprocess
import pandas as pd
import nbformat

R = Path(__file__).resolve().parents[1]
O = R / "outputs/phase1"
p = R / "notebooks/Project4_Team4.ipynb"
n = nbformat.read(p, as_version=4)
nbformat.validate(n)
code = [c for c in n.cells if c.cell_type == "code"]
assert all(c.execution_count is not None for c in code)
assert not [
    (i, o) for i, c in enumerate(code) for o in c.outputs if o.output_type == "error"
]
headings = [
    c.source.splitlines()[0]
    for c in n.cells
    if c.cell_type == "markdown" and re.match(r"^#{1,2} [1-9]\.", c.source)
]
assert len(headings) == 9, headings
master = pd.read_csv(O / "master_model_comparison.csv")
assert len(master) == 245
for filename in [
    "phase3_regression_comparison.csv",
    "phase3_twelve_month_forecasts.csv",
]:
    d = pd.read_csv(O / filename)
    assert (
        len(d) == 110
        and d.city.nunique() == 10
        and (d.groupby("city").model.nunique() == 11).all()
    )
    assert not d[["MAE", "RMSE", "R2"]].isna().any().any()
for task in ["rain", "heat"]:
    d = pd.read_csv(O / f"phase5_{task}_comparison.csv")
    assert len(d) == 8
    assert (
        d[["precision", "recall", "F1", "ROC_AUC"]]
        .apply(lambda c: c.between(0, 1).all())
        .all()
    )
hp = pd.read_csv(O / "phase3_twelve_month_predictions.csv")
origin = pd.to_datetime(hp.origin_date)
target = pd.to_datetime(hp.target_date)
assert (
    ((target.dt.year * 12 + target.dt.month) - (origin.dt.year * 12 + origin.dt.month))
    .eq(12)
    .all()
)
assert hp.groupby("city").model.nunique().eq(11).all()
assert len(pd.read_csv(O / "phase4_clusters_koppen.csv")) == 20
assert len(list((R / "figures").glob("0[1-7]_*.png"))) >= 7
warnings = pd.read_csv(O / "convergence_search_warnings.csv")
selected = pd.read_csv(O / "convergence_selected_models.csv")
assert warnings.convergence_warnings.sum() == 0, warnings[
    warnings.convergence_warnings > 0
]
assert not selected.iteration_limit_reached.any()
source = json.loads((R / "outputs/source_manifest.json").read_text())
for entry in source:
    path = R / "data/raw" / entry["filename"]
    assert path.exists()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
tex = (R / "report/main.tex").read_text()
abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S).group(1)
words = len(abstract.split())
assert 150 <= words <= 200, words
assert len(re.findall(r"\\bibitem\{", tex)) >= 4
log = (R / "report/main.log").read_text()
assert "undefined references" not in log and "Reference `" not in log
assert "Overfull \\hbox" not in log
info = subprocess.check_output(
    ["pdfinfo", str(R / "report/Project4_Team4_IEEE_Report.pdf")], text=True
)
pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
assert 8 <= pages <= 12, pages
slideinfo = subprocess.check_output(
    ["pdfinfo", str(R / "slides/Project4_Team4_Presentation.pdf")], text=True
)
slidecount = int(re.search(r"^Pages:\s+(\d+)", slideinfo, re.M).group(1))
assert 10 <= slidecount <= 12, slidecount
tracked = subprocess.check_output(["git", "ls-files"], cwd=R, text=True).splitlines()
assert not any(path.startswith("data/raw/") for path in tracked)
report = {
    "status": "passed",
    "notebook_code_cells": len(code),
    "notebook_sections": 9,
    "saved_errors": 0,
    "master_rows": 245,
    "regressor_families_per_lead": 10,
    "forecast_cities": 10,
    "event_classifiers_per_task": 8,
    "koppen_cities": 20,
    "convergence_warnings": int(warnings.convergence_warnings.sum()),
    "selected_mlp_limit_hits": 0,
    "source_hashes_verified": len(source),
    "abstract_whitespace_words": words,
    "report_pages": pages,
    "presentation_slides": slidecount,
    "notebook_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    "execution_scope": "new in-process IPython namespace; user to verify on Google-hosted Colab",
    "team_details": "Elias D Medina Galan is confirmed as a team member; precise individual contribution allocation still requires team confirmation",
}
(R / "outputs/final_validation.json").write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
