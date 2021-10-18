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


def print_grid(grid):
    for i in range(len(grid)):
        if i == 0:
            print("[", end="")
        else:
            print(" ", end="")
        print("[", end="")
        for j in range(len(grid[i])):
            print("\'"+grid[i][j]+"\'", end="")
            if j < len(grid[i]) - 1:
                print(", ", end="")
        print("]", end="")
        if i == len(grid) - 1:
            print("]")
        else:
            print(",")


def sorted_grid(grid, row_wise=True):

    # grid = [['p', 'O', 'v', 'U'], ['f', 'V', 'Y', 'k'], ['F', 'b', 'U', 'k']]
    # print_grid(grid)
    # print(random_grid(7, 7, True))
