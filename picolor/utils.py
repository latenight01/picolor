import cv2
import numpy as np
import validators
import requests


def img_from_url(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        arr = np.asarray(bytearray(response.content), dtype=np.uint8)
        return cv2.imdecode(arr, -1)
    except Exception as e:
        print("Failed to generate dominant color from URL", url, e)


def img_from_url_or_path(source: str):
    is_url = validators.url(source)
    img = None
    if is_url:
        img = img_from_url(source)
    else:
        img = cv2.imread(source)

    # Convert BGR to RGB
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def rgb_to_hex(rgb : tuple):
    return "#%02x%02x%02x" % rgb