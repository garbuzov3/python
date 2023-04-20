file = 'task- 2.txt'
with open(file, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        words = len(line.split())
        print(f'Строка {i + 1} {words} слов')
    print(f"Всего в файле {len(lines)} строки")
