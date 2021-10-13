while 1:
    h = int(input("Enter h: "))
    if(2 < h <= 30):
        break

for i in range(h):
    for j in range(h - i - 1):
        print(" ", end = '')
    print("/", end = '')
    if i + 1 == round(h / 2):
        if h % 2 == 1:
            for j in range(i * 2):
                print("-", end = '')
        else:
            for j in range(i * 2):
                print("_", end = '')
    elif i + 1 == h:
        for j in range(i * 2):
            print("_", end = '')
    else:
        for j in range(i * 2):
            print(" ", end = '')
    print("\\")