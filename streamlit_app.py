import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ABSA × VAST — The Economics of Sovereign Intelligence",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Password gate ───
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("""
        <style>
            .stApp { background: #0A1628; }
            .block-container { padding-top: 6rem !important; max-width: 600px !important; }
            h1, h2, h3, label, p, div { color: #FFFFFF !important; font-family: 'Inter