import time


def f0(n: int):
    if n <= 1:
        return n
    return f0(n - 1) + f0(n - 2)


def repeat():
    for i in range(1, 30):
        start_time = time.perf_counter()
        f0(i)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000
        print(f"f0 {i} executed in {elapsed_ms:.4f} ms")