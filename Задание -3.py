class OnlyIntegersAllowed(Exception):
    def __init__(self, text):
        self.text = text


nums = []
while True:
    try:
        user_input = input("Введите число или 'stop' для завершения: ")
        if user_input == "stop":
            break
        int(user_input)

        nums.append(int(user_input))

    except ValueError:
        raise OnlyIntegersAllowed("Только числа разрешены!")

print(nums)
