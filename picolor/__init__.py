import time
import cv2
import numpy as np
from picolor.utils import img_from_url_or_path, rgb_to_hex

# https://stackoverflow.com/a/43111221/12696223
def kmeans_dominant_color(
    path_or_url: str, hex_output: bool = False, default_color: str = (255, 255, 255)
):
    img = img_from_url_or_path(path_or_url)
    t1 = time.time()
    if img is not None:
        pixels = np.float32(img.reshape(-1, 3))
        n_colors = 5

        # (type , max_iter , epsilon : required accuracy)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 50)

        flags = cv2.KMEANS_RANDOM_CENTERS
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 2, flags)
        _, counts = np.unique(labels, return_counts=True)
        dominant = palette[np.argmax(counts)]

        rgb = tuple(dominant.astype(int))
        result = rgb
    else:
        rgb = default_color
    if hex_output:
        result = rgb_to_hex(rgb)

    t = round(time.time() - t1, 4)
    print(f"Dominant color {result} generated in", t, "sec")
    return result


# https://stackoverflow.com/a/43111221/12696223
def avg_color(
    path_or_url: str, hex_output: bool = False, default_color: str = (255, 255, 255)
):
    img = img_from_url_or_path(path_or_url)
    t1 = time.time()
    if img is not None:
        c = img.mean(axis=0).mean(axis=0)
        result = rgb = tuple(c.astype(int))
    else:
        rgb = default_color
    if hex_output:
        result = rgb_to_hex(rgb)

    t = round(time.time() - t1, 4)
    print(f"AVG color {result} generated in", t, "sec")
    return result