import torch
from diffusers import AutoPipelineForText2Image, LCMScheduler
from peft import PeftModel
import streamlit as st
import os

@st.cache_resource
def load_pipeline(model_id: str, lora_path: str):
    device = "cpu"

    pipe = AutoPipelineForText2Image.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True
    )

    pipe.scheduler = LCMScheduler.from_config(
        pipe.scheduler.config,
        timestep_spacing="trailing"
    )

    # Load LoRA
    pipe.unet = PeftModel.from_pretrained(
        pipe.unet,
        lora_path,
        is_trainable=False
    )

    pipe.enable_attention_slicing()
    pipe.to(device)
    pipe.unet.eval()

    return pipe