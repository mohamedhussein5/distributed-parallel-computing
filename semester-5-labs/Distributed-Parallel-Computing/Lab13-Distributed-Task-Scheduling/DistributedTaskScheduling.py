
import multiprocessing
import os
import time


def execute_task(task):
    """Execute one task and return its result."""
    task_id, number = task

    print(
        f"Worker PID {os.getpid()} started Task {task_id}",
        flush=True
    )

    # Simulate a task that requires processing time
    time.sleep(1)

    result = number * number

    print(
        f"Worker PID {os.getpid()} completed Task {task_id}",
        flush=True
    )

    return {
        "task_id": task_id,
        "number": number,
        "result": result,
        "worker_pid": os.getpid()
    }


def main():
    tasks = [
        (1, 5),
        (2, 10),
        (3, 15),
        (4, 20),
        (5, 25),
        (6, 30)
    ]

    number_of_workers = 3

    print("=== Distributed Task Scheduling ===")
    print(f"Total tasks: {len(tasks)}")
    print(f"Worker processes: {number_of_workers}")

    start_time = time.perf_counter()

    with multiprocessing.Pool(
        processes=number_of_workers
    ) as pool:
        results = pool.map(execute_task, tasks)

    end_time = time.perf_counter()

    print("\n--- Task Results ---")

    for item in results:
        print(
            f"Task {item['task_id']}: "
            f"{item['number']} squared = {item['result']} "
            f"(Worker PID: {item['worker_pid']})"
        )

    print("\n--- Scheduling Summary ---")
    print(f"Tasks completed: {len(results)}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print("All tasks completed successfully.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()

