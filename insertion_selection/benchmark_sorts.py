import time
from insertionsort import insertion_sort
from selectionsort import selection_sort

def benchmark_sort(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [100, 300, 500, 700, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

    print("Benchmarking Insertion Sort:")
    for size in sizes:
        arr = list(range(size, 0, -1)) 
        time_taken = benchmark_sort(insertion_sort, arr)
        print(f"Insertion sort on array of size {size}: {time_taken:.6f} seconds")

    print("\nBenchmarking Selection Sort:")
    for size in sizes:
        arr = list(range(size, 0, -1))
        time_taken = benchmark_sort(selection_sort, arr)
        print(f"Selection sort on array of size {size}: {time_taken:.6f} seconds")
