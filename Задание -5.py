profit = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))
if profit > costs:
    print("Фирма работает плюс:", (profit / costs))
    workers = int(input("Введите количество сотрудников: "))
    print("Прибыль в расчете на одного сторудника сотавила", (profit / workers))
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
