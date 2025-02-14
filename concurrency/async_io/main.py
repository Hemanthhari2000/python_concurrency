import asyncio

from . import hello_world_example_main, real_world_example_main


def main():
    asyncio.run(real_world_example_main())


if __name__ == "__main__":
    main()
