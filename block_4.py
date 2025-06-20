from typing import List, Set
import itertools
from helpers import measure_time_ms


@measure_time_ms
def f0(array: List[int]) -> Set[tuple[int]]:
    def _r(start: int):
        if start == len(array):
            result.add(tuple(array[:]))
            return
        for i in range(start, len(array)):
            array[start], array[i] = array[i], array[start]
            _r(start + 1)
            array[start], array[i] = array[i], array[start]

    result = set()
    _r(0)
    return result


@measure_time_ms
def f1(array: List[int]) -> Set[tuple[int]]:
    def _r(remain: List[int], current: List[int] ):
        if len(remain) == 0:
            result.add(tuple(current))
            return
        for i, e in enumerate(remain):
            new_current = current[:] + [e]
            _r(remain[:i] + remain[i+1:], new_current)

    result = set()
    _r(array[:], [])
    return result


@measure_time_ms
def f2(array: List[int]) -> Set[tuple[int]]:
    return set(itertools.permutations(array[:]))


def repeat():
    for i in range(1, 12):
        array = [0] * i
        for i in range(i):
            array[i] = i
        f1(array)
