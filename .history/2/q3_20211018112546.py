import string
import random


def random_grid(m, n, unique):
    result = []
    for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(random.choice(string.ascii_letters))
    return result


print(random_grid(3, 1, 1))
