# pyTask

[![Build Status](https://github.com/lucianoigit/pyTask/actions/workflows/ci.yml/badge.svg)](https://github.com/lucianoigit/pyTask/actions)
[![Documentation Status](https://readthedocs.org/projects/pytask/badge/?version=latest)]
[![MIT License](https://img.shields.io/github/license/lucianoigit/pyTask)](LICENSE)

`pyTask` is a lightweight library for running background tasks and offloading work to separate threads, making it easy to execute tasks asynchronously and improve the responsiveness of your applications. Designed with simplicity and flexibility in mind, `pyTask` is perfect for applications that need a straightforward solution for handling background tasks.

## Features

- **Simple Task Management**: Easily create, run, and manage background tasks.
- **Asynchronous Execution**: Offload tasks to a separate thread to keep your main application responsive.
- **Task Scheduling**: Schedule tasks to run at specified intervals or times.
- **Error Handling and Logging**: Capture errors and log task statuses.

## Installation

Install `pyTask` via pip:

```bash

```

Or, clone the repository and install dependencies

```bash
git clone https://github.com/lucianoigit/pyTask.git
cd pyTask
pip install -r requirements.txt
```

## Quick Start

```python
from pyTask import Task

def example_task(x, y):
    return x + y

def handle_result(result):
    print(f"Task completed with result: {result}")

# Run task with callback
task = Task(example_task, 5, 10, callback=handle_result)
task.start()

# Wait for the task to finish (optional)
result = task.wait()
print(f"Final result: {result}")


```

## Usage

```python
@Task.task_decorator
def multiply(a, b):
    return a * b

task = multiply(3, 7)
result = task.wait()
print(f"Multiplication result: {result}")



```
