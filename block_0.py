from helpers import measure_time_ms
import random
from typing import List, Callable, Set
import numpy as np


@measure_time_ms(precision=4)
def f0(array: List[int], start: int, end: int) -> int:
    random_index = random.randint(start, end)
    return array[random_index]

@measure_time_ms
def f1(collection: Set[int]) -> None:
    random_int = random.randint(0,10**10)
    collection.add(random_int)


def repeat_list(func: Callable[[List[int], int, int], None], times: int = 1, factor: int = 10) -> None:
    print("Creating data...")
    array = np.random.randint(1, 10**10, size=factor**times).tolist()
    for i in range(times):
        end = factor**i
        func(array, 0, end)

def repeat_set(func: Callable[[Set[int]], None], times: int = 1, factor: int = 10, low=1, high=10**12) -> None:
    for i in range(times):
        set_obj = set(np.random.randint(low, high, size=factor**i))
        func(set_obj)
