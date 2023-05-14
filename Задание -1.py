class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def str_to_ints(cls, date):
        day, mouth, year = map(int, date.split('-'))
        return day, mouth, year

    @staticmethod
    def validate(day, mouth, year):
        if 1 <= mouth <= 12:
            return True
        else:
            return False


date = "12-11-2020"

d = Data(date)
day, mouth, year = d.str_to_ints(date)
print(day, mouth, year)

result = d.validate(day, mouth, year)
print(result)

date = "30-13-2020"
day, mouth, year = d.str_to_ints(date)
result = d.validate(day, mouth, year)
print(result)
