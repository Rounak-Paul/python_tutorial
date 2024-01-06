import functools
import time

@functools.lru_cache(maxsize=None) # add cache for the function
def factorial_with_delay(n:int) -> int:
    time.sleep(.01)
    if n == 0 or n == 1:
        return 1
    return n * factorial_with_delay(n-1)

t_start = time.time()
factorial_with_delay(100)  
print(f"Time taken: {time.time() - t_start}s") # 1.0375330448150635s

t_start = time.time()
factorial_with_delay(150)  
print(f"Time taken: {time.time() - t_start}s") # 0.0s