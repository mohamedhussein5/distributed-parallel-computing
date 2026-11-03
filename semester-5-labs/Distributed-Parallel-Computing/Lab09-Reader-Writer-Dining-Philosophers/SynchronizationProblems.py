
import threading
import time


# Part 1: Reader-Writer Problem

read_count = 0
read_count_lock = threading.Lock()
resource_lock = threading.Lock()

shared_data = "Initial Data"


def reader(reader_id):
    global read_count

    with read_count_lock:
        read_count += 1

        if read_count == 1:
            resource_lock.acquire()

    print(f"Reader {reader_id} is reading: {shared_data}")
    time.sleep(0.5)

    with read_count_lock:
        read_count -= 1

        if read_count == 0:
            resource_lock.release()

    print(f"Reader {reader_id} finished reading.")


def writer(writer_id):
    global shared_data

    with resource_lock:
        print(f"Writer {writer_id} is writing...")
        shared_data = f"Updated Data by Writer {writer_id}"
        time.sleep(0.5)
        print(f"Writer {writer_id} finished writing.")


def run_reader_writer():
    print("\n=== Reader-Writer Problem ===")

    threads = [
        threading.Thread(target=reader, args=(1,)),
        threading.Thread(target=reader, args=(2,)),
        threading.Thread(target=writer, args=(1,)),
        threading.Thread(target=reader, args=(3,))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Reader-Writer demonstration completed.")


# Part 2: Dining Philosophers Problem

NUMBER_OF_PHILOSOPHERS = 5

forks = [
    threading.Lock()
    for _ in range(NUMBER_OF_PHILOSOPHERS)
]

# Allow at most four philosophers to compete for forks at once.
# This prevents circular waiting among all five philosophers.
waiter = threading.Semaphore(NUMBER_OF_PHILOSOPHERS - 1)


def philosopher(philosopher_id):
    left_fork = philosopher_id
    right_fork = (philosopher_id + 1) % NUMBER_OF_PHILOSOPHERS

    print(f"Philosopher {philosopher_id + 1} is thinking.")
    time.sleep(0.2)

    with waiter:
        with forks[left_fork]:
            with forks[right_fork]:
                print(
                    f"Philosopher {philosopher_id + 1} "
                    "is eating."
                )
                time.sleep(0.5)

    print(f"Philosopher {philosopher_id + 1} finished eating.")


def run_dining_philosophers():
    print("\n=== Dining Philosophers Problem ===")

    threads = [
        threading.Thread(target=philosopher, args=(i,))
        for i in range(NUMBER_OF_PHILOSOPHERS)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Dining Philosophers demonstration completed.")


if __name__ == "__main__":
    run_reader_writer()
    run_dining_philosophers()
    print("\nAll synchronization demonstrations completed.")
