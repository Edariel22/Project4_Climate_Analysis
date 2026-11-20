"""Build the IEEE manuscript from the executed notebook evidence; run from repo root."""

from pathlib import Path
import json, re, shutil, hashlib, platform
import numpy as np, pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

R = Path(__file__).resolve().parents[1]
O = R / "outputs/phase1"
D = R / "report"
F = D / "figures"
F.mkdir(exist_ok=True)
for p in (R / "figures").glob("*.png"):
    shutil.copy2(p, F / p.name)
facts = json.loads((R / "outputs/report_facts.json").read_text())
old = {
    "mean_cv_selected_city_MAE": 0.855,
    "twelve_month_mean_city_MAE_skill": 0.213,
    "rain_F1": 0.640,
    "rain_AUC": 0.869,
    "heat_F1": 0.493,
    "heat_AUC": 0.878,
    "koppen_ARI": 0.0596,
    "warming_pre1975": 0.0360,
    "warming_post1975": 0.1642,
}
s = (D / "manuscript_template.tex").read_text()


def tex(x):
    return (
        str(x)
        .replace("\\", "\\textbackslash{}")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("&", "\\&")
    )


def num(x, n=3):
    return "--" if pd.isna(x) else f"{x:.{n}f}"


def params(x):
    return tex(str(x).replace("model__", "").replace("poly__", ""))


def table(label, caption, spec, headers, rows, wide=False, size="scriptsize"):
    env = "table*" if wide else "table"
    return (
        "\\begin{"
        + env
        + "}[!tbp]\n\\caption{"
        + caption
        + "}\\label{"
        + label
        + "}\\centering\\"
        + size
        + "\n"
        + "\\begin{tabular}{"
        + spec
        + "}\n\\toprule "
        + " & ".join(headers)
        + r" \\\midrule"
        + "\n"
        + "\n".join(" & ".join(map(str, row)) + r" \\" for row in rows)
        + "\n\\bottomrule\n\\end{tabular}\\end{"
        + env
        + "}"
    )


def replace_table(label, replacement):
    global s
    matches = list(re.finditer(r"\\begin\{(table\*?)\}.*?\\end\{\1\}", s, re.S))
    selected = [m for m in matches if "\\label{" + label + "}" in m.group()]
    assert len(selected) == 1, (label, len(selected))
    m = selected[0]
    s = s[: m.start()] + replacement + s[m.end() :]


# Tables always use this run's values, including timings and selected hyperparameters.
globalmodels = pd.read_csv(O / "phase2_trend_models.csv")
replace_table(
    "tab:globalmodels",
    table(
        "tab:globalmodels",
        "Global held-out results, 2001--2015. CV is training MAE mean $\\pm$ SD. CO$_2$ models condition on observed test-year concentrations.",
        "llrrrrrr",
        [
            "Specification",
            "Best parameters",
            "CV MAE",
            "CV SD",
            "MAE",
            "RMSE",
            "$R^2$",
            "Train s",
        ],
        [
            [
                tex(r.model) + (" + CO$_2$" if r.with_co2 else ""),
                params(r.params),
                num(r.cv_mean),
                num(r.cv_sd),
                num(r.MAE),
                num(r.RMSE),
                num(r.R2),
                num(r.train_seconds, 2),
            ]
            for r in globalmodels.itertuples()
        ],
        True,
    ),
)
slopes = pd.read_csv(O / "phase2_warming_slopes.csv")
hac = pd.read_csv(O / "phase2_warming_slopes_HAC.csv")
sloperows = []
for i, label in [(2, "1850--2015"), (0, "1850--1974"), (1, "1975--2015")]:
    r = slopes.iloc[i]
    rr = hac.iloc[{2: 2, 0: 0, 1: 1}[i]]
    sloperows.append(
        [
            label,
            num(r.value, 4),
            f"[{r.ci_low:.4f}, {r.ci_high:.4f}]",
            f"[{rr.ci_low:.4f}, {rr.ci_high:.4f}]",
        ]
    )
replace_table(
    "tab:slopes",
    table(
        "tab:slopes",
        "Descriptive warming in $^\\circ$C/decade. Ordinary and HAC (five annual lags) 95\\% intervals.",
        "lrrr",
        ["Period", "Rate", "Ordinary CI", "HAC CI"],
        sloperows,
        size="scriptsize",
    ),
)
reg = pd.read_csv(O / "phase3_regression_comparison.csv")
hor = pd.read_csv(O / "phase3_twelve_month_forecasts.csv")


def regtable(df, label, caption):
    g = (
        df.groupby("model")[
            [
                "cv_mean",
                "cv_sd",
                "MAE",
                "RMSE",
                "R2",
                "train_seconds",
                "predict_seconds",
            ]
        ]
        .mean()
        .sort_values("MAE")
    )
    rows = [
        [tex(name)]
        + [
            num(
                r[c],
                4 if c == "predict_seconds" else (2 if c == "train_seconds" else 3),
            )
            for c in g.columns
        ]
        for name, r in g.iterrows()
    ]
    return table(
        label,
        caption,
        "lrrrrrrr",
        ["Family", "CV MAE", "CV SD", "MAE", "RMSE", "$R^2$", "Train s", "Pred. s"],
        rows,
        True,
    )


replace_table(
    "tab:regression",
    regtable(
        reg,
        "tab:regression",
        "One-month held-out comparison. Entries are unweighted means across ten cities. Each city has its own tuned model; exact parameters are in the master CSV.",
    ),
)
chosen = (
    reg[reg.model != "Seasonal naive"]
    .sort_values("cv_mean")
    .groupby("city", sort=True)
    .first()
    .reset_index()
)
rows = [
    [
        tex(r.city),
        tex(r.model),
        params(r.params),
        f"{r.cv_mean:.3f} $\\pm$ {r.cv_sd:.3f}",
        num(r.MAE),
        num(r.RMSE),
        num(r.R2),
    ]
    for r in chosen.itertuples()
]
replace_table(
    "tab:cities",
    table(
        "tab:cities",
        "One-month reporting models selected by training CV MAE, with held-out results.",
        "lllrrrr",
        ["City", "Model", "Parameters", "CV MAE", "MAE", "RMSE", "$R^2$"],
        rows,
        True,
    ),
)
for kind in ["rain", "heat"]:
    df = pd.read_csv(O / f"phase5_{kind}_comparison.csv")
    rows = [
        [
            tex(r.model),
            params(r.params),
            f"{r.cv_mean:.3f} $\\pm$ {r.cv_sd:.3f}",
            num(r.precision),
            num(r.recall),
            num(r.F1),
            num(r.ROC_AUC),
            num(r.train_seconds, 2),
            num(r.predict_seconds, 4),
        ]
        for r in df.itertuples()
    ]
    replace_table(
        "tab:" + kind,
        table(
            "tab:" + kind,
            f"Next-day {kind}: every classifier. CV F1 mean $\\pm$ SD and held-out test metrics.",
            "lllrrrrrr",
            [
                "Model",
                "Parameters",
                "CV F1",
                "Precision",
                "Recall",
                "F1",
                "AUC",
                "Train s",
                "Pred. s",
            ],
            rows,
            True,
        ),
    )
# Composite EDA and diagnostic figures from the regenerated image files.
for names, name, shape in [
    (
        [
            "01_global_temperature.png",
            "02_global_anomalies.png",
            "03_co2.png",
            "04_monthly_cycles.png",
        ],
        "eda_climate.pdf",
        (2, 2),
    ),
    (["05_rain_frequency.png", "06_missingness.png"], "eda_rain.pdf", (1, 2)),
]:
    if name == "eda_climate.pdf":
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader

        temp = F / "eda_climate_build.pdf"
        c = canvas.Canvas(str(temp), pagesize=(864, 504))
        for i, ((x, y), file) in enumerate(
            zip([(0, 252), (432, 252), (0, 0), (432, 0)], names)
        ):
            c.drawImage(
                ImageReader(str(F / file)),
                x + 8,
                y + 14,
                width=416,
                height=232,
                preserveAspectRatio=True,
                anchor="c",
                mask="auto",
            )
            c.drawString(x + 8, y + 240, f"({chr(97+i)})")
        c.showPage()
        c.save()
        temp.replace(F / name)
        continue
    fig, axs = plt.subplots(*shape, figsize=(12, 7 if shape == (2, 2) else 4))
    for i, (ax, file) in enumerate(zip(np.ravel(axs), names)):
        ax.imshow(plt.imread(F / file))
        ax.axis("off")
        ax.set_title(f"({chr(97+i)})", loc="left", fontsize=10)
    fig.tight_layout()
    fig.savefig(F / name, bbox_inches="tight")
    plt.close(fig)
for file, name in [
    ("phase3_residual_analysis.png", "residual_compact.pdf"),
    ("phase5_feature_importance.png", "importance_compact.pdf"),
]:
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.imshow(plt.imread(F / file))
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(F / name, bbox_inches="tight")
    plt.close(fig)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.5))
for ax, kind in zip(axs, ["rain", "heat"]):
    cm = pd.read_csv(O / f"phase5_{kind}_confusion_matrix.csv", index_col=0).to_numpy()
    ax.imshow(cm, cmap="Blues")
    ax.set(
        xticks=[0, 1],
        yticks=[0, 1],
        xticklabels=["No", "Yes"],
        yticklabels=["No", "Yes"],
        xlabel="Predicted",
        ylabel="Actual",
        title=kind.title(),
    )
    for (y, x), value in np.ndenumerate(cm):
        ax.text(
            x,
            y,
            f"{value:,}",
            ha="center",
            va="center",
            color="white" if value > cm.max() / 2 else "black",
        )
fig.tight_layout()
fig.savefig(F / "confusions.pdf", bbox_inches="tight")
plt.close(fig)
lead = pd.read_csv(O / "phase3_lead_summary.csv", index_col=0)
sel = pd.read_csv(O / "phase3_twelve_month_cv_selected.csv")
fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))
lead[["MAE_1m", "MAE_12m"]].plot.bar(ax=axs[0])
axs[0].set(
    ylabel="Mean city MAE (°C)", xlabel="", title="All ten families at both leads"
)
sel.set_index("city").MAE_skill.mul(100).plot.bar(ax=axs[1], color="#277a68")
axs[1].set(
    ylabel="MAE skill over seasonal naive (%)",
    xlabel="",
    title="Twelve-month models selected by CV",
)
fig.tight_layout()
fig.savefig(F / "horizon.pdf", bbox_inches="tight")
plt.close(fig)
# Replace stale horizon discussion as a unit.
a = s.index("Twelve-month Ridge improves over seasonal naive")
b = s.index("\\subsection{", a)
worst = lead.drop(index="Seasonal naive").MAE_change.idxmax()
best = hor[hor.model != "Seasonal naive"].groupby("model").MAE.mean().idxmin()
new = (
    f"""All ten regression families were evaluated at twelve months (Table~\\ref{{tab:horizon}}). Models chosen separately for each city by training CV average {sel.MAE.mean():.3f}~$^\\circ$C held-out MAE, {sel.RMSE.mean():.3f}~$^\\circ$C mean city RMSE, and {sel.R2.mean():.3f} mean city $R^2$. Their mean within-city MAE skill is {sel.MAE_skill.mean()*100:.1f}\\% over seasonal naive. The best family by retrospective mean test MAE is {tex(best)}; that test ranking is descriptive and does not replace validation selection.

"""
    + regtable(
        hor,
        "tab:horizon",
        "Twelve-month held-out results on the same city target months as the one-month experiment. All families use origin-available features. Mean CV SD is fold variation, not an inferential interval.",
    )
    + f"""
\\figwide{{horizon.pdf}}{{Errors for all ten regressors at one- and twelve-month leads, and twelve-month baseline skill for models selected by training CV.}}{{fig:horizon}}
Figure~\\ref{{fig:horizon}} compares identical target dates. {tex(worst)} has the largest absolute increase in mean MAE, {lead.loc[worst,'MAE_change']:.3f}~$^\\circ$C. This compares the two measured leads, not every possible horizon. Different features, conservative training endpoints and retuned hyperparameters contribute to the changes, so the experiment does not isolate a single physical mechanism.

"""
)
s = s[:a] + new + s[b:]
# Specific method/prose corrections.
s = s.replace(
    "Ten regression families are assessed for the one-month task; a separate twelve-month experiment evaluates Ridge and seasonal naive.",
    "Ten regression families are assessed at both one- and twelve-month leads against seasonal naive.",
)
s = s.replace(
    "We instead test a twelve-month Ridge hindcast",
    "We instead test twelve-month city hindcasts",
)
s = s.replace("Twelve-month Ridge uses", "Every twelve-month regressor uses")
s = s.replace(
    "the separate twelve-month Ridge experiment",
    "the ten-family twelve-month experiment",
)
s = (
    s.replace(
        "110 one-month rows, 20 twelve-month rows",
        "110 one-month rows, 110 twelve-month rows",
    )
    .replace("155 total", "245 total")
    .replace("155-row", "245-row")
)
s = s.replace(
    "Stored confidence intervals use the slope standard error and Student-$t$ critical value. They assume ordinary regression errors and do not adjust serial correlation.",
    "Ordinary intervals use the slope standard error and Student-$t$ critical value. An additional Newey--West HAC calculation allows annual residual dependence through five lags. A segmented model with separate intercepts and slopes at 1975 tests the slope difference. These are descriptive observational estimates, not causal attribution.",
)
s = s.replace(
    "with ordinary-regression 95\\% intervals of [0.0296, 0.0424] and [0.1405, 0.1878], respectively.",
    "with autocorrelation-aware uncertainty reported alongside ordinary intervals.",
)
s = s.replace(
    "A separate twelve-month Ridge experiment improves mean per-city error skill by 21.3\\% over seasonal naive.",
    f"All ten families are also tested twelve months ahead, where validation-selected models achieve {sel.MAE.mean():.3f}~$^\\circ$C mean city MAE and {sel.MAE_skill.mean()*100:.1f}\\% mean baseline skill.",
)
s = s.replace(
    "Twelve-month Ridge averages 0.919~$^\\circ$C MAE and 21.3\\% mean city skill over seasonal naive. Flexible families are not universally superior, and the full ten-family comparison at twelve months remains future work.",
    f"Twelve-month validation-selected models average {sel.MAE.mean():.3f}~$^\\circ$C MAE and {sel.MAE_skill.mean()*100:.1f}\\% mean city skill. All ten families were tested at both leads, and {tex(worst)} has the largest absolute MAE increase.",
)
s = s.replace(
    "Ridge's average error increases here, although individual cities vary. Only Ridge was tested at both leads, so the fastest-degrading family is not established. A fair comparison needs common origins and multi-horizon experiments for all families.",
    f"{tex(worst)} has the largest measured increase in mean MAE between one and twelve months. Both evaluations use identical target dates, but their information sets and final training endpoints differ. Further horizons and alternative datasets are needed to establish a general degradation pattern.",
)
s = s.replace(
    "twelve-month Ridge supplies 21.3\\% mean city skill over seasonal naive.",
    f"twelve-month validation-selected models supply {sel.MAE_skill.mean()*100:.1f}\\% mean city skill over seasonal naive.",
)
break_result = json.loads((R / "outputs/slope_break_HAC.json").read_text())
s = s.replace(
    "Ordinary intervals are available, but a formal slope-break test and autocorrelation-adjusted inference were not completed.",
    f'The separate-intercept HAC comparison estimates a post-minus-pre slope difference of {break_result["slope_difference_C_per_decade"]:.4f}~$^\\circ$C/decade, with 95\\% interval [{break_result["ci_low"]:.4f}, {break_result["ci_high"]:.4f}] and $p={break_result["p_value"]:.3g}$.',
)
s = s.replace(
    "Warming intervals assume ordinary errors; no robust breakpoint test was performed.",
    "HAC results depend on the five-lag specification; more complete climate attribution and uncertainty propagation remain outside this benchmark.",
)
s = s.replace(
    "The evidence comes from the saved integrated notebook \\texttt{ProjectX\\_Team4.ipynb} and its October 30, 2026 outputs. This does not claim the older linked live notebook was fully rerun after its separate acquisition correction. The saved run executed 27 code cells in an in-process IPython executor using cached sources; fresh Google-hosted end-to-end acquisition was not verified for that run.",
    "The evidence comes from \\texttt{Project4\\_Team4.ipynb} and its October 30, 2026 outputs. All 27 code cells executed sequentially in a new in-process IPython namespace, including source acquisition in this workspace. The host prevented a TCP Jupyter kernel from starting, so this validation does not claim execution on Google-hosted Colab. The repository-backed Colab link opens the same final notebook for independent verification.",
)
versions = json.loads((R / "outputs/tested_versions.json").read_text())
env = json.loads((R / "outputs/runtime_environment.json").read_text())
a = s.index("The environment used Python")
b = s.index("\\begin{thebibliography}", a)
s = (
    s[:a]
    + "The environment used Python "
    + tex(env["python"].split()[0])
    + ", "
    + ", ".join(tex(k) + " " + tex(v) for k, v in versions.items())
    + ". Search used two workers. Timings include search/refit and are specific to this host; they are not expected production latency. Exact parameters, per-city results, CV variation and times are preserved in the master CSV. Raw source bytes are hashed and excluded from GitHub.\n\nThe repository is \\url{https://github.com/Edariel22/Project4_Climate_Analysis}. Its final notebook opens directly in Google Colab. Codex assisted with notebook revision, analysis verification, report drafting and formatting. Both students remain responsible for reviewing the code and results.\n\n"
    + s[b:]
)
# Update any repeated three-decimal main metrics from the current run.
for key, oldval in old.items():
    if key in facts:
        digits = (
            4 if key in ["koppen_ARI", "warming_pre1975", "warming_post1975"] else 3
        )
        s = s.replace(f"{oldval:.{digits}f}", f"{facts[key]:.{digits}f}")
# Remove old claim that selected convergence warnings were zero if the rerun differs.
hits = facts["selected_mlp_limit_hits"]
s = s.replace(
    "zero selected MLP iteration-limit hits",
    f"{hits} selected MLP iteration-limit hits",
)
# Table timings change without changing science, so wording need not overstate speed rankings.
s = s.replace(
    "The author list follows the supplied template. Elias D Medina Galan's full name has been confirmed by the team; contact information has not been supplied. Specific tasks must be confirmed against actual work and commit history; file ownership does not establish authorship of individual analyses.",
    "The author list uses the names supplied by the team. Repository history records code and notebook commits under Miguel A. De Jesus and Edariel22. The team must confirm the identity mapping and individual task allocation before submitting a signed contribution claim. Codex assistance is disclosed above.",
)
s = s.replace(
    "Coding, analysis, writing, and commit evidence require author confirmation.",
    "Notebook and analysis commits are recorded under Miguel A. De Jesus; final individual task allocation requires team confirmation.",
).replace(
    "Coding, analysis, writing, and commit evidence require author confirmation.",
    "Individual tasks require team confirmation; contributions are not inferred from repository ownership.",
)
s = s.replace(
    "This is a period comparison, not a formal breakpoint test. Ordinary intervals quantify uncertainty under their regression assumptions; serial dependence could alter coverage.",
    "This is a comparison at the assignment-specified 1975 split, rather than a search over possible break dates. Ordinary intervals are supplemented with HAC intervals and a segmented slope comparison in the discussion.",
)
s = s.replace("[hidelinks]{hyperref}", "[hidelinks,hypertexnames=false]{hyperref}")
s = s.replace("\\begin{figure}[H]", "\\begin{figure}[!tbp]")
(D / "main.tex").write_text(s)
# A complete auditable table set accompanies the compact manuscript tables.
shutil.copytree(O, D / "evidence", dirs_exist_ok=True)
for file in [
    "source_manifest.json",
    "tested_versions.json",
    "report_facts.json",
    "run_summary.json",
    "clean_run_verification.json",
    "slope_break_HAC.json",
    "runtime_environment.json",
]:
    if (R / "outputs" / file).exists():
        shutil.copy2(R / "outputs" / file, D / "evidence" / file)
print(
    "Manuscript rebuilt from",
    len(pd.read_csv(O / "master_model_comparison.csv")),
    "master rows",
)
