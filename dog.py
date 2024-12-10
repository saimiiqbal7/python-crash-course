class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):

        self.name = name
        self.age = age
    
    def sit(self):

        print(f"{self.name} is now sitting")
    
    def rollOver(self):

        print(f"{self.name} rolled over")


myDog = Dog("Willie", 3)
print(myDog.name)