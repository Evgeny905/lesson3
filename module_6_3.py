class Horse:
    def __init__(self, x_distance = 0, y_distance = 0, sound = 'Frrr'):
        super().__init__(sound = 'I train, eat, sleep, and repeat')
        self.x_distance = x_distance
        self.y_distance = y_distance
        self.sound = sound
    def run(self, dx = 0):
        self.dx = dx
        self.x_distance = self.x_distance + self.dx
class Eagle:
    def __init__(self, x_distance = 0, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.x_distance = x_distance
        self.y_distance = y_distance
        self.sound = sound
    def fly(self, dy = 0):
        self.dy = dy
        self.y_distance = self.y_distance + self.dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__(sound = 'I train, eat, sleep, and repeat')
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.run(self.dx)
        self.fly(self.dy)
    def get_pos(self):
        Tuple = (self.x_distance, self.y_distance)
        return Tuple
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
