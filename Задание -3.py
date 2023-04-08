mounth = int(input())
mounth_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = dict(Зима=1, Весна=2, Лето=3, Осень=4)
if mounth == 12 or mounth == 1 or mounth == 2:
    print(mounth_list[0])
elif mounth == 3 or mounth == 4 or mounth == 5:
    print(mounth_list[1])
elif mounth == 6 or mounth == 7 or mounth == 8:
    print(mounth_list[2])
elif mounth == 9 or mounth == 10 or mounth == 11:
    print(mounth_list[3])
else:
    print('Такого месяца не существует')
