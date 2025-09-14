import time
from functools import wraps


def measure_time_ms(func=None, *, precision=3):
    def decorator(inner_func):
        @wraps(inner_func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = inner_func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_ms = (end_time - start_time) * 1000
            if len(args) == 3:
                input_size = abs(args[1] - args[2])
            else:
                if type(args[0]) in (list, set, dict, str):
                    input_size = len(args[0])
                else:
                    input_size = args[0]
            print(f"'{inner_func.__name__}' executed in {elapsed_ms:.{precision}f} ms for input size {input_size}")
            return result
        return wrapper

    if func and callable(func):
        return decorator(func)
    else:
        return decorator

