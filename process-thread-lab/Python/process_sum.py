import multiprocessing
import time


def calculate_sum(worker_id, start, end, queue):
    print(f"Process {worker_id} calculating from {start} to {end}")

    total = 0

    for number in range(start, end + 1):
        total += number

    queue.put((worker_id, total))

    print(f"Process {worker_id} finished.")


if __name__ == "__main__":

    start_time = time.perf_counter()

    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(
        target=calculate_sum,
        args=(1, 1, 1_000_000, queue)
    )

    process2 = multiprocessing.Process(
        target=calculate_sum,
        args=(2, 1_000_001, 2_000_000, queue)
    )

    process3 = multiprocessing.Process(
        target=calculate_sum,
        args=(3, 2_000_001, 3_000_000, queue)
    )

    process4 = multiprocessing.Process(
        target=calculate_sum,
        args=(4, 3_000_001, 4_000_000, queue)
    )

    processes = [process1, process2, process3, process4]

    for process in processes:
        process.start()

    results = [0, 0, 0, 0]

    for _ in processes:
        worker_id, result = queue.get()
        results[worker_id - 1] = result

    for process in processes:
        process.join()

    total_sum = sum(results)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("\n=== RESULTS ===")
    print("Individual Results:", results)
    print("Total Sum:", total_sum)
    print("Execution Time:", execution_time, "seconds")