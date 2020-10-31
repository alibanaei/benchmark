import time


def main(args):
    start = time.time()
    delay = args.get("number", 10)

    finished = False
    timer_start = time.time()
    timing = 0
    while not finished:
        timer_finished = time.time()
        var = 0
        for i in range(0, 100):
            var += 1
        if timer_finished - timer_start > delay:
            timing = timer_finished - timer_start
            finished = True

    end = time.time()
    t = end - start
    return {"time": t, "result": timing}
