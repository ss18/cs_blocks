from helpers import measure_time_ms
from typing import List, Callable
import numpy as np


@measure_time_ms
def f0(array: List[int], start: int, end: int) -> int:
    if start < 0 or end > len(array) or start >= end:
        raise ValueError("Invalid start or end indices")
    subarray = array[start:end]
    if len(subarray) < 1:
        raise ValueError("Empty subarray")
    ret_value = subarray[0]
    for element in subarray[1:]:
        if element > ret_value:
            ret_value = element
    return ret_value

@measure_time_ms
def f1(array: List[int], start: int, end: int) -> int:
    total = 0
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            total += array[i] + array[j]
    return total

@measure_time_ms
def f2(array: List[int], start: int, end: int) -> None:
    for i in range(start, end):
        for j in range(start, end - (i - start) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def repeat(func: Callable[[List[int], int, int], None], times: int = 1, factor: int = 10) -> None:
    print("Creating data...")
    array = np.random.randint(1, 10**10, size=factor**times).tolist()
    for i in range(times):
        end = factor**i
        func(array, 0, end)