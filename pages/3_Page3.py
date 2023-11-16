import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FlowGenius", "Page2")
    set_page_overview("Main Header", "description text...")
