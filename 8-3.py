class Check(Exception):
    @staticmethod
    def func():
        my_list = []
        while True:
            try:
                el = input('Введите число в список, для выхода нажмите q:')
                if el == 'q':
                    break
                if not el.isdigit():
                    raise Check()
                my_list.append(int(el))
            except Check as ex:
                print('Неверный ввод!',ex)
                print(my_list)


print(Check.func())
