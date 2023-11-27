n = int(input("input n "))
if n <= 9:
        p = 1
        for i in range(1, n+1):
            if i == 1:
                print(p)
            else:
                p = p * 10 + i
                print(p)
else:
    print('Введите другое n')
