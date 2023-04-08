my_list = []
elem = 0
my_count = input('Введите размер списка: ')
for i in range(int(my_count)):
    my_list.append(int(input('Введите элемент: ')))
for k in range(int(len(my_list) / 2)):
    my_list[elem], my_list[elem + 1] = my_list[elem + 1], my_list[elem]
    elem += 2
print(my_list)
