def pow(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n - 1)
result = pow(2, 3)
print(result)