origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [x for x in origin_list if origin_list.count(x) == 1]
print(result_list)
