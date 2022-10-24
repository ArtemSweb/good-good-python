"""На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел, до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue, а также использовать цикл while. Результат произведения вывести на экран."""

n = 1
total = 1

while n:
    n = int(input())
    if n <= 0:
        continue
    total *= n

print(total)