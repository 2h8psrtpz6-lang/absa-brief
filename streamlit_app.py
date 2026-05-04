import streamlit as st
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
            h1, h2, h3, label, p, div { color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
            .stTextInput input {
                background: #112040 !important;
                color: #FFFFFF !important;
                border: 1px solid rgba(0,212,255,0.3) !important;
            }
        </style>
        """, unsafe_allow_html=True)
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

# ─── Hide ALL Streamlit chrome ───
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden !important; display: none !important; }
    .stApp { background: #0A1628; }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    .main > div:first-child { padding: 0 !important; }
    [data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    .stApp > div:first-child { margin-top: -80px; }
</style>
""", unsafe_allow_html=True)

# ─── Render the microsite directly (no iframe) ───
html_content = Path("absa_microsite.html").read_text(encoding="utf-8")
st.markdown(html_content, unsafe_allow_html=True)