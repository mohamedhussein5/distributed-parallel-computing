
import multiprocessing
import time
import heapq


# Part 1: Parallel Matrix Multiplication

def multiply_row(args):
    row, matrix_b = args
    result = []

    for column in zip(*matrix_b):
        value = sum(
            row[i] * column[i]
            for i in range(len(row))
        )
        result.append(value)

    return result


def sequential_matrix_multiplication(matrix_a, matrix_b):
    return [
        multiply_row((row, matrix_b))
        for row in matrix_a
    ]


def parallel_matrix_multiplication(matrix_a, matrix_b):
    tasks = [(row, matrix_b) for row in matrix_a]

    with multiprocessing.Pool(processes=2) as pool:
        return pool.map(multiply_row, tasks)


def run_matrix_multiplication():
    print("\n=== Matrix Multiplication ===")

    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [2, 3, 4]
    ]

    matrix_b = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    start = time.perf_counter()
    sequential_result = sequential_matrix_multiplication(
        matrix_a, matrix_b
    )
    sequential_time = time.perf_counter() - start

    start = time.perf_counter()
    parallel_result = parallel_matrix_multiplication(
        matrix_a, matrix_b
    )
    parallel_time = time.perf_counter() - start

    print("Parallel matrix result:")
    for row in parallel_result:
        print(row)

    print("Results match:", sequential_result == parallel_result)
    print(f"Sequential time: {sequential_time:.6f} seconds")
    print(f"Parallel time:   {parallel_time:.6f} seconds")


# Part 2: Parallel Sorting

def split_into_chunks(numbers, number_of_chunks):
    chunk_size = (len(numbers) + number_of_chunks - 1) // number_of_chunks

    return [
        numbers[i:i + chunk_size]
        for i in range(0, len(numbers), chunk_size)
    ]


def parallel_sort(numbers):
    chunks = split_into_chunks(numbers, 2)

    with multiprocessing.Pool(processes=2) as pool:
        sorted_chunks = pool.map(sorted, chunks)

    return list(heapq.merge(*sorted_chunks))


def run_parallel_sorting():
    print("\n=== Parallel Sorting ===")

    numbers = [
        42, 7, 19, 3, 25, 11, 8, 31,
        15, 2, 28, 10, 5, 36, 1, 22
    ]

    start = time.perf_counter()
    sequential_result = sorted(numbers)
    sequential_time = time.perf_counter() - start

    start = time.perf_counter()
    parallel_result = parallel_sort(numbers)
    parallel_time = time.perf_counter() - start

    print("Original list:", numbers)
    print("Sorted list:  ", parallel_result)
    print("Results match:", sequential_result == parallel_result)
    print(f"Sequential time: {sequential_time:.6f} seconds")
    print(f"Parallel time:   {parallel_time:.6f} seconds")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    run_matrix_multiplication()
    run_parallel_sorting()

    print("\nAll parallel algorithm demonstrations completed.")
