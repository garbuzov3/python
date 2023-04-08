# Первый вариант
spisok = [13, True, "False", 12.5, None, -4, False]


def typ():
    for i in range(len(spisok)):
        print(type(spisok[i]))


typ()
# Второй вариант
my_list = [13, True, "False", 12.5, None, "line", [1, 2, 4]]
for elm in my_list:
    print(type(elm))
