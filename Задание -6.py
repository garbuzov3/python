import itertools

for num in itertools.count(3):
    if num > 10:
        break
    print(num)

list_test = [1, 2, 3, 4, 5]
for element in itertools.cycle(list_test):
    if element == 5:
        break
    print(element)
