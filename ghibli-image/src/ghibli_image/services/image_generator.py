import torch
from ghibli_image.services.pipeline_loader import load_pipeline

class GhibliImageGenerator:
    def __init__(self):
        self.pipe = load_pipeline()

    def generate(self, prompt: str):
        with torch.no_grad():
            image = self.pipe(
                prompt,
                num_inference_steps=30,
                guidance_scale=8.0,
                height=256,
                width=256
            ).images[0]

        return image