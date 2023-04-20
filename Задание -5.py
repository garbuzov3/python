with open("task-5.txt", 'w') as f:
    numbers = [1, 2, 3, 4, 5]
    f.write(' '.join(str(num) for num in numbers))
with open("task-5.txt", 'r') as f:
    data = f.read()
    sum_numbers = sum(int(num) for num in data.split())
print("Сумма чисел:", sum_numbers)
