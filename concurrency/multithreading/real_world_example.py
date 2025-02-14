import time
from concurrent.futures import ThreadPoolExecutor

import requests
from common import get_image_urls


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    img_path = f"outputs/multithreading/{img_name}"
    with open(img_path, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")


def real_world_example():
    img_urls = get_image_urls()

    t1 = time.perf_counter()
    # Using synchronous execution
    # Finished in 4.440151624999999 seconds
    # for img_url in img_urls:
    #     download_image(img_url)

    # Using Multithreading
    # Finished in 2.5671004169998923 seconds
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1} seconds")
