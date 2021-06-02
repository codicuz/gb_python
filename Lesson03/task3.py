'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
list=[]

def my_func(arg1, arg2, arg3):
    list.append(arg1)
    list.append(arg2)
    list.append(arg3)
    list.sort(reverse=True)
    return list[0] + list[1]

print(f'Результат: {my_func(int(input("Введите первый агрумент: ")), int(input("введите второ аргумент: ")), int(input("Введите третий аргумент: ")))}') 
