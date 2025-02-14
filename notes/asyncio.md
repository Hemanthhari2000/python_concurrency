# Asyncio

## Core concepts of Asyncio

- Event Loop
- Coroutines
- Futures
- Tasks

### Event Loop

- The central execution device provided by asyncio. It manages and distributes the execution of different tasks. It's responsible for handling events and scheduling asynchronous routines.

### Coroutines

- Asynchronous functions declared with `async def`. These functions can be paused and resumed at await points, allowing I/O operations to run in the background.

### Futures

- Objects that represent the result of work that has not yet been completed. They are returned from tasks scheduled by the event loop.

### Tasks

- Scheduled coroutines that are wrapped into a Future object by the event loop, allowing their execution.

## The `await` Reserve Keyword

- The `await` keyword in Python is an essential part of asynchronous programming, introduced in Python 3.5.
- It is used to pause the execution of an `async` function until an awaitable object (like coroutines, Tasks, Futures or I/O) completes, allowing other tasks to run in the meantime.
- The key feature enables efficient handling of I/O-bound and high-level structured network code.

## Understanding await

- **Context**: `await` can only be used inside `async` functions. Attempting to use it outside such a context results in a syntax error.
- **Purpose**: Its primary purpose is to yield control back to the event loop, suspending the execution of the enclosing coroutine until the awaited object is resolved. This non-blocking behavior is what makes asynchronous programming efficient, especially for I/O-bound tasks.
- **Awaitables**: The objects that can be used with `await` must be awaitable. The most common awaitables are coroutines declared with `async def`, but others include asyncio Tasks, Futures, or any object with an `__await__()` method.
