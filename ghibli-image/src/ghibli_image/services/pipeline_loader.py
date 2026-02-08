import torch
from diffusers import AutoPipelineForText2Image, LCMScheduler
import streamlit as st

@st.cache_resource
def load_pipeline():
    device = "cpu"

    pipe = AutoPipelineForText2Image.from_pretrained(
        "Ishan1000/tiny-sd-ghibli-lcm",
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )

    pipe.scheduler = LCMScheduler.from_config(
        pipe.scheduler.config,
        timestep_spacing="trailing"
    )

    pipe.enable_attention_slicing()
    pipe.to(device)
    pipe.unet.eval()

    return pipe