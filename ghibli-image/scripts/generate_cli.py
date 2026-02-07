from ghibli_image.services.image_generator import GhibliImageGenerator
from PIL import Image

def main():
    print("🎨 Ghibli Image Generator (CLI)")
    prompt = input("Enter prompt: ")

    generator = GhibliImageGenerator()
    image = generator.generate(prompt)

    output_path = "ghibli_output.png"
    image.save(output_path)

    print(f"✅ Image saved as {output_path}")

    try:
        image.show()
    except Exception:
        pass

if __name__ == "__main__":
    main()
