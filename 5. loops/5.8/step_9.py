"""
Вводятся два списка целых чисел одинаковой длины каждый с новой строки. С помощью list comprehension сформировать третий список, состоящий из суммы соответствующих пар чисел введенных списков. Результат вывести на экран в одну строку через пробел.
"""

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst = [elem + lst2[i] for i, elem in enumerate(lst1)]

print(*lst)