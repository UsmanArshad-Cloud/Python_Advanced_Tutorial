import time
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        before = time.time()
        func(args)
        after = time.time()
        func_name = func.__name__
        print(f"{func_name} took {after-before} seconds")
    return wrapper

@decorator
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@decorator
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


numbers1 = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90]
numbers2 = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90]
insertion_sort(numbers1)
bubble_sort(numbers2)
print(numbers1)
print(numbers2)

