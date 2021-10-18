import string
import random


def random_grid(m, n, unique=False):
    if unique == True and m * n > 52:
        print("The grid is too big for having unique items!")
  result = []
   for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(random.choice(string.ascii_letters))
    return result


print(random_grid(3, 4))
