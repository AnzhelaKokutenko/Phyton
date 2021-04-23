a = input('Введите строку: ')
b = a.split()
print(b)
for ind, el in enumerate(b, 1):
        if len(el) < 10:
         print(ind, el)
        if len(el) > 10:
            print(ind, el[:10])