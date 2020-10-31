import time


def get_nth_prime_number(n):
    num = 2
    for count in range(0, n):
        num = get_next_prime_number(num)

    return num


def get_next_prime_number(n):
    for i in range(n+1, n * n):
        if is_prime(i):
            return i
    return 0


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main(args):
    start = time.time()

    num = args.get("number", 0)
    result = get_nth_prime_number(num)

    end = time.time()
    t = end - start
    return {"time": t, "result": result}
