"""водятся два целых положительных числа n и m, причем, n < m. Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m]. Программу реализовать при помощи цикла while"""

n, m = map(int, input().split())

while n <= m:
    print(n**2, end=' ')
    n+=1

