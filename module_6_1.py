class Animal:
    alive = True          #живой
    fed = False           #накормленный
    def __init__(self, name):
        self.name = name
    def eat(a, food):
        if food.edible == True:
            print(f"{a.name} съел {food.name}")
            a.fed = True
        else:
            print(f"{a.name} не стал есть {food.name}")
            a.alive = False
class Plant:
    edible = False         #съедобность
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
