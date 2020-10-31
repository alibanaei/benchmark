import random
import time


def generate_matrix(size):
    matrix = [[random.randint(1, 999) for x in range(size)] for y in range(size)]
    return matrix


def multiply_matrices(m1, m2, size):
    result = [[0 for x in range(size)] for y in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            sum = 0
            for k in range(0, size):
                sum += m1[i][k] * m2[k][j]

            result[i][j] = sum
    return result


def main(args):
    start = time.time()

    size = args.get("size", 50)
    m1 = generate_matrix(size)
    m2 = generate_matrix(size)
    result = multiply_matrices(m1, m2, size)

    end = time.time()
    t = end - start
    return {"time": t, "result": len(result)}
