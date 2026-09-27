import threading
import time

results = [0, 0, 0, 0]


def calculate_sum(worker_id, start, end):
    print(f"Thread {worker_id} calculating from {start} to {end}")

    total = 0

    for number in range(start, end + 1):
        total += number

    results[worker_id - 1] = total

    print(f"Thread {worker_id} finished.")


start_time = time.perf_counter()

thread1 = threading.Thread(
    target=calculate_sum,
    args=(1, 1, 1_000_000)
)

thread2 = threading.Thread(
    target=calculate_sum,
    args=(2, 1_000_001, 2_000_000)
)

thread3 = threading.Thread(
    target=calculate_sum,
    args=(3, 2_000_001, 3_000_000)
)

thread4 = threading.Thread(
    target=calculate_sum,
    args=(4, 3_000_001, 4_000_000)
)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

total_sum = sum(results)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("\n=== RESULTS ===")
print("Individual Results:", results)
print("Total Sum:", total_sum)
print("Execution Time:", execution_time, "seconds")