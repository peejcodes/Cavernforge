
skill_types = ["animals", "arts", "building", "cooking", "crafting", "healing", "melee", "mining", "intellect", "botany", "shooting", "socializing"]




class Skill:
    def __init__(self, name):
        self.name = name
        self.skillpoints = 0
        self.xp_to_level = 0
        self.xp = 0
        self.level = 1
        
class Skills:
    def __init__(self):
        self.skills = {}
        self.load_skills()
        
        
    def load_skills(self):
        for skill in skill_types:
            self.skills[skill] = 0
            
    def __repr__(self):
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string[0:-1]
            