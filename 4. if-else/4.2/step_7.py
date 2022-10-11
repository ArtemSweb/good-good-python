
month, day = map(int, input().split())
monts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if day == 1:
    pday = monts[day-2]
    pmonth = month - 1
    fday = 2
    nmonth = month
elif day == monts[month-1]:
    pday = day-1
    pmonth = month
    fday = 1
    nmonth = month+1
else:
    pday = day-1
    pmonth = month
    fday = day+1
    nmonth = month
print(f"{str(pmonth).rjust(2, '0')}.{str(pday).rjust(2, '0')} {str(nmonth).rjust(2, '0')}.{str(fday).rjust(2, '0')}")