#!/usr/bin/env python3

import requests
from changeImage import get_images

def upload_image(image, url):
    with open(image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
if __name__ == '__main__':
    images = get_images('./supplier-data/images/', 'jpeg')
    for image in images:
        upload_image(image, 'http://localhost/upload/')
