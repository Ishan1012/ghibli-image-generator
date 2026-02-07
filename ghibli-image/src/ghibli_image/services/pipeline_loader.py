import torch
import streamlit as st
from diffusers import StableDiffusionPipeline
from peft import PeftModel

@st.cache_resource
def load_pipeline(model_id: str, lora_path: str, device: str):
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        device_map=None,
        low_cpu_mem_usage=False
    )

    pipe.unet = PeftModel.from_pretrained(
        pipe.unet,
        lora_path,
        is_trainable=False
    )

    pipe = pipe.to(device)

    return pipe