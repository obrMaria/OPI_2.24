from queue import Queue
from threading import Thread, Lock
import math

EPS = 1e-07
q = Queue()


def sum(x, q):
    n, summa, temp = 1, 1.0, 0
    while abs(summa - temp) > EPS:
        temp = summa
        summa += math.sin(n * x) / n
        n += 1
    with lock:
        q.put(summa)


def func_y(x, q):
    summa = q.get()
    rez = (math.pi - x) / 2

    print(f"Sum is {summa}")
    print(f"Check: {rez}")


if __name__ == '__main__':
    lock = Lock()
    x = math.pi / 3
    t1 = Thread(target=sum, args=(x, q))
    t2 = Thread(target=func_y, args=(x, q))
    t1.start()
    t2.start()
