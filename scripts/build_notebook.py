"""Build the self-contained starter notebook. Do not overwrite later hand edits.

Use --force only when intentionally regenerating from these sources.
"""
import argparse
from pathlib import Path
import nbformat as nbf

root = Path(__file__).resolve().parents[1]
target = root / "notebooks/Project4_TeamTBD.ipynb"
parser = argparse.ArgumentParser()
parser.add_argument("--force", action="store_true")
args = parser.parse_args()
if target.exists() and not args.force:
    raise SystemExit("Notebook exists. Preserve edits, or explicitly pass --force.")

cells = []
def md(text):
    cells.append(nbf.v4.new_markdown_cell(text))
def code(text):
    cells.append(nbf.v4.new_code_cell(text))

md("""# 1. Title, team members and summary
## Project 4: Machine Learning in Climate Analysis and Prediction

**Status:** setup and Phase 1 checkpoint; later experiments are pending.
**Team:** number and full names pending (GitHub: Edariel22 and pologram1).
**Repository:** https://github.com/Edariel22/Project4_Climate_Analysis (currently public).

This working notebook establishes reproducible data acquisition, checks coverage and missingness, computes 1951-1980 temperature anomalies and begins the required EDA. It does not yet report trained-model results. Replace this paragraph with a one-paragraph summary of measured findings at final submission. The selected local reference is Meteostat station 78526, about 21.3 km from UAGM Gurabo, with data for 2000-2025. See the station-selection note for coverage and source limitations.

The nine top-level sections follow D1 exactly. Work progresses through Phases 1-5 in the assignment; the presentation order places unsupervised analysis before supervised models. See `docs/PROJECT_CHECKLIST.md` in GitHub for the complete requirement map.
""")
md("""# 2. Imports, configuration and data loading

**Run:** use Python 3.12 or 3.13 and Run all. In Colab, the first cell installs pinned dependencies; a fresh CPU runtime is sufficient for this checkpoint. Data are downloaded from the original public sources, cached locally and excluded from Git. The city CSV is large. This notebook contains its helpers so a Drive copy does not need private-repository credentials.

Sources: [Berkeley Earth/Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data), [NOAA GML](https://gml.noaa.gov/ccgg/trends/data.html), [Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package), [Meteostat](https://dev.meteostat.net/python/). Preserve source attribution and verify licenses before redistribution.
""")
reqs = (root / "requirements.txt").read_text().splitlines()
code("""import sys, subprocess, importlib.util
from pathlib import Path
IN_COLAB = importlib.util.find_spec('google') is not None and importlib.util.find_spec('google.colab') is not None
""" + f"PINNED_PACKAGES = {reqs!r}\n" + """if IN_COLAB:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *PINNED_PACKAGES])
print('Python:', sys.version)
ROOT = Path('/content/project4') if IN_COLAB else (Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd())
for folder in ['data/raw', 'data/processed', 'figures', 'docs']:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)
print('Working directory:', ROOT)
""")
code((root / "src/project_setup.py").read_text(encoding="utf-8"))
code("""import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown
from importlib.metadata import version
np.random.seed(SEED)
sns.set_theme(style='whitegrid', context='notebook')
plt.rcParams.update({'figure.figsize': (10, 4), 'figure.dpi': 110})
STATION_ID = '78526'  # UAGM Gurabo regional reference; 25 years with >=90% tmax coverage.
STATION_START, STATION_END = '2000-01-01', '2025-12-31'
print({package: version(package) for package in ['numpy', 'pandas', 'scikit-learn', 'meteostat', 'kagglehub']})
paths = acquire_data(ROOT, STATION_ID, STATION_START, STATION_END)
glob, co2, rain, station = load_core(paths)
cities, climatology, city_summary, city_missingness = scan_cities(paths['cities'])
summary = {'global': coverage(glob, 'dt'), 'co2': coverage(co2, 'dt'),
           'rain': coverage(rain, 'Date', 'Location'), 'cities_full_file': city_summary}
if station is not None:
    summary['station'] = coverage(station, 'time')
coverage_table = pd.DataFrame(summary).T
display(coverage_table)
coverage_table.to_csv(ROOT / 'docs/data_coverage.csv', index_label='dataset')
display(city_coverage(cities))
city_coverage(cities).to_csv(ROOT / 'docs/city_coverage.csv', index=False)
for name, frame in [('global', glob), ('co2', co2), ('rain', rain), ('selected_cities', cities)]:
    print(name, 'shape:', frame.shape)
    display(frame.head())
    display(frame.isna().mean().sort_values(ascending=False).rename('missing_fraction').to_frame())
display(city_missingness.to_frame())
if station is None:
    print('LOCAL STATION PENDING: campus is not confirmed; no station data or heat results are claimed.')
else:
    print('station shape:', station.shape)
    display(station.head())
    display(station.isna().mean().to_frame('missing_fraction'))
""")
md("""### UAGM Gurabo station: selection and quality

Station **78526 / TJSJ**, San Juan International Airport, is approximately **21.3 km** from the campus reference. We requested **2000-2025**, a 26-year period. It is the closer of two stations returned by the Meteostat catalog within 50 km; the alternative has only about five years of daily data.

This coastal station is a regional reference, not an on-campus instrument. Data use Meteostat's aggregated `Provider.DAILY` product, which is not certified observation-only. No application-level interpolation was used. See [selection and provenance notes](https://github.com/Edariel22/Project4_Climate_Analysis/blob/main/docs/STATION_SELECTION.md).
""")
code("""station_calendar = station.set_index('time').sort_index().reindex(pd.date_range(STATION_START, STATION_END, freq='D'))
station_calendar.index.name = 'time'
valid_tmax = station_calendar.tmax.notna()
station_annual_coverage = pd.DataFrame({'valid_tmax': valid_tmax.resample('YS').sum(), 'expected_days': valid_tmax.resample('YS').size()})
station_annual_coverage['coverage'] = station_annual_coverage.valid_tmax / station_annual_coverage.expected_days
print(f'Valid tmax: {valid_tmax.sum():,}/{len(valid_tmax):,} days ({valid_tmax.mean():.1%})')
print('Years with >=90% tmax coverage:', (station_annual_coverage.coverage >= 0.90).sum())
display(station_annual_coverage)
display(station_calendar.isna().mean().to_frame('missing_fraction_calendar'))
station_annual_coverage.to_csv(ROOT / 'docs/station_coverage_78526.csv', index_label='year_start')
display(Markdown('**Quality note:** 2009 has only 66.3% maximum-temperature coverage. Later heat-trend analysis must flag low-coverage years and report observed-day rates alongside counts. The 90% annual completeness threshold is our quality-control choice.'))
""")
md("""# 3. Exploratory data analysis

Phase 1: at least six figures, each followed by an interpretation. This checkpoint uses actual observed data only. Local heat-frequency analysis will be added in Phase 5; station coverage is checked below. Early temperature estimates and uncertainty columns must be discussed; no gaps are silently interpolated.
""")
code("""annual = annual_anomalies(glob)
def save_figure(name):
    plt.tight_layout()
    plt.savefig(ROOT / 'figures' / (name + '.png'), dpi=160, bbox_inches='tight')
    plt.show()

ax = annual['mean'].plot(label='Annual mean (12 observed months)')
annual['mean'].rolling(10, min_periods=10).mean().plot(ax=ax, label='Trailing 10-year mean', linewidth=2.5)
ax.set(title='Global land-and-ocean temperature: observed historical coverage', xlabel='Year', ylabel='Temperature (°C)')
ax.legend()
save_figure('01_global_temperature')
display(Markdown(f"**Interpretation:** Complete annual observations span {annual['mean'].dropna().index.min().year}–{annual['mean'].dropna().index.max().year}; the 10-year curve smooths short-term variability. This historical source does not establish coverage up to the current year."))
""")
code("""ax = annual['anomaly'].plot(label='Annual anomaly')
annual['rolling_10y'].plot(ax=ax, label='Trailing 10-year anomaly', linewidth=2.5)
ax.axhline(0, color='black', linewidth=0.8)
ax.set(title='Global anomalies relative to 1951–1980', xlabel='Year', ylabel='Anomaly (°C)')
ax.legend()
save_figure('02_global_anomalies')
display(Markdown('**Interpretation:** Zero represents the mean of the 30 complete annual values in 1951–1980; positive values are warmer than that reference. Quantified warming slopes and confidence intervals belong to Phase 2 and have not been estimated here.'))
""")
code("""ax = co2.plot(x='dt', y='average', legend=False)
ax.set(title='Mauna Loa monthly atmospheric CO₂', xlabel='Date', ylabel='CO₂ (ppm)')
save_figure('03_co2')
display(Markdown(f"**Interpretation:** There are {co2['average'].notna().sum():,} valid monthly CO₂ measurements in this snapshot. The series combines long-term change with seasonal variability; plotting it alongside temperature does not by itself demonstrate causation."))
""")
code("""seasonal_cities = cities[cities.City.isin(['London', 'Cairo', 'Sydney'])].copy()
seasonal_cities = seasonal_cities[seasonal_cities.dt.between('1961-01-01', '1990-12-31')]
seasonal_cities['month'] = seasonal_cities.dt.dt.month
cycles = seasonal_cities.groupby(['month', 'City']).AverageTemperature.mean().unstack('City')
ax = cycles.plot(marker='o')
ax.set(title='Monthly temperature cycles, 1961–1990', xlabel='Month', ylabel='Mean temperature (°C)', xticks=range(1, 13))
save_figure('04_monthly_cycles')
peaks = ', '.join(f'{city}: month {int(cycles[city].idxmax())}' for city in cycles)
display(Markdown(f'**Interpretation:** Peak climatological temperatures occur in {peaks}. Comparing Northern and Southern Hemisphere cities reveals the seasonal timing difference.'))
""")
code("""rain_frequency = rain.assign(rain_label=rain.RainTomorrow.map({'Yes': 1.0, 'No': 0.0})).groupby('Location').rain_label.mean().sort_values()
ax = rain_frequency.plot.bar(figsize=(14, 5), color='#287b8e')
ax.set(title='Next-day rain frequency by Australian location', xlabel='Location', ylabel='Fraction of observed labels with rain')
save_figure('05_rain_frequency')
display(Markdown(f'**Interpretation:** Observed rain-label prevalence ranges from {rain_frequency.min():.1%} to {rain_frequency.max():.1%} across locations; missing target labels are excluded from the denominator. This variation motivates reporting per-location test accuracy as well as class-sensitive metrics.'))
""")
code("""missing = rain.isna().mean().sort_values(ascending=False)
ax = missing.plot.bar(color='#be7946', figsize=(12, 4))
ax.set(title='Rain in Australia: missing fraction by field', xlabel='Field', ylabel='Missing fraction')
save_figure('06_missingness')
display(Markdown(f'**Interpretation:** {missing.index[0]} has the largest missing fraction ({missing.iloc[0]:.1%}). Predictor imputation must be fitted inside training folds, while rows without the target cannot supply supervised training labels.'))
""")
code("""uncertainty_column = GLOBAL_SERIES + 'Uncertainty'
if uncertainty_column in glob:
    unc = glob.set_index('dt')[uncertainty_column].loc['1850':].resample('YS').mean()
    ax = unc.plot()
    ax.set(title='Mean of source monthly temperature uncertainties by year', xlabel='Year', ylabel='Source uncertainty (°C)')
    save_figure('07_source_uncertainty')
    display(Markdown('**Interpretation:** This summarizes the uncertainty values supplied with the monthly observations. Averaging those values is descriptive and is not a confidence interval for the annual mean or warming trend.'))
""")
md("""# 4. Preprocessing and train / validation / test split

Phase 1 documents the prescribed boundaries; model fitting begins in later phases.

- Global trends: use 1850 onward, compare 1850–1974 and 1975–latest available. Align annual CO₂ from 1958 onward.
- Monthly forecasting: training target dates through 2000, test target dates 2001–2013. TimeSeriesSplit only within training; fit imputers/scalers inside each model Pipeline. A direct 12-month target requires a 12-month purge at validation boundaries so training targets are observed by the issue date.
- Rain: train dates through 2015, test dates from 2016. CV splits must operate on **unique dates**, keeping all locations on the same day together; a one-day purge protects next-day targets.
- Heat: use station 78526 (2000-2025); freeze a chronological test interval before modeling. Reindex the daily calendar before creating tomorrow's label. Keep missing tomorrow temperatures as missing targets.
- The assignment's primary heat definition is the full-record 90th percentile; report a training-only-threshold sensitivity analysis separately.
- No missing targets are imputed. Lag/rolling features must only use observations available at issuance. Never forward/back-fill across holdout boundaries.
""")
code("""split_counts = city_coverage(cities)
display(split_counts[['city', 'country', 'test_valid_months', 'test_expected_months']])
rain_labelled = rain.dropna(subset=['RainTomorrow'])
print('Rain train rows through 2015:', int((rain_labelled.Date < '2016-01-01').sum()))
print('Rain test rows from 2016:', int((rain_labelled.Date >= '2016-01-01').sum()))
print('Duplicate rain location/date keys:', int(rain.duplicated(['Location', 'Date']).sum()))
print('Duplicate selected city/month/geography keys:', int(cities.duplicated(['City', 'Country', 'Latitude', 'Longitude', 'dt']).sum()))
print('Do not infer complete 2013 coverage from the requested test end date.')
""")
md("""# 5. Unsupervised analysis (PCA and k-Means)

**Phase 4 pending.** The source scan has prepared 1961–1990 climatologies for all eligible cities (12 monthly means, annual range, latitude). Eligibility requires >=24 years per calendar month; there is no random subsampling. Fit scaling and PCA, interpret PC1/PC2 loadings, select k using elbow and silhouette, and map coordinates. Source Köppen labels for at least 20 recognizable cities and assess agreement with a contingency table plus ARI/NMI; cluster labels are arbitrary.
""")
code("""print('Cities eligible for clustering:', len(climatology))
display(climatology.head())
print('PCA and k-Means have not yet been fitted.')
""")
md("""# 6. Supervised models

**Phases 2, 3 and 5 pending.** Each subsection below must contain its Pipeline, tuning search, temporal CV mean/SD, best parameters, fit/predict times and final held-out metrics. No model is marked trained by merely listing it. Compare all models on the same eligible rows and horizons.
""")
models = [
('Linear regression', 'Global annual trend and each city forecast; slope per decade with an autocorrelation-aware 95% CI.'),
('Ridge', 'City forecasts and annual global models with/without CO₂; tune alpha.'),
('Lasso', 'City forecasts and annual global models with/without CO₂; tune alpha and monitor convergence.'),
('Polynomial regression', 'Degree 2 and 3 global trends; city forecasts with PolynomialFeatures inside the Pipeline.'),
('Logistic regression', 'Rain and local heat classifiers; tune regularization and address imbalance.'),
('k-Nearest Neighbors', 'Regressor for every city; classifiers for rain and heat; tune neighbors and weights after fold-fitted scaling.'),
('Naive Bayes', 'Rain and heat classifiers; select an appropriate distribution and tune smoothing.'),
('Support Vector Machine', 'SVR city forecasts; SVC rain and heat; tune C, kernel and relevant scale parameters.'),
('Decision tree', 'Regression and both classification tasks; tune depth and minimum leaf size.'),
('Random forest', 'Regression and both classification tasks; tune tree count, depth and leaf size; seed 42.'),
('Gradient boosting', 'Regression and both classification tasks; tune learning rate, stages and tree complexity.'),
('Multilayer perceptron', 'MLPRegressor and MLPClassifier; tune architecture, regularization and learning rate; record convergence.'),
]
for name, task in models:
    md(f'## {name}\n\n**Not trained yet.** {task}')
md("""## Baselines and local frequency trend

Seasonal naive predicts the same month last year. For a forecast issued at t with target t+12, its prediction is the observed T(t). Use a majority-class baseline for event classification as context. Count local heat days by year, include valid observation counts/rates, and fit a linear trend with uncertainty. These analyses remain pending.
""")
md("""# 7. Model comparison table and plots

**Pending measured experiments.** A master table must identify task, city/station, horizon, model, best hyperparameters, CV mean/SD, held-out metrics, training time and prediction time. Regression needs RMSE/MAE/R² and seasonal-naive skill; classification needs precision/recall/F1/ROC-AUC/confusion matrices and Australian per-location accuracy. Add forecast-vs-actual plots for three cities, ROC curves and a climate-zone world map. Empty cells below are intentional, not zero scores.
""")
code("""comparison = pd.DataFrame(columns=['task', 'location', 'horizon', 'model', 'best_hyperparameters',
    'cv_metric', 'cv_mean', 'cv_std', 'test_rmse', 'test_mae', 'test_r2', 'seasonal_naive_skill',
    'test_precision', 'test_recall', 'test_f1', 'test_roc_auc', 'training_seconds', 'prediction_seconds'])
display(comparison)
""")
md("""# 8. Interpretation

Complete after evaluation:
1. Warming per decade, 95% confidence interval and change since 1975.
2. Twelve-month forecast accuracy, skill over seasonal naive, and how errors change with horizon/city.
3. PCA interpretations and cluster agreement with climate zones for 20 cities.
4. Rain/heat predictive ability and local heat-frequency change.

Add feature importance (prefer held-out permutation importance where appropriate), false-negative/false-positive analysis and errors by location/season. Explain why CO₂ association alone does not prove causation, how instruments/station moves/missing records bias trends, and how local heat predictions could inform health or energy planning.
""")
md("""# 9. Conclusions and limitations

This checkpoint establishes data access and exploratory checks. Model performance and scientific conclusions remain unmeasured. Known limitations include historical source endpoints, incomplete months, source uncertainty, the coastal station's representativeness of inland Gurabo, mixed source provenance, non-random geographic coverage and the assignment's full-record heat threshold. The report currently contains methodological intentions and must be updated only from measured results.

**Final checks:** all models tuned with temporal CV; no held-out tuning; all nine sections complete; full clean Colab/Kaggle run; source citations; both students' commits; IEEE report 8–12 pages; slides 10–12 pages; instructor access. See GitHub's requirements tracker.

**Implementation references:** [KaggleHub](https://github.com/Kaggle/kagglehub), [Meteostat daily](https://dev.meteostat.net/python/api/meteostat.daily), [scikit-learn leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html), and the supplied Project 4 assignment. Record AI assistance according to course policy and distinguish it from each student's contributions.
""")
nb = nbf.v4.new_notebook(cells=cells)
nb.metadata.update(kernelspec={'display_name':'Python 3', 'language':'python', 'name':'python3'},
                   language_info={'name':'python', 'version':'3.13.2'},
                   colab={'name': target.name, 'provenance': []})
nbf.validate(nb)
nbf.write(nb, target)
print(target)
