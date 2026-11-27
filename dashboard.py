"""Retail Anomaly Command Centre. Run with:  streamlit run dashboard.py"""
import streamlit as st

st.set_page_config(page_title="Retail Anomaly Command Centre", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

from retail_anomaly import db, theme, ui  # noqa: E402  (must come after set_page_config)

db.init_db()
S = st.session_state
S.setdefault("dark", True)
st.markdown(theme.css(S["dark"]), unsafe_allow_html=True)
ui.reset_keys()

if not S.get("user"):
    ui.login_page()
    st.stop()

full = ui.load_scored()
page, flt = ui.render_sidebar(full)
ctx = ui.make_ctx(full, flt)
ui.PAGES[page](ctx)
