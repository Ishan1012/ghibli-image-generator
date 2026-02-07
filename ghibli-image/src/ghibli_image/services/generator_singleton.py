import streamlit as st
from ghibli_image.services.image_generator import GhibliImageGenerator

@st.cache_resource
def get_generator():
    return GhibliImageGenerator()