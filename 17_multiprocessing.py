from multiprocessing import  Process, Value, Array, Lock
import os
import time

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i', 0)
    print(f'Number at beginning is {shared_number.value}')

    for _ in range(os.cpu_count()):
        p = Process(target=add_100, args=(shared_number, lock))
        p.start()
        p.join()

    print(f'Number at end is {shared_number.value}')