import math
import random

species_list = ['Beech', 'Ash', 'Poplar', 'Cypress', 'Ginkgo', 'Yew', 'Sycamore', 'Walnut', 'Hickory', 'Juniper', 'Chestnut', 'Redbud', 'Palm', 'Dogwood', 'Fruit Tree', 'Larch', 'Mulberry', 'Chestnut Oak', 'Buckeye', 'Fir Tree', 'Blackthorn', 'Linden', 'Elder', 'Alder', 'Serviceberry', 'Rowan', 'Hemlock', 'Hackberry', 'Catalpa', 'Holly', 'Spruce', 'Buckthorn', 'Hazel', 'Magnolia Tree', 'Black Gum', 'Hawthorn', 'Holly Oak', 'Butternut', 'Dog Rose', 'Hophornbeam', 'Paper Birch', 'Balsam Fir', 'Red Pine', 'Douglas Fir', 'Cedar', 'Cork Oak', 'Red Cedar', 'Yellow Birch', 'Black Spruce', 'Sweet Birch', 'Scots Pine', 'Jack Pine', 'Red Elderberry', 'White Pine', 'Sassafras', 'Ponderosa Pine', 'Hornbeam', 'White Spruce', 'Bigleaf Maple']
tree_species = {
    # Existing tree species

    "Beech": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False
    },
    "Ash": {
        "bark_texture": "rough",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "oval",
        "fruit_production": False
    },
    "Poplar": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "columnar",
        "fruit_production": False
    },
    "Cypress": {
        "bark_texture": "fibrous",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Ginkgo": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "broad",
        "fruit_production": True
    },
    "Yew": {
        "bark_texture": "rp4ough",
        "leaf_type": "evergreen",
        "foliage_color": "dark green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "conical",
        "fruit_production": True
    },
    "Sycamore": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False    
    },
    "Walnut": {
        "bark_texture": "rough",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "oval",
        "fruit_production": True
    },
    "Hickory": {
        "bark_texture": "ridged",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Juniper": {
        "bark_texture": "shredding",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "irregular",
        "fruit_production": True
    },
    "Chestnut": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "round",
        "fruit_production": True
    },
    "Redbud": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "purple",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "vase-like",
        "fruit_production": False
    },
    "Palm": {
        "bark_texture": "smooth",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "fan-shaped",
        "fruit_production": True
    },
    "Dogwood": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Fruit Tree": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "varies",
        "fruit_production": True
    },
    "Larch": {
        "bark_texture": "rough",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Mulberry": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Chestnut Oak": {
        "bark_texture": "ridged",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Buckeye": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Fir Tree": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Blackthorn": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "spreading",
        "fruit_production": True
    },
    "Linden": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Elder": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Alder": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Serviceberry": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "oval",
        "fruit_production": True
    },
    "Rowan": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Hemlock": {
        "bark_texture": "scaly",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Hackberry": {
        "bark_texture": "warty",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Catalpa": {
        "bark_texture": "scaly",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "broad",
        "fruit_production": True
    },
    "Holly": {
        "bark_texture": "smooth",
        "leaf_type": "evergreen",
        "foliage_color": "dark green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": True
    },
    "Spruce": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Buckthorn": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Hazel": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Magnolia Tree": {
        "bark_texture": "smooth",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Black Gum": {
        "bark_texture": "rough",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": True
    },
    "Hawthorn": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Holly Oak": {
        "bark_texture": "ridged",
        "leaf_type": "evergreen",
        "foliage_color": "dark green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Butternut": {
        "bark_texture": "ridged",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "Dog Rose": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "climbing",
        "fruit_production": True
    },
    "Hophornbeam": {
        "bark_texture": "ridged",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False
    },
    "Paper Birch": {
        "bark_texture": "paper-like",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Balsam Fir": {
        "bark_texture": "smooth",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "conical",
        "fruit_production": False
    },
    "Red Pine": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Douglas Fir": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Cedar": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Cork Oak": {
        "bark_texture": "ridged",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False
    },
    "Red Cedar": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Yellow Birch": {
        "bark_texture": "peeling",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False
    },
    "Black Spruce": {
        "bark_texture": "scaly",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Sweet Birch": {
        "bark_texture": "peeling",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "rounded",
        "fruit_production": False
    },
    "Scots Pine": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Jack Pine": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Red Elderberry": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "rounded",
        "fruit_production": True
    },
    "White Pine": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Sassafras": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "oval",
        "fruit_production": False
    },
    "Ponderosa Pine": {
        "bark_texture": "rough",
        "leaf_type": "evergreen",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "moderate",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    },
    "Hornbeam": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "oval",
        "fruit_production": False
    },
    "White Spruce": {
        "bark_texture": "scaly",
        "leaf_type": "evergreen", 
        "foliage_color": "green",
       "foliage_density": 1,
        "branch_density": "dense",
        "canopy_shape": "pyramidal",
        "fruit_production": False
    }, 
    "Bigleaf Maple": {
        "bark_texture": "smooth",
        "leaf_type": "deciduous",
        "foliage_color": "green",
        
       "foliage_density": 1,
        "branch_density": "sparse",
        "canopy_shape": "rounded",
        "fruit_production": False
    }
}



class Tree:
    def __init__(self, species, age, height, stage):
        """
        Initialize a Tree object with its species, age, height, and growth stage.

        Args:
            species (str): The species of the tree.
            age (int): The age of the tree in years.
            height (int): The height of the tree in feet.
            stage (int): The growth stage of the tree.

        Raises:
            KeyError: If the species is not found in the tree_species dictionary.
        """
        self.species = species
        self.age = age
        self.height = height
        self.growth_stage = stage
        self.growth_rate = math.exp(0.1 * (self.height / 100))
        self.bark_texture = tree_species[species]['bark_texture']
        self.leaf_type = tree_species[species]['leaf_type']
        self.foliage_color = tree_species[species]['foliage_color']
        self.foliage_density = tree_species[species]['foliage_density']
        self.branch_density = tree_species[species]['branch_density']
        self.canopy_shape = tree_species[species]['canopy_shape']
        self.fruit_production = tree_species[species]['fruit_production']
        
        self.position = (random.randint(0,10000),random.randint(0,10000))

    def grow(self):
        """
        Simulate the growth of the tree based on photosynthesis and water absorption.
        """
        # Implement the logic for tree growth here
        # Tree growth is based on photosynthesis and water absorption.
        # The maximum growth rate is determined by available resources.
        pass

    def leaf_cycle(self):
        """
        Simulate the cycle of leaves changing colors and dropping in deciduous tree_species.
        """
        # Implement the logic for leaves changing colors and dropping in deciduous tree_species
        # In winter, there are no leaves. In spring, the leaves are green and just forming.
        # In summer, the leaves are fully formed and green. In fall, the leaves turn yellow/orange/red and then they fall.
        pass

    def produce_fruit(self):
        """
        Simulate fruit production by the tree if applicable.
        """
        if self.fruit_production:
            # Implement the logic for fruit production here
            # Figure out when each tree starts to produce fruit and when they are harvested.
            # If it's the right time, try to harvest the fruit.
            # If fruits aren't developed enough, they fall off with the leaves and decompose.
            pass
        else:
            print("This tree does not produce fruits.")

    def photosynthesis(self):
        """
        Simulate the process of photosynthesis, where the tree converts sunlight into energy.
        """
        # Implement the logic for photosynthesis here.
        # Less sunlight or fewer leaves result in less photosynthesis and slower growth.
        pass

    def absorb_water(self):
        """
        Simulate the absorption of water by the tree's roots.
        """
        # Implement the logic for water absorption by the tree's roots.
        # tree_species have roots in the ground that extract water.
        # Water in the cells around the roots keeps the tree from getting thirsty.
        # Any rain helps keep the tree alive.
        # This logic should work for crops and flowers as well.
        pass

    def reproduce(self):
        """
        Simulate the reproduction of the tree, such as producing seeds or sprouting new shoots.
        """
        # Implement the logic for tree reproduction here.
        # In autumn, when leaves fall off the tree_species, each tile they fall to has a chance of having seeds fall.
        # Seeds can be picked up and put in a stockpile, but if left for too long, they either sprout or decompose.
        pass

    def provide_shade(self):
        """
        Calculate and provide the area covered by the tree for shade.
        """
        # Implement the logic to calculate and provide the shade area covered by the tree.
        # The amount of leaf coverage over each tile should be based on branch density and leaf density, as well as the canopy shape.
        pass

    def remove_carbon_dioxide(self):
        """
        Simulate the absorption and removal of carbon dioxide from the environment by the tree.
        """
        # Implement the logic for the tree to absorb and remove carbon dioxide from the environment.
        # The air space around everything contains invisible carbon dioxide.
        # tree_species slowly remove CO2 from the air, providing a boost to their natural growth.
        # CO2 is replenished by dwarves and elves doing work that causes its release.
        pass

    def calculate_age(self):
        """
        Calculate the age of the tree based on its growth.
        """
        # Implement the logic to calculate the age of the tree based on its growth.
        # This may not be needed as the age can be determined by the number of frames that pass.
        # The age could calculate on its own. For example, when you go to see its info, it refreshes.
        pass
        
    def __repr__(self):
        return f'{self.species}, {self.position}'

    def __str__(self):
        """
        Return a string representation of the Tree object.
        """
        return f"Tree Species: {self.species}\nBark Texture: {self.bark_texture}\nLeaf Type: {self.leaf_type}\nFoliage Color: {self.foliage_color}\nFoliage Density: {self.foliage_density}\nBranch Density: {self.branch_density}\nCanopy Shape: {self.canopy_shape}\nFruit Production: {self.fruit_production}\nPosition: {self.position}"

if __name__ == '__main__':
#birch = Tree('Yellow Birch', 3, 20, 2)
    #print(birch)
    listss = []
    for thing in tree_species:
        listss.append(thing)
    #print(listss)