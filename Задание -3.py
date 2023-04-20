with open('task-3.txt', 'r') as f:
    low_salary = []

    for line in f:
        line = line.strip()
        name, salary = line.split()
        salary = float(salary)
        low_salary.append((name, salary))
print('Сотрудники с окладом менее 20 тысяч:')
for name, salary in low_salary:
    if salary < 20000:
        print(name)
avg_salary = sum([salary for name, salary in low_salary]) / len(low_salary)
print(f'Средний доход всех сотрудников: {avg_salary}')
