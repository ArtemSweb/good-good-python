"""Вводится порядковый номер дня недели (1, 2, ..., 7). Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье). Программу реализовать с использованием операторов if-elif."""


day_of_week = int(input())

if day_of_week == 1:
    print('понедельник')
elif day_of_week == 2:
    print('вторник')
elif day_of_week == 3:
    print('среда')
elif day_of_week == 4:
    print('четверг')
elif day_of_week == 5:
    print('пятница')
elif day_of_week == 6:
    print('суббота')
elif day_of_week == 7:
    print('воскресенье')
else:
    print(f'Дня недели с номером {day_of_week} не существует')