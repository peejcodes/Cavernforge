import random
import pygame

animal_species_list = ['dog', 'cat', 'squirrel', 'hamster', 'rabbit', 'porcupine', 'racoon', 'fox', 'cow', 'bull', 'pig', 'goat', 'sheep', 'deer', 'bear', 'rooster', 'chicken', 'duck', 'swan', 'flamingo', 'bird', 'seagull', 'bat', 'horse']

species_dict = {"dog": {
    "habitat": "field",
    "sprite": "file",
    "diet": "carnivore",
    "tamable": True
},
    "cat": {
        "habitat": "field",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": True
    },
    "squirrel": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "hamster": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "rabbit": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    },
    "porcupine": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "racoon": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False
    },
    "fox": {
        "habitat": "field",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False
    },
    "cow": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    },
    "bull": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    },
    "pig": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True
    },
    "goat": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    },
    "sheep": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    },
    "deer": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "bear": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False
    },
    "rooster": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True
    },
    "chicken": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True
    },
    "duck": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "duck",
        "tamable": True
    },
    "swan": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "flamingo": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False
    },
    "bird": {
        "habitat": "all",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True
    },
    "seagull": {
        "habitat": "beach",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False
    },
    "bat": {
        "habitat": "mountain",
        "sprite": "file",
        "diet": "insectavore, frugavore, carnivore",
        "tamable": False
    },
    "horse": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True
    }
}


animal_demeanors = [
    'Affectionate',
    'Friendly',
    'Loyal',
    'Protective',
    'Curious',
    'Energetic',
    'Alert',
    'Independent',
    'Timid',
    'Nervous',
    'Hostile',
    'Vicious',
    'Dominant',
    'Intimidating',
    'Combative',
    'Savage'
]


class Animal:
    def __init__(self, species):
        #attributes
        self.species = species
        self.sprite = species_dict[species]['sprite']
        self.sex = self.get_sex()
        self.is_pregnant = False
        self.stats = 'animal stats'
        self.demeanor = self.get_demeanor()
        self.diet = species_dict[species]['diet']
        self.habitat = species_dict[species]['habitat']
        self.tamable = species_dict[species]['tamable']

        #movement
        self.direction = 0
        self.speed = 1
        self.position = [0,0]

    def __repr__(self):
        return f"species='{self.species}'," \
               f"\nsprite={self.sprite}," \
               f"\nsex='{self.sex}'," \
               f"\nis_pregnant={self.is_pregnant}," \
               f"\nstats='{self.stats}'," \
               f"\ndemeanor='{self.demeanor}'," \
               f"\ndiet='{self.diet}'," \
               f"\nhabitat='{self.habitat}'"

    def draw_animal(self, screen, scale, position, filename):
        image = pygame.image.load(filename)
        new_size = (image.get_width()*scale, image.get_height()*scale)
        print(new_size)
        resized_image = pygame.transform.scale(image,new_size)
        screen.blit(resized_image,position)
    
    def get_demeanor(self):
        self.demeanor = random.choice(animal_demeanors)
        return self.demeanor
        
    def get_sex(self):
        sexes = ['male','female']
        self.sex = random.choice(sexes)
        return self.sex


if __name__ == '__main__':
    goat = Animal('goat')
    #print(goat)
    print(goat)