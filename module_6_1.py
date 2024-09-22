class  Animal():                    #Животное
    alive = True                    #(живой)
    fed = False                     #(накормленный)
    def __init__(self, name):
        self.name = name            #индивидуальное название каждого животного.

    def eat(self):
        food = Plant()
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            fed = True
        if food.edible == False:
            print(f"{self.name}не стал есть {food.name}")
            alive = False



class Plant():                      #Растение
    edible = False                  #(съедобность)
    def __init__(self, name):
        self.name = name            #индивидуальное название каждого растения

class Mammal(Animal):               #Млекопитающее
    pass

class Predator(Animal):             #Хищник
    pass

class Flower(Plant):                #Цветок
    pass

class Fruit(Plant):                 #Фрукт
    edible = True
    pass


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