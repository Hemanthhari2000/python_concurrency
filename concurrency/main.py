from concurrency.async_io.main import main as hello_world_example_main
from concurrency.multi_processing.main import main as multiprocessing_example
from concurrency.multithreading.main import main as multithreading_example


def main():
    # multithreading_example()
    # multiprocessing_example()
    hello_world_example_main()


if __name__ == "__main__":
    main()
