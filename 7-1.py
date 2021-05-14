class Matrix:
    def __init__(self, my_list):
        self.l = my_list

    def __str__(self):
        return '\n'.join(map(str, self.l))

    def __add__(self, other):
        for i in range(len(self.l)):
            for j in range(len(other.l[i])):
                self.l[i][j] = self.l[i][j] + other.l[i][j]
        return Matrix.__str__(self)


a = Matrix([[3,5,8,3],[8,3,7,1]])
b = Matrix([[4,1,2,3],[0,1,6,7]])

print(a+b)