# to prevent race condition we use lock --> prevent another process from accessing the same variable at the same time
from multiprocessing import Process, Value, Array, Lock
import time


def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.1)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('d', [0.0, 1.50, 20.10, 110.0, 156.5])
    print('Array at the beginning is ', shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at end is ', shared_array[:])
