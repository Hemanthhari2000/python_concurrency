import time
from threading import Thread

from common import do_something


def manual_threading():
    print("Running threading (manual) example")

    start_time = time.perf_counter()

    threads = []
    for _ in range(5):
        t = Thread(target=do_something, args=(1,))  # Create a new Thread
        t.start()  # Start the created Thread
        threads.append(t)  # Add the thread to threads list

    for thread in threads:
        thread.join()  # Call .join() to wait for completing all the threads before moving to main thread

    # By the time the interpreter comes here, all the threads are executed and returns to main thread
    print(f"Execution took: {round(time.perf_counter() - start_time, 2)}")
