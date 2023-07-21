import random



personalities = [
    "adventurous",
    "ambitious",
    "analytical",
    "artistic",
    "assertive",
    "caring",
    "charismatic",
    "charming",
    "competitive",
    "confident",
    "creative",
    "curious",
    "determined",
    "diplomatic",
    "disciplined",
    "easygoing",
    "empathetic",
    "energetic",
    "enthusiastic",
    "extroverted",
    "friendly",
    "funny",
    "generous",
    "gracious",
    "honest",
    "humble",
    "imaginative",
    "independent",
    "innovative",
    "intelligent",
    "introverted",
    "kind",
    "logical",
    "loyal",
    "modest",
    "optimistic",
    "organized",
    "outgoing",
    "passionate",
    "patient",
    "perceptive",
    "persistent",
    "practical",
    "proactive",
    "rational",
    "reliable",
    "reserved",
    "resourceful",
    "respectful",
    "responsible",
    "self-confident",
    "self-disciplined",
    "sensitive",
    "sociable",
    "spontaneous",
    "supportive",
    "sympathetic",
    "tactful",
    "tenacious",
    "thoughtful",
    "trustworthy",
    "understanding",
    "visionary",
    "witty",
    "altruistic",
    "bold",
    "calm",
    "capable",
    "carefree",
    "compassionate",
    "considerate",
    "cooperative",
    "courageous",
    "decisive",
    "diligent",
    "dreamer",
    "empowered",
    "focused",
    "genuine",
    "grateful",
    "hardworking",
    "humorous",
    "idealistic",
    "imaginative",
    "innovative",
    "inspiring",
    "intuitive",
    "leader",
    "logical",
    "nurturing",
    "observant",
    "patient",
    "peaceful",
    "philanthropic",
    "pragmatic",
    "reliable",
    "resilient",
    "romantic",
    "thoughtful",
    "versatile"
]


class Personality:
    def __init__(self):
        self.personality = []
        
    def personality_generator(self):
        for i in range(5):
            a = random.choice(personalities)
            self.personality.append(a)
        print(self.personality)
        
    def __repr__(self):
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string[0:-1]
            

if __name__=='__main__':
    personality = Personality()
    personality.personality_generator()