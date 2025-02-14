import asyncio


async def say_hello():
    await asyncio.sleep(2)  # Simulate waiting for 2 seconds
    print("Hello, Async World!")


async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulate doing something else for 1 second
    print("Finished another task...")


async def hello_world_example_main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(say_hello(), do_something_else())


if __name__ == "__main__":
    asyncio.run(hello_world_example_main())
