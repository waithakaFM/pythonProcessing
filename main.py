from multiprocessing import Process
import os


# define our function
def square_numbers():
    for i in range(1000):
        i * i


if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choise of the number for the processes

    # Create the processes and assign a function for each processes
    for i in range(num_processes):
        process = Process(target=square_numbers())
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait all the processes to finish
    # block the main program until these processes are finished
    for process in processes:
        process.join()