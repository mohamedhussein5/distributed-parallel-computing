
import threading
import time


def worker(task_name):
    for i in range(1, 6):
        print(f"{task_name}: Step {i}")
        time.sleep(0.5)

    print(f"{task_name} completed.")


def main():
    print("Python Threading Demonstration Started")

    thread1 = threading.Thread(
        target=worker, args=("Thread 1",)
    )
    thread2 = threading.Thread(
        target=worker, args=("Thread 2",)
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("All threads have finished.")


if __name__ == "__main__":
    main()
