from functools import reduce

event_list = [x for x in range(100, 1000, 2)]
product = reduce((lambda x, y: x * y), event_list)
print(product)
