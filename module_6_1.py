class Animal:

    def __init__(self, alive, fed, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Plant:

    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Predator(Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Flower(Plant):

    def __init__(self, name):
        super().__init__(name, False)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, True)

    wolf = Animal(True, False, 'Волк с Уолл-Стрит')
    hat = Animal(True, False, 'Хатико')
    color7 = Plant('Цветик семицветик', False)
    fancy_orange = Plant('Заводной апельсин', True)

    print(wolf.name)
    print(color7.name)
    print(wolf.alive)
    print(hat.fed)
    wolf.eat(color7)
    hat.eat(fancy_orange)
    print(wolf.alive)
    print(hat.fed)
