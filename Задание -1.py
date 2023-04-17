def calculate_salary(hours, rate, bonus):
    salary = hours * rate + bonus
    return salary


if __name__ == '__main__':
    hours = int(input('Введите число отработанных часов: '))
    rate = int(input('Введите ставку за час: '))
    bonus = int(input('Введите премию: '))
    salary = calculate_salary(hours, rate, bonus)
print(f'Зарплата сотрудника: {salary}')
