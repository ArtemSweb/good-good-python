"""
Вводится список вещественных чисел. С помощью list comprehension сформировать список, состоящий из элементов введенного списка, имеющих четные индексы (то есть, выбрать все элементы с четными индексами). Результат вывести на экран в одну строку через пробел
"""

lst = [float(elem) for i, elem in enumerate(input().split()) if i%2==0]

print(*lst)

