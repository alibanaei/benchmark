import time


def fib(n):
    if n < 2:
        return n

    return fib(n - 2) + fib(n - 1)


def main(args):
    start = time.time()

    number = args.get("number", 5)
    result = fib(number)

    end = time.time()
    t = end - start
    return {"time": t, "result": result}

