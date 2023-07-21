health_systems = ["sight", "hearing", "moving", "manipulation", "talking", "eating", "breathing", "blood filtration", "blood pumping", "metabolism", "consciousness"]

pain_ = []

class Health:
    def __init__(self):
        self.sight = 0
    
    def __repr__(self):
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string[0:-1]
