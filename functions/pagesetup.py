import streamlit as st
import streamlit.components.v1 as c
from streamlit_elements import elements, mui, html
import hydralit_components as hc

### 1. TITLE and SUBTITLE
def set_title(varTitle, varSubtitle):
        st.markdown(f"""# {varTitle} <span style=color:#7ab3ba><font size=5>{varSubtitle}</font></span>""",unsafe_allow_html=True)
        st.divider()

### 2. PAGE OVERVIEW
def set_page_overview(varHeader, varText):
        st.markdown(f"#### {varHeader}")
        st.markdown(f"{varText}")
        st.divider()

### 3. HYDRALIT NAVBAR

def set_nav_bar():
        navbar_menu_items = [
                {'icon': "far fa-chart-bar", 'label':"Item1", 'ttip': "tooltip"},
                {'icon': "fas fa-tachometer-alt", 'label':"Item2",'ttip':"tooltip"},
                {'icon': "far fa-copy", 'label':"Item3", 'ttip': "Tooltip", 'submenu': [{'icon': "fa fa-paperclip", 'label': "Subitem1"}, {'icon': "fa fa-database", 'label': "subitem2"}, {'icon': "far fa-copy", 'label': "Subitem3"}]}
        ]
        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(
                menu_definition = navbar_menu_items, 
                override_theme = over_theme,
                home_name = "Home",
                login_name = "Logout",
                hide_streamlit_markers=False,
                sticky_nav = True,
                sticky_mode = "pinned"
        )
        
