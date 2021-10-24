import sys, os
sys.path.append(os.getcwd())

from imcolor import avg_color, kmeans_dominant_color



url = "https://cdn01.zoomit.ir/2021/10/covid-19-iran-216x144.jpg"
url = "https://cdn01.zoomit.ir/2021/10/new-14-inch-macbook-pro-top-copy-1200x800-216x144.jpg"

print(
    avg_color(url, hex_output=True),
    kmeans_dominant_color(url, hex_output=True),
)
