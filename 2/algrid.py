import string
import random


def random_grid(m, n, unique=False):
    if unique == True and m * n > 52:
        print("The grid is too big for having unique items!")
        return

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
        print('[[' if i == 0 else ' [', end='')
        for j in range(len(grid[0])):
            print("\'" + grid[i][j] + "\'", end="")
            print(", " if j < len(grid[i]) - 1 else '', end='')
        print(']]' if i == len(grid) - 1 else '],')


def sorted_grid(grid, row_wise=True):
    l = []
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            l.append(grid[i][j])
    l.sort(key=lambda v: (v.lower(), v[0].isupper()))

    count = 0
    for i in range(len(grid)):
        result.append([])
        for j in range(len(grid[0])):
            result[i].append(l[count])
            count += 1

    if not row_wise:
        result = [list(x) for x in zip(*result)]
    return result


def save(grid, txt: str):
    f = open(txt, 'w')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            f.write(grid[i][j])
            f.write('\n') if j == len(grid[0]) - 1 else f.write(' ')


def restore(txt: str):
    grid = [[]]
    i = 0
    with open(txt, 'r') as f:
        x = f.readline(1)
        while x != '':
            if x == '\n':
                i += 1
                grid.append([])
            elif x != ' ':
                grid[i].append(x)
            x = f.readline(1)
    grid.pop()
    return grid


if __name__ == '__main__':
    A = [['A', 'f', 'q'],
         ['e', 'i', 't'],
         ['e', 'I', 'W'],
         ['f', 'I', 'y']]
    # save(sorted_grid(random_grid(6, 7, True), False), 'test1.txt')
    print_grid(restore('test1.txt'))
