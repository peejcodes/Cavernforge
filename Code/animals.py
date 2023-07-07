import random
import pygame

animal_species_list = ["dog", "cat", "squirrel", "hamster", "rabbit", "porcupine", "racoon", "fox", "cow", "bull", "pig", "goat", "sheep", "deer", "bear", "rooster", "chicken", "duck", "swan", "flamingo", "bird", "seagull", "bat", "horse"]


["bee", "owl", "vulture", "parrot", "toucan", "bison", "buffalo", "camel", "crab", "crocodile", "elephant", "fish", "frog", "gorilla", "hippo", "horseshoe crab", "kangaroo", "lion", "lizard", "mammoth", "monkey", "panther", "penguin", "pufferfish", "stingray", "rhino", "sabertooth", "seal", "sea turtle", "shark", "swordfish", "tiger", "turtle", "walrus", "zebra"]

species_dict = {"dog": {
        "habitat": "field",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True,
        "food_source": True,
        "tamable": True
    },
    "cat": {
        "habitat": "field",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "squirrel": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "hamster": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "rabbit": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "porcupine": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "racoon": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "fox": {
        "habitat": "field",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "cow": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "bull": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "pig": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "goat": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "sheep": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "deer": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "bear": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": True,
        "food_source": True,
        "tamable": True
    },
    "rooster": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "chicken": {
        "habitat": "field",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "duck": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "duck",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "swan": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "flamingo": {
        "habitat": "lake",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "bird": {
        "habitat": "all",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "seagull": {
        "habitat": "beach",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "bat": {
        "habitat": "mountain",
        "sprite": "file",
        "diet": "insectavore, frugavore, carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": True,
        "tamable": True
    },
    "horse": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": True,
        "tamable": True
    }, 
    "bee": {
        "habitat": "field",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": True
    },
    "owl": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "vulture": {
        "habitat": "desert",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "parrot": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "toucan": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "bison": {
        "habitat": "prairie",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "buffalo": {
        "habitat": "prairie",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "camel": {
        "habitat": "desert",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "crab": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "crocodile": {
        "habitat": "swamp",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "elephant": {
        "habitat": "savanna",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "fish": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "frog": {
        "habitat": "pond",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "gorilla": {
        "habitat": "jungle",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "hippo": {
        "habitat": "river",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "horseshoe crab": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "kangaroo": {
        "habitat": "grassland",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "lion": {
        "habitat": "savanna",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "lizard": {
        "habitat": "desert",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "mammoth": {
        "habitat": "tundra",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "monkey": {
        "habitat": "forest",
        "sprite": "file",
        "diet": "omnivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "panther": {
        "habitat": "jungle",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "penguin": {
        "habitat": "polar",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "pufferfish": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "stingray": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "rhino": {
        "habitat": "grassland",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "sabertooth": {
        "habitat": "tundra",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "seal": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "sea turtle": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "shark": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "swordfish": {
        "habitat": "ocean",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "tiger": {
        "habitat": "jungle",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": True,
        "food_source": False
    },
    "turtle": {
        "habitat": "pond",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    },
    "walrus": {
        "habitat": "arctic",
        "sprite": "file",
        "diet": "carnivore",
        "tamable": False,
        "hostile": False,
        "food_source": False
    },
    "zebra": {
        "habitat": "grassland",
        "sprite": "file",
        "diet": "herbivore",
        "tamable": True,
        "hostile": False,
        "food_source": False
    }
}




animal_demeanors = [
    "Affectionate",
    "Friendly",
    "Loyal",
    "Protective",
    "Curious",
    "Energetic",
    "Alert",
    "Independent",
    "Timid",
    "Nervous",
    "Hostile",
    "Vicious",
    "Dominant",
    "Intimidating",
    "Combative",
    "Savage"
]


class Animal:
    def __init__(self, species):
        # attributes
        self.species = species
        self.sprite = species_dict[species]["sprite"]
        self.sex = self.get_sex()
        self.demeanor = self.get_demeanor()
        self.diet = species_dict[species]["diet"]
        self.habitat = species_dict[species]["habitat"]
        self.tamable = species_dict[species]["tamable"]

        # movement
        self.direction = 0
        self.speed = 1
        self.position = (random.randint(0, 10000), random.randint(0, 10000))
        
        #changeable attributes
        self.is_pregnant = False
        self.is_baby = False
        self.stats = "animal stats"
        self.is_tame = False
        
        
    def __str__(self):
        return f"species='{self.species}',\nsprite='{self.sprite}',\nsex='{self.sex}', \ndemeanor='{self.demeanor}', \ndiet='{self.diet}', \nhabitat='{self.habitat}', \ntamable={self.tamable}, \n\ndirection={self.direction}, \nspeed={self.speed}, \nposition={self.position}\n\nis_pregnant={self.is_pregnant}, \nstats='{self.stats}', \nis_tame='{self.is_tame}'"

    
    def __repr__(self):
        return  f"{self.species}, {self.position}"

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
        sexes = ["male","female"]
        self.sex = random.choice(sexes)
        return self.sex
        
    def give_birth(self):
        self.is_pregnant = False
        #create a baby animal


if __name__ == "__main__":
    goat = Animal("goat")
    #print(goat)
    print(goat)
