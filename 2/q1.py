def body_edge(h, w):
    for i in range(w):
        print(" ", end="")
    print("+", end="")
    for i in range(2 * h + 1):
        print("-", end="")
    print("+")

def validate(h, b, w, t):
    if h < 1:
        return 0
    elif b < 2:
        return 0
    elif w < 1:
        return 0
    elif t < 2:
        return 0
    elif t > h + 2: # width of tail <= width of body i.e. 2t - 1 <= 2h + 3
        return 0
    else:
        return 1

while 1:
    h, b, w, t = map(int, input("Enter h, b, w, t: ").split(" ", 4))
    if validate(h, b, w, t):
        break
    print("Invalid input!")
    
# head
for i in range(h + w + 1):
    print(" ", end="")
print("|")

for i in range(h):
    for j in range(h + w - i):
        print(" ", end="")
    print("/", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print("\\")

# body and wings
body_edge(h, w)
for i in range(b):
    if i >= int(b / 2):
        for j in range(w):
            print("/", end="")
    else:
        for j in range(w):
            print(" ", end="")
    print("|", end="")
    for j in range(2 * h + 1):
        print(".", end="")
    print("|", end="")
    if i >= int(b / 2):
        for j in range(w):
            print("\\", end="")
    print("")
body_edge(h, w)

# tail
for i in range(int(t / 2), t):
    for j in range(w + h - i + 1): ###
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print("")
for i in range(t, 0, -1):
    for j in range(w + h - i + 2): ###
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print("")