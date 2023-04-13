def calc(num_1, num_2):
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print('На ноль делить нельзя')


num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
calc(num_1, num_2)
