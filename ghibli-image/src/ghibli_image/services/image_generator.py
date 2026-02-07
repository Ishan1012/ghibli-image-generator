import torch
from diffusers import StableDiffusionPipeline
from peft import PeftModel
import os

class GhibliImageGenerator:
    def __init__(self):
        self.model_id = "segmind/tiny-sd"
        self.lora_path = "./data/ghibli_model"
        self.device = "cpu"
        self.pipe = self._load_pipeline()

    def _load_pipeline(self):

        pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.float32,
            device_map=None,
            low_cpu_mem_usage=False
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
