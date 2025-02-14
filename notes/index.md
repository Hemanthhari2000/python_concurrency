# Concurrent in Python

## Fundamentals of concurrency

- Concurrency vs parallelism
- Programs
- Processes
- Threads
- How does the OS manage threads and processes?

### Concurrency vs Parallelism

**Concurrency**: Multiple tasks start, run, and complete in overlapping time periods but not necessarily simultaneously. Example: Handling multiple I/O-bound tasks like downloading files while processing user input.

**Parallelism**: Tasks run at the same time on multiple CPUs or cores. Example: Performing matrix multiplications across multiple CPU cores or image processing like cropping, resizing and augmenting.

### Programs

Static code; becomes a process when executed.

### Processes

Independent execution units with separate memory. Created using multiprocessing.

Processes can generally be categorised into two types:

#### I/O-bound processes

Spend most of it’s time waiting for input/output operations to complete, such as file access, network communication, or user input. While waiting, the CPU sits idle.

#### CPU-bound processes

Spend most of their time doing computations (e.g video encoding, numerical analysis). These tasks require a lot of CPU time.

### Threads

Lightweight execution units within a process, sharing memory. Created using threading

### How does the OS manage threads and processes?

**Processes**: OS schedules them independently with separate memory space.
**Threads**: OS schedules threads within a process using time-slicing (context switching).
**Thread scheduling**: The OS gives time to each thread using preemptive multitasking.
**Process scheduling**: The OS allocates CPU time and memory to processes based on priority and availability.

## Python’s concurrency models

- Multithreading
- Python’s Global Interpreter Lock (GIL)
- Multiprocessing
- Asyncio

### Multithreading (`threading` module)

**Best for**: I/O-bound tasks (network requests, file I/O, database queries).
**Why?** Threads share memory, reducing overhead. But Python’s GIL limits execution to one thread at a time for CPU-bound tasks.
**Real-world use case**: Handling multiple API requests concurrently, web scraping multiple pages at once.

### Python’s Global Interpreter Lock (GIL)

**What it does**: Ensures only one thread executes Python bytecode at a time, even on multicore CPUs.
**Effect**: Multithreading in Python is ineffective for CPU-bound tasks but useful for I/O-bound tasks.
**Workaround**: Use multiprocessing for CPU-bound workloads instead.

### Multiprocessing (`multiprocessing` module)

**Best for**: CPU-bound tasks (data processing, image processing, numerical computations).
**Why?** Each process has its own Python interpreter and memory, bypassing the GIL.
**Real-world use case**: Training deep learning models, video processing, large data transformations.

### Asyncio (`asyncio` module)

**Best for**: High-performance I/O-bound tasks (web scraping, async HTTP requests, socket programming).
**Why?** Uses an event loop instead of threads/processes, reducing overhead.
**Real-world use case**: Building high-performance web servers, concurrent database queries in a web app.
