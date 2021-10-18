import string
import random


def random_grid(m, n, unique=False):
    if unique == True and m * n > 52:

    result = []
    for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(random.choice(string.ascii_letters))
    return result


print(random_grid(3, 4))
