x = list(input('Введите значения списка без пробелов и запятых:'))
for i in range(0, len(x)-1, 2):
    x[i], x[i+ 1] = x[i + 1], x[i]
print(x)


