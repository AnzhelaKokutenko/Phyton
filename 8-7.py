class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__ (self, other):
        return f'Сумма комплексных чисел равна = {self.a+other.a}+{self.b+other.b}*i'
    def __mul__(self,other):
        return f'Произведение комплексных чисел равно: {self.a * other.a - self.b * other.b}+{self.a * other.b+self.b*other.a}*i'

x = ComplexNumber(2,6)
y = ComplexNumber(5,4)
print(x+y)
print(x*y)