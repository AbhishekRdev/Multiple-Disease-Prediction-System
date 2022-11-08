import streamlit as st
import app0,app1,app2,app3
from streamlit_option_menu import option_menu
with st.sidebar:
    sel = option_menu(
        menu_title="Multiple Disease Prediction",
        options=["Diabetes Prediction", "Heart Disease",
                 "Cancer", "kidney"],
        icons=["graph-up-arrow", "graph-up-arrow",
               "graph-up-arrow", "graph-up-arrow"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"

    )

placeholder = st.empty()
if sel == "Diabetes Prediction":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = app0.app()


if sel == "Heart Disease":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = app2.app()


if sel == "Cancer":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = app1.app()


if sel == "kidney":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = app3.app()








st.info("Made with ⌚ by Abhishek & Tanish ©️ 2022")