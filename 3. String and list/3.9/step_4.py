"""
Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.
"""

lst = [list(map(int, input().split())) for _ in range(3)]

print(lst[0][-1], lst[1][-1], lst[2][-1])