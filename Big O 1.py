import time

def my_function(n):
    """Example function with O(n) time complexity."""
    result = 0
    for i in range(n):
        result += i
    return result

# measure the execution time for different values of n
for n in [1000, 10000, 100000]:
    start_time = time.time()
    result = my_function(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"n = {n}, result = {result}, time = {elapsed_time:.6f} seconds")