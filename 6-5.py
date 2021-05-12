class Stationery:
  def __init__(self, title):
      self.t = title

      def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.t }')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.t }')
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.t }')

a = Pen('Шариковой')
b = Pencil('Черным')
c = Handle('Красным')

a.draw()
b.draw()
c.draw()