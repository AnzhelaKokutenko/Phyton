dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_file = []
with open(r'U:\\test4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        my_file.append(dict[i[0]]+ i[1])
    print(my_file)

with open('new.txt', 'w',encoding='utf-8') as f_2:
    f_2.writelines(my_file)
