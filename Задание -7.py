run = int(input("Введите километры за день: "))
wich_run = int(input("Сколько нужно пробежать: "))
days = 1
while run < wich_run:
        run = run + 0.1 * run
        days += 1
print("Hа", days, "день спортсмен достиг результата — не менее", wich_run, "км")
