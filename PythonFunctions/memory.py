import time


def main(args):
    start = time.time()

    number = args.get("number", 100000)

    result = []
    for i in range(number):
        result.append(i)

    end = time.time()
    t = end - start
    return {"time": t, "result": len(result)}

