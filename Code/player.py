import math
from pygame import Vector2
import pygame
from constants import *
from stats import PlayerStats
from needs import Needs
from skills import Skills
from names import *
from personalities import *
from health import *
from mood import *




class Player:
    def __init__(self, sprite):
        self.level = 1
        self.xp = 0
        self.xp_to_level = self.xp_calc(self.level)
        self.name = random_dwarf_name()
        self.sprite = sprite
        self.stats = PlayerStats()
        self.needs = Needs()
        self.skills = Skills()
        self.personality = Personality()
        self.health = Health()
        self.mood = Mood()
        
        
        self.position = Vector2(0, 0)
        self.direction = Vector2(0, 0)
        self.speed = 1
        self.acceleration = 0

    def __repr__(self):
        
        
     
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string

        #return f"level={self.level}\nxp={self.xp}\nxp_to_level={self.xp_to_level}\nname='{self.name}', \nsprite='{self.sprite}', \nstats={self.stats}\nneeds={self.needs}\nskills={self.skills}\nposition={self.position}\ndirection={self.direction}\nspeed={self.speed} \nacceleration={self.acceleration})"
        

        
    def load_image(self):
        self.image = pygame.image.load(self.sprite)
        

    def adjust_hp(self,qty):
        self.stats.health += qty
        return self.stats.health

    def xp_calc(self, level):
        base_experience = 500 # The base amount of experience required for level 1
        experience_growth = 1.23  # The rate at which experience requirement increases
        xp_to_level = math.floor(base_experience * (experience_growth ** (level - 1)))

        #print(xp_to_level, end = "")
        return xp_to_level

    def level_up(self):
        self.level += 1
        self.stats.health += 10
        self.stats.mana += 5
        self.stats.strength += 2
        self.stats.agility += 2
        self.stats.intelligence += 2
        self.xp_calc(self.level)

    def gain_experience(self, experience_points):
        self.xp += experience_points
        if self.xp >= self.xp_to_level:
            self.level_up()

    def move_player(self):
        self.position += self.direction*self.speed
    
    def draw_player(self,screen,x,y):
        dwarf = pygame.image.load('../Graphics/Player/tile001.png')
        screen.blit(dwarf, (x,y))

    def draw_player3(self,screen,x,y):
        size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (size[0]*3, size[1]*3))
        screen.blit(self.image, (x,y))

class Dwarf(Player):
    def __init__(self, sprite):
        super().__init__(sprite)
        self.name = random_dwarf_name()


class Elf(Player):
    def __init__(self,sprite):
        super().__init__(sprite)
        self.name = random_elf_name()


if __name__ == "__main__":

    dwarf = Dwarf('../Graphics/Animals/animals4_10.png')
    #print(dwarf.name)
    print(dwarf)
    
