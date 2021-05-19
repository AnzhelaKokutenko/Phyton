class Data:
    @classmethod
    def my_method(cls, d_m_y):
        date = []
        for i in d_m_y.split():
            if i != '-':
                date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def check(d_m_y):
        d, m, y = d_m_y.split('-')
        if int(d) <= 31 and int(d) != 0 and int(m) <= 12 and int(m) != 0 and int(y) <= 2021:
            return 'есть такая дата'
        else:
            return 'такой даты нет'

print(Data.my_method('18 - 05 - 2021'))
print(Data.check('18 - 05 - 2021'))
print(Data.check('01 - 13 - 2021'))