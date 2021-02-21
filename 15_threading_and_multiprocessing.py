from multiprocessing import Process
import os
import time
from threading import Thread


def square_numbers(limit):
    for i in range(limit + 1):
        i ** 2
        time.sleep(0.1)


if __name__ == '__main__':
    start = time.time()
    square_limit = 100
    print('Processes')
    processes = []
    processes_limit = os.cpu_count()

    for _ in range(processes_limit):
        p = Process(target=square_numbers, args=(square_limit,))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    stop = time.time()
    print(f'End Main after {stop - start}')
    print('\n')

    print('Threads')
    start = time.time()
    threads = []
    threads_limit = os.cpu_count()

    for _ in range(threads_limit):
        t = Thread(target=square_numbers, args=(square_limit,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    stop = time.time()
    print(f'End Main after {stop - start}')
