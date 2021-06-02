list=input("Введите значения через запятую: ").split(',')
list2=[]


for i in list:
    list2.append(int(i))


for i in range(1, len(list2), 2):
    list[i - 1], list[i] = list[i], list[i - 1]


print(' '.join([str(i) for i in list]))