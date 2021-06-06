my_file = open('data.txt', 'r')

# for line in my_file.readlines():
#     print(line.replace('\n', ''))

# print(my_file.read(1024))

for data in my_file.read(1024):
    print(data)


# print(my_file.tell())

# my_file.seek(-1, 2)

# print(my_file.tell())

my_file.close()