import torch
from diffusers import StableDiffusionPipeline
from peft import PeftModel
import os
import streamlit as st
from ghibli_image.services.pipeline_loader import load_pipeline

class GhibliImageGenerator:
    def __init__(self):
        self.model_id = "segmind/tiny-sd"
        self.lora_path = "./data/ghibli_model"
        # Use GPU on Streamlit Cloud if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = load_pipeline(
            self.model_id,
            self.lora_path,
            self.device
        )

    def generate(self, prompt: str):
        self.pipe.scheduler.set_timesteps(30)

        generator = torch.Generator(device=self.device)
        generator.manual_seed(torch.seed())

        with torch.no_grad():
            image = self.pipe(
                prompt,
                num_inference_steps=30,
                guidance_scale=8.0,
                height=384,
                width=384,
                generator=generator
            ).images[0]
        return image
