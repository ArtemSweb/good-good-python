"""Вводится натуральное число n (то есть, целое положительное). В цикле перебрать все целые числа в интервале [1; n] и сформировать список из чисел, кратных 3 и 5 одновременно. Вывести полученную последовательность чисел в виде строки через пробел, если значение n меньше 100. Иначе вывести на экран сообщение "слишком большое значение n" (без кавычек). Использовать в программе оператор else после цикла while."""


n = int(input())

if n<100:
    i = 1
    lst = []
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            lst.append(i)
        i += 1
    print(*lst)
else:
    print("слишком большое значение n")
