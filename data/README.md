# Data access and provenance

Run the acquisition cell in the notebook, or `python scripts/prepare_data.py` from the repository root. Source data are cached under `data/raw/` and excluded from Git. Do not commit Kaggle credentials, tokens or downloaded CSVs. The first city download is large (hundreds of MB).

| Source | Required files / role | Official access |
|---|---|---|
| Berkeley Earth via Kaggle | GlobalTemperatures.csv and GlobalLandTemperaturesByCity.csv | https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data |
| NOAA GML / Scripps | co2_mm_mlo.csv; monthly ppm | https://gml.noaa.gov/ccgg/trends/data.html |
| Rain in Australia, jsphyg | weatherAUS.csv | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package |
| Meteostat | Daily observations for a confirmed local station | https://dev.meteostat.net/python/ |

Selected station for UAGM Gurabo: **78526 / TJSJ (San Juan International Airport)**, approximately 21.3 km from campus. Download period: **2000-2025**. The default preparation script now includes it. See [station selection](../docs/STATION_SELECTION.md) for the candidate comparison, calendar-based coverage and mixed-source provenance caveat. The full-record heat threshold will refer to this explicitly selected period.

`kagglehub.dataset_download` retrieves version 2 of each public Kaggle source. The initial local snapshot was downloaded through Kaggle's official API; the notebook's KaggleHub method was separately verified on the global CSV. Some environments may require Kaggle authentication or acceptance of dataset terms; never embed credentials in the notebook. Download failures are errors, not permission to substitute made-up data. NOAA is downloaded directly. Meteostat 2.1.5 uses `meteostat.daily(...).fetch()`, rather than the older `Daily` class in the handout.

The raw manifest records retrieval timestamps, resolved Kaggle cache paths (including source version when available), file sizes and SHA256 hashes. Preserve this local snapshot for exact reproduction: NOAA and live provider data can be revised. A new download from a live source is not guaranteed byte-identical. Public aggregate coverage is saved under `docs/`.

Licensing: the handout identifies NOAA as public-domain data and Meteostat as CC BY 4.0. Cite NOAA GML/Scripps and Meteostat plus upstream providers as applicable; verify the Kaggle dataset-page terms before redistribution. This repository does not redistribute raw data.

City processing scans the full file in chunks. It retains all dates for the ten named city/country pairs and aggregates 1961-1990 climatologies across all cities. Clustering eligibility requires >=24 valid observations for each calendar month; no random sampling is used. Report names, coordinates, eligible/excluded counts and actual date coverage.
