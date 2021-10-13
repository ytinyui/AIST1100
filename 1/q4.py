def combination(i, j, k):
    return i * 5 + j * 2 + k

n = int(input("Enter an integer amount between 1 and 100: "))
i = j = k = count = 0

while 1:
    while 1:
        while 1:
            if combination(i, j, k) == n:
                count += 1
                k = 0
                break
            k += 1
        if combination(i, j + 1, k) > n:
            j = 0
            break
        j += 1
    if combination(i + 1, j, k) > n:
        break
    i += 1
    
print(count, "ways")