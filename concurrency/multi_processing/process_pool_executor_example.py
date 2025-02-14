import time
from concurrent.futures import ProcessPoolExecutor, as_completed

from common import do_something


def process_pool_executor_example():
    start_time = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, second) for second in seconds]
        for result in as_completed(results):
            print(result.result())

    print(f"Execution took: {round(time.perf_counter() - start_time, 2)}")
