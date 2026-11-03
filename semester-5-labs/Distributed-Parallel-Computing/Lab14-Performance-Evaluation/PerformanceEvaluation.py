
import multiprocessing
import time
import os


def calculate_square_sum(numbers):
    """Calculate the sum of squares for a portion of the numbers."""
    return sum(number * number for number in numbers)


def divide_into_chunks(numbers, number_of_chunks):
    """Divide numbers into approximately equal chunks."""
    chunk_size = (len(numbers) + number_of_chunks - 1) // number_of_chunks

    return [
        numbers[start:start + chunk_size]
        for start in range(0, len(numbers), chunk_size)
    ]


def sequential_calculation(numbers):
    start = time.perf_counter()
    result = calculate_square_sum(numbers)
    elapsed = time.perf_counter() - start

    return result, elapsed


def parallel_calculation(numbers, number_of_workers):
    chunks = divide_into_chunks(numbers, number_of_workers)

    start = time.perf_counter()

    with multiprocessing.Pool(
        processes=number_of_workers
    ) as pool:
        partial_results = pool.map(calculate_square_sum, chunks)

    result = sum(partial_results)
    elapsed = time.perf_counter() - start

    return result, elapsed


def main():
    # Use a sufficiently large workload for comparison.
    numbers = list(range(1, 1_000_001))
    number_of_workers = min(4, os.cpu_count() or 1)

    print("=== Performance Evaluation of Parallel Programs ===")
    print(f"Number of values: {len(numbers):,}")
    print(f"Worker processes: {number_of_workers}")

    sequential_result, sequential_time = sequential_calculation(numbers)

    parallel_result, parallel_time = parallel_calculation(
        numbers, number_of_workers
    )

    if parallel_time > 0:
        speedup = sequential_time / parallel_time
    else:
        speedup = 0

    efficiency = speedup / number_of_workers

    print("\n--- Results ---")
    print(f"Sequential result: {sequential_result}")
    print(f"Parallel result:   {parallel_result}")
    print(f"Results match:     {sequential_result == parallel_result}")

    print("\n--- Performance Metrics ---")
    print(f"Sequential time: {sequential_time:.6f} seconds")
    print(f"Parallel time:   {parallel_time:.6f} seconds")
    print(f"Speedup:         {speedup:.4f}")
    print(f"Efficiency:      {efficiency * 100:.2f}%")

    print("\n--- Conclusion ---")
    if parallel_time < sequential_time:
        print("Parallel execution was faster for this run.")
    elif parallel_time > sequential_time:
        print("Sequential execution was faster for this run.")
    else:
        print("Both execution times were equal for this run.")

    print("Performance evaluation completed.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
