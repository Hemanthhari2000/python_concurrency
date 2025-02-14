import time

from common import do_something


def synchronous_example():
    # Normal execution flow
    print("Running synchronous example")
    start_time = time.perf_counter()
    for _ in range(5):
        do_something(1)
    print(f"Execution took: {round(time.perf_counter() - start_time, 2)}")
