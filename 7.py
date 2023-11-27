n = input("Введите числа, разделенные пробелами: ").split()
new_list = []

for i in n:
    if n.count(i) == 1:
        new_list.append(i)

print(new_list)
