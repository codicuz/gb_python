'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print("Value error!")
    exit()


salary = lambda hours, rate, bonus: float(hours) * float(rate) + float(bonus)

print(f"Заработанная плата: {salary(hours, rate, bonus)}")

