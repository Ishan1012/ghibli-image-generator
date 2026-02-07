import streamlit as st
from ghibli_image.assets.styles import load_css
from ghibli_image.utils.session_state import init_session_state
from ghibli_image.components.hero import render_hero
from ghibli_image.components.input_section import render_input
from ghibli_image.services.history_service import render_latest_image
from ghibli_image.components.footer import render_footer

def main():
    st.set_page_config(
        page_title="Ghibli AI Studio",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    load_css()
    init_session_state()

    render_hero()
    render_input()
    render_latest_image()
    render_footer()

if __name__ == "__main__":
    main()