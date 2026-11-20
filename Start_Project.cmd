@echo off
setlocal
cd /d "%~dp0"
set "PROJECT_CONDA=%USERPROFILE%\anaconda3\condabin\conda.bat"
if not exist "%PROJECT_CONDA%" (
  echo Anaconda was not found at %USERPROFILE%\anaconda3.
  echo Open Anaconda Prompt, activate climate-team4, and run python -m jupyterlab.
  pause
  exit /b 1
)
call "%PROJECT_CONDA%" run --no-capture-output -n climate-team4 python -m jupyterlab notebooks/Project4_Team4.ipynb
if errorlevel 1 pause
