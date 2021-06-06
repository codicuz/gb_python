my_file = open('data.txt', 'w')

if my_file.writable():
    my_file.write("Update\n")

    strings = ["John\n", "Kate\n"]
    my_file.writelines(strings)
else:
    print("Can not writable")

my_file.close()