#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread


def consumer(lock):
    ls = []
    while not q.empty():
        with lock:
            s = q.get()
            r = random.choice(["вопрос остался открыт", "вопрос решен", "гудок идет"])
            ls.append(
                {
                    "№": s[1],
                    "Проблема": s[0],
                    "Результат": r
                }
            )
        print(f"звонок №: {s[1]} столкнулся с проблемой: {s[0]}, Результат: {r}")

    with lock:
        for i in ls:
            if i["Результат"] == "вопрос остался открыт":
                print(f"звонок № {i['№']} ожидает оператора")


def producer(lock):
    i = 1
    while i <= 6:
        idx = random.randint(0, 3)
        exp = random.randint(1, 1000)
        with lock:
            q.put([ls[idx], exp])
        i += 1


if __name__ == "__main__":
    ls = ['проблема с отправкой показаний', 'не проходит оплата', 'сломался счетчик', 'нет света/газа/воды']

    lock = Lock()
    q = Queue()

    th1 = Thread(target=producer, args=(lock,))
    th2 = Thread(target=consumer, args=(lock,))
    th1.start()
    th2.start()
