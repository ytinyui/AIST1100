while 1:
    h, b, w, t = map(int, input("Enter h, b, w, t: ").split(" ", 4))
    if h >= 1 and b >= 2 and w >= 1 and t >= 2 and t <= h + 2:
        break
    print("Invalid input!")

# head
print(' ' * (h + w + 1), '|', sep='')
for i in range(h):
    print(' ' * (h + w - i), '/', '*' * (2 * i + 1), '\\', sep='')

# body and wings
print(' ' * w, '+', '-' * (2 * h + 1), '+', sep='')
for i in range(b):
    if i >= int(b / 2):
        print('/' * w, '|', '.' * (2 * h + 1), '|', '\\' * w, sep='')
    else:
        print(' ' * w, '|', '.' * (2 * h + 1), '|', sep='')
print(' ' * w, '+', '-' * (2 * h + 1), '+', sep='')

# tail
for i in range(int(t / 2), t):
    print(' ' * (w + h - i + 1), '*' * (2 * i + 1), sep='')
for i in range(t, 0, -1):
    print(' ' * (w + h - i + 2), '*' * (2 * i - 1), sep='')
