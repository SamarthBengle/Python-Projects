from PIL import Image, ImageEnhance, ImageFilter
import os

image_path = "./images"
exported_image = "./Image-editor/export"

for filename in os.listdir(image_path):
    img = Image.open(f"{image_path}/{filename}")

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    edit = img.filter(ImageFilter.SHARPEN)

    factor = 2.0
    enhancer = ImageEnhance.Contrast(edit)
    enhancer = ImageEnhance.Color(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{exported_image}/{clean_name}_edited.jpg')