import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import do_something


def thread_pool_executor():
    start_time = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(5)]
        for result in as_completed(results):
            print(result.result())

    print(f"Execution took: {round(time.perf_counter() - start_time, 2)}")
