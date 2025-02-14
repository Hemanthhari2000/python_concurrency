import os
import time
from concurrent.futures.process import ProcessPoolExecutor

from PIL import Image, ImageFilter

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(30))

    img.thumbnail(size)
    img_name = img_name.split("/")[-1]
    img.save(f"outputs/multiprocessing/{img_name}")
    print(f"{img_name} was processed...")


def real_world_example():
    base_image_path = "outputs/multithreading/"
    images = [
        f"{base_image_path}{img_path}"
        for img_path in os.listdir(base_image_path)
        if img_path.endswith(".jpg")
    ]

    t1 = time.perf_counter()
    # Using synchronous execution
    # Finished in 7.002350750030018 seconds
    # for img in images:
    #     process_image(img)

    # Using Multithreading
    # Finished in 2.906993707991205 seconds
    with ProcessPoolExecutor() as executor:
        executor.map(process_image, images)

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1} seconds")
