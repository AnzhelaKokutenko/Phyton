class Cell:
    def __init__(self, quant):
        self.quant = int(quant)

    def __str__(self):
        return f'Количество клеток {self.quant}'

    def __add__(self, other):
        return f'Сумма клеток {self.quant + other.quant}'

    def __sub__(self, other):
        return f'Разница {self.quant - other.quant if (self.quant - other.quant) > 0 else print("Невозможно")}'

    def __mul__(self, other):
        return f'Умножние {int(self.quant * other.quant)}'

    def __truediv__(self, other):
        return f'Деление {round(self.quant // other.quant)}'

    def make_order(self, cells):
        line = ''
        for i in range(int(self.quant / cells)):
            line += f'{"*" * cells} \\n'
            line += f'{"*" * (self.quant % cells)}'
        return line

c_1 = Cell(24)
c_2 = Cell(10)
print(c_1)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 / c_2)
print(c_1 * c_2)
print(c_1.make_order(6))

