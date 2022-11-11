"""
Вводится натуральное число N. Необходимо сгенерировать вложенный список с помощью list comprehension, размером N x N, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки
"""

n = int(input())

lst = [[elem for _ in range(n)] for elem in range(n)]

for row in lst:
    print(*row)