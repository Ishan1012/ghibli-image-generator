import torch
from ghibli_image.services.pipeline_loader import load_pipeline

class GhibliImageGenerator:
    def __init__(self):
        self.model_id = "segmind/tiny-sd"
        self.lora_path = "Ishan1000/ghibli_lora"
        self.pipe = load_pipeline(self.model_id, self.lora_path)

    def generate(self, prompt: str):
        self.pipe.scheduler.set_timesteps(20)

        with torch.no_grad():
            image = self.pipe(
                prompt,
                num_inference_steps=20,
                guidance_scale=7.5,
                height=256,
                width=256
            ).images[0]

        return image