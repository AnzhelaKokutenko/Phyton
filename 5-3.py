with open(r'U:\\test3.txt', 'r', encoding='utf-8') as my_file:
    oklad = []
    min_oklad = []
    my_list = my_file.readlines()
    for i in my_list:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
           min_oklad.append(i[0])
           oklad.append(i[1])
print(f'Оклад меньше 20.000 имеют {min_oklad}, средний оклад {sum(map(int, oklad)) / len(oklad)}')