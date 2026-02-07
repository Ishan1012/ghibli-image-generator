import streamlit as st

def init_session_state():
    if "image_history" not in st.session_state:
        st.session_state.image_history = []
