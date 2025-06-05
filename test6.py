# linear_search
from memory_profiler import profile 
import random

@profile
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(tange(1, 10000001))
target = 10000000

linear_search(arr, target)

