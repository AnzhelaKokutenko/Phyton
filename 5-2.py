f = open(r'U:\\test2.txt', 'r', encoding='utf-8')
b = f.readlines()
print(b)
print(f'Количество строк = {len(b)}')
for line in b:
    word = len(line.split())
print(f'Каждая строка содержит {word} слов')
f.close()




