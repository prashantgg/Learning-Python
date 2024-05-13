class Animal:
    animalType = "Mammal"

class Pets(Animal):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print ("The dog is barking!")


d = Dog()
d.bark()


