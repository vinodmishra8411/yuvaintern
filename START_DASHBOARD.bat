@echo off
cd /d "%~dp0"
title Retail Anomaly Command Centre
echo ==========================================
echo   RETAIL ANOMALY COMMAND CENTRE - STARTUP
echo ==========================================
set PYCMD=
where py >nul 2>nul && set PYCMD=py
if "%PYCMD%"=="" (where python >nul 2>nul && set PYCMD=python)
if "%PYCMD%"=="" (
  echo Python was not found. Install Python 3.10+ from python.org and tick "Add Python to PATH".
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PYCMD% -m venv .venv
)
call ".venv\Scripts\activate.bat"
echo Installing/checking dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
  echo Dependency installation failed. Check your internet connection and try again.
  pause
  exit /b 1
)
echo.
echo Starting dashboard. First launch creates 50,000 sample transactions and trains the AI models (about 1 minute).
echo Login: admin / Admin@123
python -m streamlit run dashboard.py
pause
