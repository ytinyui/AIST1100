while 1:
    a = int(input("Enter a positive integer: "))
    if(a <= 0):
        print("Only positive integer is acceptable.")
    else:
        break

while 1:
    print(str(a) + ",", end = " ")
    if a % 2 == 0:
        a = int(a / 2)
    else:
        a = a * 3 + 1
    if a == 1:
        print(a)
        break