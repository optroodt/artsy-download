import argparse
import pathlib

import urlobject
import requests
from PIL import Image

BLOCK_SIZE = 512


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, type=str)
    return parser.parse_args()


def download(url):
    image_bytes = io.BytesIO()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=8192):
            image_bytes.write(chunk)

    return image_bytes


def stitch(url):
    url_obj = urlobject.URLObject(url)
    base_url = url_obj.root
    for segment in url_obj.path.segments[:-1]:
        base_url = base_url.add_path_segment(segment)
    x, rest = url_obj.path.segments[-1].split("_")
    y, rest = rest.split(".")
    x = int(x)
    y = int(y)

    # test_img = Image.open(f"{w-1}_{h-1}.jpg")
    test_img = Image.open(download(url))

    max_width = x * BLOCK_SIZE + test_img.width
    max_height = y * BLOCK_SIZE + test_img.height

    destination = Image.new("RGB", (max_width, max_height))
    for j in range(x + 1):
        for i in range(y + 1):
            source_img = f"{j}_{i}.jpg"

            x_pos = j * BLOCK_SIZE
            y_pos = i * BLOCK_SIZE
            destination.paste(Image.open(source_img), (x_pos, y_pos))

    destination.save("output.jpg", quality=100)


if __name__ == "__main__":
    args = get_arguments()
    stitch(args.url)
