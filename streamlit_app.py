import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ABSA × VAST — The Economics of Sovereign Intelligence",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background: #0A1628; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }
    iframe { border: none !important; }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

html_content = Path("absa_microsite.html").read_text(encoding="utf-8")
components.html(html_content, height=8000, scrolling=True)