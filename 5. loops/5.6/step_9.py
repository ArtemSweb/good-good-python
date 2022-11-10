"""
Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька
"""

n =int(input())

money_list = [64, 32, 16, 8, 4, 2, 1]

res_list = []

for elem in money_list:
    while n >= elem:
        n = n - elem
        res_list.append(elem)
        if elem > n:
            continue

print(*res_list)