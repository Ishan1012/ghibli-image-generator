#!/usr/bin/env python
"""
Script to download models during deployment.
Run this once on the server before starting the app.

Usage:
    python scripts/setup_models.py
    
Or with custom cache directory:
    MODEL_CACHE_DIR=/var/cache/ghibli-models python scripts/setup_models.py
"""
import os
import sys
from pathlib import Path

# Add src to path to import ghibli_image
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ghibli_image.services.image_generator import GhibliImageGenerator

if __name__ == "__main__":
    print("🎨 Setting up Ghibli Image Generator...")
    print(f"Cache directory: {os.getenv('MODEL_CACHE_DIR', './data/models/segmind')}")
    
    try:
        GhibliImageGenerator.download_model()
        print("✅ Setup complete! Ready for deployment.")
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)
