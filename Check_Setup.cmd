@echo off
setlocal
cd /d "%~dp0"
call "%USERPROFILE%\anaconda3\condabin\conda.bat" run --no-capture-output -n climate-team4 python scripts/check_environment.py
pause
