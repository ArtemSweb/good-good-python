"""Вводится список в виде вещественных чисел в одну строку через пробел. С помощью цикла for необходимо найти наименьшее значение в этом списке. Полученный результат вывести на экран.  Реализовать программу без использования функции min, max и сортировки."""

lst = list(map(float, input().split()))

min_value = lst[0]

for elem in lst:
    if elem<min_value:
        min_value = elem

print(min_value)