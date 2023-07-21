import random


class PlayerStats:
    def __init__(self):
        self.health = 100
        self.mana = 100
        self.strength = 1
        self.agility = 2
        self.intelligence = 2
        self.fortitude = 2
        self.recovery = 1
        self.age = random.randint(20,80)
        
    def __repr__(self):
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string[0:-1]
            


class ItemStats:
    def __init__(self):
        pass
    
    
class AnimalStats:

    def __init__(self):
        self.health = 100
        self.attack = 1
        self.defense = 1


        


if __name__ == '__main__':
    animal = AnimalStats()
    
    print(id(animal))
