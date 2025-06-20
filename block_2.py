import numpy as np
from typing import List
from helpers import measure_time_ms
import random
import bisect


@measure_time_ms(precision=4)
def f0(array: List[int], value: int) -> int:
    index, left, right = -1, 0, len(array) - 1
    while left < right:

        if right - left == 1:
            if array[right] == value:
                index = right
            elif array[left] == value:
                index = left
            break

        c = (right + left) // 2
        if array[c] == value:
            index = c
            break
        elif array[c] > value:
            right = c
        else:
            left = c

    return index


@measure_time_ms(precision=6)
def f1(array: List[int], value: int) -> int:
    return bisect.bisect_left(array, value)


@measure_time_ms(precision=6)
def f2(array: List[int], value: int) -> int:
    for i, e in enumerate(array):
        if e == value:
            return i
    return -1


def repeat(times: int = 1, factor: int = 10, low=1, high=10**15) -> None:
    for i in range(1, times + 1):
        size = factor ** i
        array = np.sort(np.random.randint(low, high, size=size))
        rand_int = random.randint(1, size)
        f2(array, rand_int)
        # for _ in range(10):
        #     rand_int = random.randint(1, size)
        #     f0(array, rand_int)
