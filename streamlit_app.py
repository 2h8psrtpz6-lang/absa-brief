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
    """Returns True if the user entered the correct password."""
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't keep it in memory
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run
        st.markdown(
            """
            <style>
                .stApp { background: #0A1628; }
                .block-container { padding-top: 6rem !important; }
                h1, h2, h3, label, p { color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
                .stTextInput input {
                    background: #112040 !important;
                    color: #FFFFFF !important;
                    border: 1px solid rgba(0,212,255,0.3) !important;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown("### VAST DATA × ABSA — Executive Brief")
        st.markdown("This site is confidential. Please enter the access passcode to continue.")
        st.text_input("Passcode", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("### VAST DATA × ABSA — Executive Brief")
        st.text_input("Passcode", type="password", on_change=password_entered, key="password")
        st.error("Incorrect passcode.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# ─── Hide Streamlit chrome and render the microsite ───
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