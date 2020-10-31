from threading import Thread
import invoke
from random import randint
from time import sleep
import numpy as np


users = ["user1", "user2", "user3", "user4", "user5"]

actions = ["prime128", "factorial128", "fib128", "matrix128", "delay128", "memory128",
           "prime128php", "factorial128php", "fib128php", "matrix128php", "delay128php", "memory128php",
           "prime256", "factorial256", "fib256", "matrix256", "delay256", "memory256",
           "prime256php", "factorial256php", "fib256php", "matrix256php", "delay256php", "memory256php",
           "prime512", "factorial512", "fib512", "matrix512", "delay512", "memory512",
           "prime512php", "factorial512php", "fib512php", "matrix512php", "delay512php", "memory512php"]


def input_argument(name, size):
    if "fib" in name:
        if size == "small":
            return '{"number" : ' + repr(randint(20, 25)) + '}'
        if size == "medium":
            return '{"number" : ' + repr(randint(36, 38)) + '}'
        if size == "large":
            return '{"number" : ' + repr(randint(40, 41)) + '}'

    if "factorial" in name:
        if size == "small":
            return '{"number" : ' + repr(100) + '}'
        if size == "medium":
            return '{"number" : ' + repr(250000) + '}'
        if size == "large":
            return '{"number" : ' + repr(300000) + '}'

    if "prime" in name:
        if size == "small":
            return '{"number" : ' + repr(100) + '}'
        if size == "medium":
            return '{"number" : ' + repr(6500) + '}'
        if size == "large":
            return '{"number" : ' + repr(10000) + '}'

    if "matrix" in name:
        if size == "small":
            return '{"size" : ' + repr(50) + '}'
        if size == "medium":
            return '{"size" : ' + repr(500) + '}'
        if size == "large":
            return '{"size" : ' + repr(600) + '}'

    if "memory" in name:
        if size == "small":
            return '{"number" : ' + repr(1000) + '}'
        if size == "medium":
            return '{"number" : ' + repr(10000000) + '}'
        if size == "large":
            return '{"number" : ' + repr(90000000) + '}'

    if "delay" in name:
        if size == "small":
            return '{"number" : ' + repr(randint(1, 5)) + '}'
        if size == "medium":
            return '{"number" : ' + repr(randint(40, 50)) + '}'
        if size == "large":
            return '{"number" : ' + repr(randint(90, 100)) + '}'


def get_size():
    size = ["small", "medium", "large"]
    return size[randint(0, len(size) - 1)]


def invocations(interval, numbers):
    threads = []

    for i in range(numbers):
        user = users[randint(0, len(users) - 1)]
        action = actions[randint(0, len(actions) - 1)]
        data = input_argument(action, get_size())

        t = Thread(target=invoke.invoker, args=[i, user, action, data])
        threads.append(t)
        t.start()
        sleep(np.random.exponential(scale=interval, size=None))

    for t in threads:
        t.join()

