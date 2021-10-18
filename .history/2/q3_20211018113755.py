import string
import random


def random_grid(m, n, unique=False):
    if unique == True and m * n > 52:
        print("The grid is too big for having unique items!")
        return None

    result = []
    occur = []
    for i in range(m):
        result.append([])
        for j in range(n):
            if unique:
                while 1:
                    tmp = random.choice(string.ascii_letters)
                    if tmp not in occur:
                        occur.append(tmp)
                        result[i].append(tmp)
                        break
            else:
                result[i].append(random.choice(string.ascii_letters))
    return result


print(random_grid(3, 4))
