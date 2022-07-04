# NB: processes are in the same mem space, so they don't have access to the same mem dat
import time
from multiprocessing import Process, Value, Array
import time


# define our function
def add_100(number):
    for i in range(100):
        time.sleep(0.1)
        number.value += 1


if __name__ == '__main__':
    # single shared value
    shared_number = Value('i', 0)
    print('Number at the beginning is ', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,))
    p2 = Process(target=add_100, args=(shared_number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is ', shared_number.value)  # the value keeps changing since there is race condition
    # race condition is whereby processes compete to perform an operation on the same variable at the same time so
    # some operation from executing


