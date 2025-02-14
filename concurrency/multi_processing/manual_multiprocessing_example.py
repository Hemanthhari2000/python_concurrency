import time
from multiprocessing import Process

from common import do_something


def manual_multiprocessing_example():
    print("Running multiprocessing (manual) example")

    start_time = time.perf_counter()

    processes = []
    for _ in range(5):
        p = Process(target=do_something, args=[1.5])  # Create a new Process
        p.start()  # Start the created Process
        processes.append(p)  # Add the process to process list

    for process in processes:
        process.join()  # Call .join() to wait for completing all the processes before moving to main process

    # By the time the interpreter comes here, all the processes are executed and returns to main process
    print(f"Execution took: {round(time.perf_counter() - start_time, 2)}")
