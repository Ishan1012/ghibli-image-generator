# Deployment Guide

## Setup for Production Server

### Step 1: Clone repository (models NOT included)
```bash
git clone <your-repo-url>
cd ghibli-image
poetry install
```

### Step 2: Download model to server cache

Set cache directory and run setup script:

**Option A: Using environment variable (Recommended)**
```bash
export MODEL_CACHE_DIR=/var/cache/ghibli-models
python scripts/setup_models.py
```

**Option B: Default location**
```bash
python scripts/setup_models.py
# Downloads to ./data/models/segmind
```

### Step 3: Run the app

**Local development:**
```bash
poetry run streamlit run src/ghibli_image/main.py
```

**Production with custom cache:**
```bash
export MODEL_CACHE_DIR=/var/cache/ghibli-models
poetry run streamlit run src/ghibli_image/main.py
```

### Environment Variables

- `MODEL_CACHE_DIR`: Path to cache downloaded models (default: `./data/models/segmind`)
- `LORA_MODEL_PATH`: Path to LoRA model weights (default: `./data/ghibli_model`)

### Docker Example

```dockerfile
FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install poetry && poetry install --no-root

# Pre-download models during build
ENV MODEL_CACHE_DIR=/app/models
RUN python scripts/setup_models.py

EXPOSE 8501
CMD ["poetry", "run", "streamlit", "run", "src/ghibli_image/main.py"]
```

### GitHub - What's Ignored

Model files are NOT committed to Git (.gitignore includes):
- `data/` - Model cache directory
- `models/` - Alternative model directory
- `final_model/` - LoRA weights

These will be downloaded fresh on each deployment.

# Streamlit Cloud Deployment Guide

## Prerequisites
- GitHub account with this repository
- Streamlit Cloud account (https://streamlit.io/cloud)

## Deployment Steps

1. Push your code to GitHub
2. Go to https://share.streamlit.io/
3. Click "New app"
4. Select your repository, branch, and main file (`src/ghibli_image/main.py`)
5. Click "Deploy"

## Important Notes

- Model files in `data/` must be committed to GitHub (use Git LFS for large files)
- Cold start times may be long due to model loading
- Use `@st.cache_resource` for expensive operations
- Streamlit Cloud has CPU-only instances by default (GPU requires paid tier)

## Environment Setup

The deployment uses `requirements.txt` automatically.
