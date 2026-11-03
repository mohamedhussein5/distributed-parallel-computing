
import multiprocessing
import os
import time


def worker(task_name):
    process_id = os.getpid()

    print(f"{task_name} started. Process ID: {process_id}")

    for i in range(1, 6):
        print(f"{task_name}: Step {i}")
        time.sleep(0.5)

    print(f"{task_name} completed. Process ID: {process_id}")


def main():
    print("Python Multiprocessing Demonstration Started")

    process1 = multiprocessing.Process(
        target=worker,
        args=("Process 1",)
    )

    process2 = multiprocessing.Process(
        target=worker,
        args=("Process 2",)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes have finished.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
