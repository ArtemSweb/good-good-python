"""Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension, состоящий из делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел."""
n = int(input())

lst = [elem for elem in range(1, n+1) if n % elem == 0]

print(*lst)