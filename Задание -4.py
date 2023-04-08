num = 1
for word in input("Введите слова- ").split():
    if len(word) <= 10:
        print(f" {num} {word}")
        num += 1
    else:
        print(f" {num} {word[0:10]}")
        num += 1
