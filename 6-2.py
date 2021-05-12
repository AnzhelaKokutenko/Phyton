class Road:
    def __init__(self, length, width):
       self._l = length
       self._w = width

    def my_method (self,massa,sm):
        self.m = massa
        self.sm = sm
        M = (self._l*self._w*self.m*self.sm)/1000
        return M

x = float(input('Введите длину: '))
y = float(input('Введите ширину: '))
a = Road(x, y)
print(a.my_method(25,5))