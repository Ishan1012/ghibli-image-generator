import torch
from diffusers import StableDiffusionPipeline
from peft import PeftModel
import os
import streamlit as st

class GhibliImageGenerator:
    def __init__(self):
        self.model_id = "segmind/tiny-sd"
        self.lora_path = "./data/ghibli_model"
        # Use GPU on Streamlit Cloud if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = self._load_pipeline()

    @st.cache_resource
    def _load_pipeline(self):
        pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto",
            low_cpu_mem_usage=True
        )

        pipe.unet = PeftModel.from_pretrained(
            pipe.unet,
            self.lora_path,
            is_trainable=False
        )

        pipe = pipe.to(self.device)
        pipe.enable_attention_slicing()
        return pipe

    def generate(self, prompt: str):
        with torch.no_grad():
            image = self.pipe(
                prompt,
                num_inference_steps=30,
                guidance_scale=8.0,
                height=384,
                width=384,
                generator=torch.Generator(device=self.device).manual_seed(42)
            ).images[0]
        return image
