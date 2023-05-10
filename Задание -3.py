class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        if self.num_cells - other.num_cells > 0:
            return Cell(self.num_cells - other.num_cells)
        else:
            print("Разность количества ячеек двух клеток меньше или равна нулю.")
            return None

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        return Cell(self.num_cells // other.num_cells)

    def make_order(self, cells_in_row):
        rows = self.num_cells // cells_in_row
        remainder = self.num_cells % cells_in_row
        result = ""
        for i in range(rows):
            result += "*" * cells_in_row + "\n"
        result += "*" * remainder
        return result

    def __str__(self):
        return f"Клетка с {self.num_cells} ячейками"


cell1 = Cell(7)
cell2 = Cell(12)

print(cell1.make_order(3))
print(cell2.make_order(5))
