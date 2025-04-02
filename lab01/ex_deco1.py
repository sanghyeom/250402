# {func.__name__}

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time= time.time()
        result = func(*args, **kwargs)
        end_time= time.time()
        print(f"실행 시간: {end_time-start_time:.10f}초")
        return result
    return wrapper
'''
# 특정함수에 적용
def some_function:
...
decorated = timing_decorator(some_function)
# 또는
@timing_decorator
def some_function:
...'
'''
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n+1):
        yield a
        a, b = b , a+b
        # print(f"a:{a} b:{b}")

def fibonacci_dp(n):
    if n == 0:
        return[0]
    fib = [0] *(n+1)

    fib[0]=0
    fib[1]=1

    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]

    return fib

def fibonacci_deco(n):
    return [_ for _ in fibonacci(n)]

fibonacci_dp = timing_decorator(fibonacci_dp)
fibonacci_dp(4000)
fibonacci_deco= timing_decorator(fibonacci_deco)
fibonacci_deco(4000)       