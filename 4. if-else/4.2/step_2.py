
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

lst = m.split('\n')
n = int(input())
if str(n) in lst[0]:
    print(lst[0])
elif str(n) in lst[1]:
    print(lst[1])
elif str(n) in lst[2]:
    print(lst[2])
elif str(n) in lst[3]:
    print(lst[3])
elif str(n) in lst[4]:
    print(lst[4])
else:
    print(lst[5])


