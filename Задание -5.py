from typing import List


def my_function():
    x = False
    sum_list = 0
    while not x:
        entered_list = input("Введите список чисел, для завершения нажмите 'q' : ").split()
        result = 0
        for num in range(len(entered_list)):
            if entered_list[num] == 'q':
                x = True
                break
            else:
                result += int(entered_list[num])
        sum_list = sum_list + result
        print("Сумма списка:", sum_list)


my_function()
