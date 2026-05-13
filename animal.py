class Animal:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Dog(Animal):

    def eating(self):

        return f"{self.name} is eating"
    
    def sleeping(self):

        return f"{self.name} is sleeping"
    
class Cat(Animal):

    def speak(self):

        return f"{self.name} says Meow!"
    
    def sit(self):

        return f"{self.color} {self.age} years old {self.name} is sitting"
    
dog = Dog("Rexy", 3, "white")
cat = Cat("Garfield", 5, "gray")
print(dog.eating())
print(dog.sleeping())
print(cat.speak())
print(cat.sit())

        