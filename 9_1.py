def b_matrix(n):
    matrix = [[0] * n for _ in range(n)] # Создаем нулевую матрицу размером n x n
    num = 1 # Начальное значение для заполнения элементов

    for d in range(n):
        i, j = 0, d
        while j >= 0:
            matrix[i][j] = num
            num += 1
            i += 1
            j -= 1

    for d in range(1, n):
        i, j = d, n - 1
        while i < n:
            matrix[i][j] = num
            num += 1
            i += 1
            j -= 1

    return matrix

n = 5 # Размерность матрицы
result = b_matrix(n)
for row in result:
    print(row)
