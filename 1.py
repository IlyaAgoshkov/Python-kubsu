n = int(input("Введите количество минут "))
hours = n // 60
minutes = n % 60
hours %= 24
print("Время на часах:", hours, "ч.", minutes, "м.")