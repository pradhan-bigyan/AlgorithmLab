import time
import random
import sys
from mergesort import merge_sort
from quicksort import quick_sort

# Increase recursion limit to handle larger inputs for quick sort
sys.setrecursionlimit(10**6)

def benchmark_sort(sort_function, arr, *args):
    start_time = time.time()
    if args:
        sort_function(arr, *args)
    else:
        sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 20000, 23000]

    print("Benchmarking Merge Sort:")
    for size in sizes:
        arr = list(range(size, 0, -1))
        time_taken = benchmark_sort(merge_sort, arr[:], 0, len(arr) - 1)
        print(f"Merge sort on array of size {size}: {time_taken:.6f} seconds")

    print("\nBenchmarking Quick Sort:")
    for size in sizes:
        arr = list(range(size, 0, -1))
        time_taken = benchmark_sort(quick_sort, arr[:], 0, len(arr) - 1)
        print(f"Quick sort on array of size {size}: {time_taken:.6f} seconds")
