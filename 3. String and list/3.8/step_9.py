"""
Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем, удалить последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False. Отобразить полученный список на экране командой:
print(*lst)
Реализовать программу без использования условного оператора.
"""

lst = list(map(int, input().split()))

lst[-1] = lst[-1] % 2 != 0
print(*lst)