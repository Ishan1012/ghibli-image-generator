# app.py (repo root)

import os
os.environ["HF_HOME"] = "/tmp/hf_cache"
os.environ["TORCH_HOME"] = "/tmp/torch_cache"

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "src"))

import streamlit as st
from ghibli_image.main import render_app

def main():
    render_app()

if __name__ == "__main__":
    main()