import os
from PIL import Image


def check():
    images = os.listdir(os.getcwd())

    for image, num in enumerate(images):
        if image == "main.py":
            images.pop(num)
            break

    for image in images:
        if '.py' in image or '.jpg' in image: continue
        img = Image.open(image)
        img = img.resize((64, 64))
        img = img.convert("RGB")
        img.save(f"{image.split('.')[0]}.jpg", "jpeg")
        os.remove(image)