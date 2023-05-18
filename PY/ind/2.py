from queue import Queue
from threading import Thread, Lock
import math

EPS = 1e-07
q = Queue()
lock = Lock()


def sum(x = math.pi / 3):
    lock.acquire()
    n, summa, temp = 1, 1.0, 0
    while abs(summa - temp) > EPS:
        temp = summa
        summa += math.sin(n*x)/n
        n += 1
        q.put(summa)
    lock.release()


def func_y(x):
    result = (math.pi - x) / 2
    print(result)


if __name__ == '__main__':
    t1 = Thread(target=sum).start()
    t2 = Thread(target=func_y(q.get())).start()


