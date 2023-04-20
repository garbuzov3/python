import json

with open('task-7.txt', 'r') as f:
    lines = f.readlines()
firms = []
total_profit = 0
for line in lines:
    name, form, revenue, expenses = line.split()
    profit = int(revenue) - int(expenses)
    firms.append({name: profit})
    if profit > 0:
        total_profit += profit
average_profit = total_profit / len(firms)
firms.append({'average_profit': average_profit})

with open('firms.json', 'w') as f:
    json.dump(firms, f)
