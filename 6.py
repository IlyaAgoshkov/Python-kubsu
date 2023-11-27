max1 = 0
max2 = 0
n = int
while n != 0:
    n = int(input())
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n

print(max2)