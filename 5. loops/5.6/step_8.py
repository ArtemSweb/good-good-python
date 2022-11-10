"""Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька."""

lst = list(map(int, input().split()))

for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j + 1] = lst[j+1], lst[j]

print(*lst)