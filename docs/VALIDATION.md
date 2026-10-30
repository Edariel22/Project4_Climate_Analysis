# Setup checkpoint validation

Validated on 2026-10-27 (America/La_Paz), using Windows and Python 3.13.2.

- Isolated `.venv` installed from pinned `requirements.txt`; `pip check` reports no broken requirements. Full tested Windows dependency snapshot saved in `requirements-lock-windows.txt`.
- All 13 code cells in the 35-cell notebook executed top to bottom without errors using nbclient and the project kernel. All nine required top-level sections are present. Later model sections explicitly state that experiments are pending.
- Three targeted unit tests pass: baseline anomalies, rejection of an incomplete baseline, and coverage/missingness counting. These use synthetic fixtures only, not synthetic project results.
- All three available data sources loaded from official downloads. Kaggle source versions verified as 2; the notebook's KaggleHub download method was tested separately on the global CSV. NOAA snapshot runs through September 2026. SHA256 provenance is in `data_manifest.json`; raw data remain local and ignored.
- City file scanned in chunks: 8,599,212 rows / 3,510 distinct city-country-coordinate keys. All ten working city/country selections exist after replacing missing Buenos Aires with La Plata. Check `city_coverage.csv` for valid test months.
- Seven labelled EDA figures generated, with interpretations in the notebook. Rain-frequency and seasonal-cycle figures visually checked for legibility.
- `git check-ignore` confirms the virtual environment, raw datasets and processed data are excluded.
- Local execution is verified. The notebook has been uploaded to Colab with outputs; a fresh Google-hosted runtime has not yet been tested. Teammate sharing is pending their Google email.
- Local station acquisition is not complete because the campus is pending. Model training, tuning, test metrics, final report, final slides and instructor sharing are not claimed complete.

Known report alignment items: the supplied draft is five pages; authors/team are placeholders; it calls the workflow public although the repository is private; its global-series wording must be aligned with the selected land-and-ocean primary analysis; and the city list must reflect La Plata. Original report files were preserved without invented results.

## Station checkpoint — 2026-10-28

- UAGM Gurabo confirmed. Selected Meteostat 78526 after comparing both catalog results within 50 km; documented distance, yearly coverage, weak year 2009 and source limitations.
- Fourth dataset downloaded locally for 2000-2025. Calendar completeness: 9,278/9,497 valid daily maximum temperatures; 25 years with >=90% coverage.
- Updated notebook executed all 14 code cells successfully, retaining all nine required sections. All three existing unit tests passed.
- The original campus-pending status above is superseded by this entry. Hosted Colab execution, team identity fields and editor sharing remain pending; the Drive notebook was updated in place with the executed local checkpoint.

## Integrated notebook organization — 2026-10-30

- The team reports successful execution of its integrated notebook. The attachment supplied for this update contains 20 code cells, all with null execution counts and no saved outputs.
- Current entry point: `notebooks/ProjectX_Team4.ipynb`. All nine required main sections are numbered in order. Markdown was reorganized; every uploaded code cell was preserved exactly.
- JSON/notebook schema, all code-cell syntax (with notebook magic handled), and the ordered nine-section structure were checked. Models were not rerun in this update.
- Corrected a markdown claim of an implemented 12-month-horizon experiment: the uploaded code implements rolling one-month forecasts only.
- README and data instructions now describe the integrated notebook; earlier checkpoint files and code remain available. The detailed current assessment is in `docs/RUBRIC_ALIGNMENT.md`.
- Successful execution is distinct from rubric completion. Saved results, sourced Köppen comparison, 12-month forecast, master table, interpretation, final report and slides remain outstanding.
