#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread

"""
Условие задачи:
    * потребитель: звонок на горячую линию по вопросу ком. услуг
    * производитель: оператор, принимающий звонки 
"""


def consumer():
    lock.acquire()
    ls = []
    while not q.empty():
        s = q.get()
        r = random.choice(["вопрос остался открыт", "вопрос решен", "гудок идет"])
        print(f"звонок №: {s[1]} столкнулся с проблемой: {s[0]}, Результат: {r}")
        ls.append(
            {
                "№": s[1],
                "Проблема": s[0],
                "Результат": r
            }
        )
    for i in ls:
        if i["Результат"] == "вопрос остался открыт":
            print(f"звонок № {i['№']} ожидает оператора")
    lock.release()


def producer(ls):
    lock.acquire()
    ls = ls
    i = 0
    while i <= 6:
        idx = random.randint(0, 3)
        exp = random.randint(1, 1000)
        q.put([ls[idx], exp])
        i += 1
    lock.release()


if __name__ == "__main__":
    ls = ['проблема с отправкой показаний', 'не проходит оплата', 'сломался счетчик', 'нет света/газа/воды']
    lock = Lock()
    q = Queue()
    q2 = Queue()
    th1 = Thread(target=producer(ls)).start()
    th2 = Thread(target=consumer()).start()
