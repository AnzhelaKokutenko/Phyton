class Worker:
    def __init__(self,name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._i = {"зп": wage, "премия": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Имя сотрудника {self.n} {self.s}'
    def get_total_income(self):
        return f'Доход с учетом премии {sum(self._i.values())}'

per = Position('Jhon', 'Jhonov', 'HR', 50000, 50000)
print(per.get_full_name())
print(per.get_total_income())