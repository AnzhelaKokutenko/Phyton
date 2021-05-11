obj = input('введите данные:').split()
with open('test.txt', "w", encoding='utf-8') as f:
    for el in obj:
        f.write(el + '\n')


