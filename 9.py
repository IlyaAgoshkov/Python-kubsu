n = int(input('Введите число n: '))  # Вводим значение n

# Создаем пустой двумерный массив размером n x n
matrix = [[0] * n for _ in range(n)]

# Заполняем массив согласно правилам
for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)  # Записываем модуль разницы индексов

# Выводим массив на экран
for row in matrix:
    print(row)