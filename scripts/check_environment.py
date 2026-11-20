"""Check the local environment and start a real kernel without retraining models."""
import importlib
import importlib.metadata
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    packages = {
        "numpy": "numpy", "pandas": "pandas", "scipy": "scipy",
        "scikit-learn": "sklearn", "matplotlib": "matplotlib",
        "seaborn": "seaborn", "statsmodels": "statsmodels.api",
        "rasterio": "rasterio", "meteostat": "meteostat",
        "kagglehub": "kagglehub", "nbformat": "nbformat",
        "nbclient": "nbclient", "ipykernel": "ipykernel",
        "jupyterlab": "jupyterlab",
    }
    versions = {}
    for package, module in packages.items():
        importlib.import_module(module)
        versions[package] = importlib.metadata.version(package)

    import nbformat
    from nbclient import NotebookClient
    import pandas as pd

    source = nbformat.read(ROOT / "notebooks/Project4_Team4.ipynb", as_version=4)
    nbformat.validate(source)
    smoke = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(
        "import sys, numpy as np, pandas as pd, rasterio\n"
        "from sklearn.linear_model import LinearRegression\n"
        "x = np.arange(6).reshape(-1, 1)\n"
        "model = LinearRegression().fit(x, 2*x.ravel()+1)\n"
        "assert np.allclose(model.predict([[6]]), [13])\n"
        "assert 'climate-team4' in sys.executable\n"
        "print('Project kernel and numerical libraries are working.')"
    )])
    NotebookClient(smoke, timeout=120, kernel_name="climate-team4").execute(
        cwd=str(ROOT)
    )
    master = pd.read_csv(ROOT / "outputs/phase1/master_model_comparison.csv")
    assert len(master) == 245, "Unexpected imported results table"
    report = {
        "status": "passed", "python": sys.version.split()[0],
        "python_executable": sys.executable, "versions": versions,
        "kernel_smoke_test": "passed", "notebook_schema": "valid",
        "saved_comparison_rows": len(master),
        "full_project_retrained": False,
    }
    destination = ROOT / "tmp/local_setup_check.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
