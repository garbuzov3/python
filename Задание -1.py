class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += '\t'.join(map(str, row)) + '\n'
        return result

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Матрицы имеют разные размеры')

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)


m1 = Matrix([[31, 32], [37, 43], [51, 86]])
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Матрица 3:")
print(m3)

print("Сумма матриц 1 и 2:")
print(m1 + m2)

try:
    m1 + m3
except ValueError as e:
    print("Ошибка:", str(e))
