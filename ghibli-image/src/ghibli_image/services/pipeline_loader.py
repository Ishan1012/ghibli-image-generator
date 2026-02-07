import torch
import streamlit as st
from diffusers import StableDiffusionPipeline
from peft import PeftModel

@st.cache_resource
def load_pipeline(model_id: str, lora_path: str):
    device = "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        device_map=None,
        low_cpu_mem_usage=True,
        force_download=True
    )

    pipe.unet = PeftModel.from_pretrained(
        pipe.unet,
        lora_path,
        is_trainable=False,
        from_hf_hub=True
    )

    pipe.enable_attention_slicing()
    return pipe.to(device)