from multithreading.manual_threading_example import manual_threading
from multithreading.real_world_example import real_world_example
from multithreading.synchronous_example import synchronous_example
from multithreading.thread_pool_executor_example import thread_pool_executor


def main():
    # synchronous_example()
    # manual_threading()
    thread_pool_executor()
    # real_world_example()


if __name__ == "__main__":
    main()
