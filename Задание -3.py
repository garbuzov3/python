def my_function(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num2 < num1 < num3:
        return num1 + num3
    else:
        return num2 + num3


print(f' {my_function(float(input("Enter num1: ")), float(input("Enter num2: ")), float(input("Enter num3: ")))}')
