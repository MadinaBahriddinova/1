class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} the {self.species} is eating."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken")
    
    def lay_egg(self):
        return f"{self.name} laid an egg."

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Horse")
    
    def run(self):
        return f"{self.name} is running in the field."

# Example Usage
cow = Cow("Bessie")
print(cow.eat())
print(cow.produce_milk())

chicken = Chicken("Clucky")
print(chicken.sleep())
print(chicken.lay_egg())

horse = Horse("Thunder")
print(horse.run())
