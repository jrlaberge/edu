#!/usr/bin/env python3
import os
from glob import glob
from PIL import Image

def change_image(image):
    img = Image.open(image)
    img = img.convert('RGB')
    img = img.resize((600,400))
    img.save(image.replace('tiff', 'jpeg'), 'JPEG', quality=90)

def get_images(file_path, ext):
    images = glob("{}*.{}".format(file_path, ext))
    return images

if __name__ == '__main__':
    images = get_images('./supplier-data/images/', 'tiff')
    for image in images:
        change_image(image)
