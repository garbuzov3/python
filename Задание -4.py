def my_func(x, y):
    if x < 0 or y >= 0:
        print('Второе число должно быть целым-отрицательным')
    else:
        result = x ** y
    print(result)


x = float(input('Введите действительное число: '))
y = int(input('Введите целое отрицательное число: '))
my_func(x, y)
