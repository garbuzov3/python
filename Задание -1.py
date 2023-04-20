file = input('Имя файла: ')
f = open(file, 'w')
while True:
    line = input('Введите строку: ')
    if line == '':
        break
    f.write(line + '\n')
f.close()

