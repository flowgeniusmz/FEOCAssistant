import streamlit as st
from st_login_form import login_form
from supabase import create_client, client

def get_loginform():
    client = login_form()

    if st.session_state.authenticated:
        if st.session_state.username:
            st.success(f"Welcome {st.session_state.username}")
        else:
            st.success("Welcome Guest")
    else:
        st.error("Not Authenticated")

#https://app.supabase.com/project/rbaawqpeyigwmzukrmvc/editor/28594
#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#create-a-supabase-database
