"""Составить программу поиска всех трехзначных чисел, которые при делении на 47 дают в остатке 43 и кратны 3. Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while."""


n = 100

while n < 1000:
    if n % 47 == 43 and n % 3 == 0:
        print(n, end=' ')
    n += 1


