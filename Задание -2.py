class ZeroDivisionException(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        if b == 0:
            raise ZeroDivisionException("На ноль делить нельзя!")
        else:
            print(a / b)
            break
    except ZeroDivisionException as e:
        print(e)
    except:
        print("Ошибка!")
