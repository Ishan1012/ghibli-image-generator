import streamlit as st

def render_hero():
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Ghibli AI Studio</h1>
        <p class="hero-subtitle">
            Transform your imagination into stunning Studio Ghibli-style artwork with the power of AI
        </p>
    </div>
    """, unsafe_allow_html=True)
