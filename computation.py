import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed {func.__name__} in {end_time - start_time:.4f}s")
        return result
    return wrapper

@timer_decorator
def heavy_computation():
    return sum(range(10**7))

heavy_computation()