from time import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print(time() - start_time)
        return res
    return wrapper


def fib_cycle(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b

    return b


def fib_rec(n):
    if n == 1 or n == 0:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


@lru_cache(maxsize=None)
def fib_rec_cache(n):
    if n == 1 or n == 0:
        return 1
    return fib_rec_cache(n - 1) + fib_rec_cache(n - 2)


@time_decorator
def fib_cycle_measure(n):
    print(fib_cycle(n))


@time_decorator
def fib_rec_measure(n):
    print(fib_rec(n))


@time_decorator
def fib_cache_measure(n):
    print(fib_rec_cache(n))
