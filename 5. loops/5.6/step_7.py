"""
водится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку выбором по возрастанию (неубыванию)
"""

lst = list(map(int, input().split()))

for i in range(len(lst)-1):
    small_index = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[small_index]:
            small_index = j

    lst[i], lst[small_index] = lst[small_index], lst[i]

print(*lst)
