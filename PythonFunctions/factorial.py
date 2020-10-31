import time


def main(args):
    start = time.time()

    n = args.get("number", 1)

    r = 1
    for i in range(1, n + 1):
        r *= i

    end = time.time()
    t = end - start
    return {"time": t}
