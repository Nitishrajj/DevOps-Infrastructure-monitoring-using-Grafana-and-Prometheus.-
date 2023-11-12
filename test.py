import numpy as np
import time

def cpu_intensive_task():
    # Perform a CPU-intensive task
    result = 0
    for _ in range(10**7):
        result += np.random.rand()
    return result

def memory_intensive_task():
    # Allocate and fill a large array to consume memory
    large_array = np.random.rand(10000, 10000)
    return large_array

def main():
    try:
        while True:
            # Perform CPU-intensive task
            cpu_result = cpu_intensive_task()
            print(f"CPU Result: {cpu_result}")

            # Perform memory-intensive task
            memory_result = memory_intensive_task()
            print(f"Memory Result: {memory_result}")

            time.sleep(2)  # Sleep for 2 seconds before the next iteration

    except KeyboardInterrupt:
        print("\nExiting the script.")

if __name__ == "__main__":
    main()
