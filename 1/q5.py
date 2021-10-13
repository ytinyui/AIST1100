def change(arr):
    global c
    for i in range(len(arr)):
        count = 0
        while c - arr[i][0] >= 0:
            c -= arr[i][0]
            count += 1
        if count > 0:
            if count > 1:
                output.append((count,arr[i][2]))
            else:
                output.append((count,arr[i][1]))

notes = ((10000, "$100", '$100\'s'), (5000, '$50', '50\'s'), (2000, '$20', '$20\'s'), (1000, '$10', '$10\'s'), (500, '$5', '$5\'s'), (100, '$1', '$1\'s'))
coins = ((25, 'quarter', 'quarters'), (10, 'dime', 'dimes'), (5, 'nickel', 'nickels'), (1, 'penny', 'pennies'))
output = []

a = float(input("Insert money ($): "))
b = float(input("Item price ($): "))
if a != round(a, 2) or b != round(b, 2):
    print("No change combination is found!")
else:
    c = round(a * 100 - b * 100)
    print("Change: $%s" % (c / 100))
    change(notes)
    change(coins)
    for i in range(len(output)):
        print(output[i][0],"x",output[i][1])
