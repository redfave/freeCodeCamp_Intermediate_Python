from threading import Thread, Lock, current_thread
from queue import Queue
import os
import time
import random

num_threads = os.cpu_count() * 2
print('Lock based threading')
database_value = 0


def increase(lock):
    with lock:
        global database_value
        local_copy = database_value
        local_copy += 1
        time.sleep(random.uniform(0.1, 0.5))
        database_value = local_copy


if __name__ == '__main__':
    threads = []

    print(f'Start value: {database_value}')
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=increase, args=(lock,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'End lock based threading with value: {database_value}')

print('Threading queue')


def worker(q, lock):
    while True:
        value = q.get() # threadsafe
        with lock:
            print(f'Working in {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i) # threadsafe

    q.join()
    print(f'Threading queue finished')