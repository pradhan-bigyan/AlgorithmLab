import time
from linear_search import linear_search

def benchmark_linear_search(n):
    arr = list(range(1, n + 1))
    
    start_time = time.time()
    
    result = linear_search(arr, n)
    
    end_time = time.time()
    
    time_taken = end_time - start_time
    
    print(f"Linear search result for target {n}: {result}")
    print(f"Time taken to search in an array of size {n}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    sizes = [100, 300, 500, 700, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    for size in sizes:
        benchmark_linear_search(size)
