'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и 
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
обработку ситуации деления на ноль.
'''

try:
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель: "))
except ValueError:
    print("Вы ввели не число")


def devide(num1, num2):
    return num1 / num2


try:
    print(devide(num1, num2))
except NameError:
    print("Делимое и/или делитель не определено(-ы)")
except ZeroDivisionError:
    print("Делить на ноль - плохая идея!")

