#!/usr/bin/env bash
# Mac / Linux launcher
cd "$(dirname "$0")"
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "Login: admin / Admin@123"
python -m streamlit run dashboard.py
