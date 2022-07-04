# Pool object which offers a convenient means of parallelizing the execution of a function across multiple input
# values, distributing the input data across processes (data parallelism).


from multiprocessing import Pool
import time


def cube(number):
    return number * number * number


if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    # methods most commonly used: map, apply, join, close
    result = pool.map(cube, numbers) # allocate the pool, split the data and then add this method in parallel once
    # done it return the result

    # pool.apply(cube, numbers[0]) # this will execute a process in this function with one argument

    pool.close()
    pool.join()

    print(result)