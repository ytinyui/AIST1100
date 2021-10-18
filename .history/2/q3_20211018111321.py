import string
import random

for i in range(10):
    print(random.choice(string.ascii_letters))


def random_grid(m, n, unique):
    result = []
