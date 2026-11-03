
import threading
import time


# Part 1: Mutex demonstration
counter = 0
counter_lock = threading.Lock()


def increment_counter():
    global counter

    for _ in range(10000):
        with counter_lock:
            counter += 1


def run_mutex_demo():
    global counter

    print("\n=== Mutex Demonstration ===")
    counter = 0

    threads = [
        threading.Thread(target=increment_counter)
        for _ in range(5)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Expected counter:", 50000)
    print("Actual counter:", counter)
    print("Mutex demonstration completed.")


# Part 2: Semaphore demonstration
semaphore = threading.Semaphore(2)
active_tasks = 0
active_lock = threading.Lock()


def limited_task(task_id):
    global active_tasks

    with semaphore:
        with active_lock:
            active_tasks += 1
            current_active = active_tasks

        print(
            f"Task {task_id} started. "
            f"Active tasks: {current_active}"
        )

        time.sleep(1)

        with active_lock:
            active_tasks -= 1

        print(f"Task {task_id} finished.")


def run_semaphore_demo():
    print("\n=== Semaphore Demonstration ===")

    threads = [
        threading.Thread(target=limited_task, args=(i,))
        for i in range(1, 6)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Semaphore demonstration completed.")


# Part 3: Deadlock demonstration with timeout recovery
lock_a = threading.Lock()
lock_b = threading.Lock()
ready = threading.Barrier(2)


def deadlock_worker(name, first_lock, second_lock):
    print(f"{name}: Acquiring first lock.")

    with first_lock:
        print(f"{name}: First lock acquired.")

        # Both threads hold one lock before requesting the other.
        ready.wait()

        print(f"{name}: Requesting second lock.")

        acquired = second_lock.acquire(timeout=2)

        if acquired:
            try:
                print(f"{name}: Second lock acquired.")
            finally:
                second_lock.release()
        else:
            print(
                f"{name}: Could not acquire second lock. "
                "Potential deadlock detected."
            )

    print(f"{name}: Released first lock.")


def run_deadlock_demo():
    print("\n=== Deadlock Demonstration ===")

    thread1 = threading.Thread(
        target=deadlock_worker,
        args=("Thread 1", lock_a, lock_b)
    )

    thread2 = threading.Thread(
        target=deadlock_worker,
        args=("Thread 2", lock_b, lock_a)
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Deadlock demonstration completed safely.")


if __name__ == "__main__":
    run_mutex_demo()
    run_semaphore_demo()
    run_deadlock_demo()

    print("\nAll synchronization demonstrations completed.")
