import requests
import uuid
import os

def generate_image(prompt: str):
    image_url = f"https://image.pollinations.ai/prompt/{prompt}"
    img_data = requests.get(image_url).content
    os.makedirs("generated_images", exist_ok = True)
    file_path = f"generated_images/{uuid.uuid4()}.png"
    with open(file_path, "wb") as f:
        f.write(img_data)

    return file_path
