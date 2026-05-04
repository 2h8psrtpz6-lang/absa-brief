import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ABSA x VAST - The Economics of Sovereign Intelligence",
    page_icon=":diamond_shape_with_a_dot_inside:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Password gate
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    gate_css = """
    <style>
        .stApp { background: #0A1628; }
        .block-container { padding-top: 6rem !important; max-width: 600px !important; }
        h1, h2, h3, label, p, div { color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
        .stTextInput input {
            background: #112040 !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(0,212,255,0.3) !important;
        }
    </style>
    """

    if "password_correct" not in st.session_state:
        st.markdown(gate_css, unsafe_allow_html=True)
        st.markdown("### VAST DATA x ABSA - Executive Brief")
        st.markdown("This site is confidential. Please enter the access passcode to continue.")
        st.text_input("Passcode", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown(gate_css, unsafe_allow_html=True)
        st.markdown("### VAST DATA x ABSA - Executive Brief")
        st.text_input("Passcode", type="password", on_change=password_entered, key="password")
        st.error("Incorrect passcode.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# Hide Streamlit chrome
hide_chrome = """
<style>
    #MainMenu, footer, header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden !important;
        display: none !important;
        height: 0 !important;
    }
    .stApp { background: #0A1628; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    [data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
    iframe { border: none !important; width: 100% !important; }
</style>
"""
st.markdown(hide_chrome, unsafe_allow_html=True)

# Load HTML and patch the hero min-height issue for iframe rendering
html_content = Path("absa_microsite.html").read_text(encoding="utf-8")
html_content = html_content.replace("min-height: 100vh;", "min-height: 820px;")

components.html(html_content, height=6500, scrolling=True)
