class Horse:  # класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
    def __init__(self,):
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr'  # звук, который издаёт лошадь
        super().__init__()

    def run(self, dx):
        self.x_distance += dx  # изменение дистанции, увеличивает x_distance на dx.


class Eagle:  # класс описывающий орла. Объект этого класса обладает следующими атрибутами:
    def __init__(self,):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy  # изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Horse, Eagle):  # класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    def __init__(self):  # Объект обладающий атрибутами классов родителей в порядке наследования.
        super().__init__()

    def move(self, dx, dy):  # изменения дистанции. В этом методе должны запускаться наследованные методы run и# fly
        self.run(dx)
        self.fly(dy)

    def get_pos(self):              #возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance)
        return self.x_distance, self.y_distance

    def voice(self):               # печатает значение унаследованного атрибута sound.
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
