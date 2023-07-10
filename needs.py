import random

needs_list = ['Hunger', 'Hunger', 'Hunger', 'Social interaction', 'Mental stimulation', 'Healthcare', 'Safety', 'Cleanliness', 'Exploration', 'Entertainment', 'Knowledge acquisition', 'Creativity', 'Nature appreciation', 'Achievement', 'Companionship', 'Adventure', 'Sense of purpose', 'Financial stability', 'Emotional well-being', 'Self-improvement', 'Power and influence', 'Spiritual fulfillment', 'Environmental preservation', 'Community involvement', 'Introspection', 'Legacy', 'Conflict resolution']



needs_dict= {
    "Hunger": [
        "Eating a meal",
        "Snacking on fruits",
        "Cooking a hearty stew",
        "Hunting for fresh meat",
        "Fishing for a fresh catch",
        "Baking bread",
        "Gathering edible plants",
        "Foraging for mushrooms",
        "Trading for food supplies",
        "Planting and tending to a vegetable garden",
    ],
    "Thirst": [
        "Drinking clean water",
        "Brewing a refreshing potion",
        "Collecting rainwater",
        "Searching for a natural spring",
        "Harvesting juicy fruits",
        "Creating herbal teas",
        "Building a water filtration system",
        "Digging a well",
        "Exploring underground rivers",
        "Purifying water with magical spells",
    ],
    "Rest": [
        "Sleeping in a cozy bed",
        "Napping in a peaceful grove",
        "Finding a comfortable resting spot",
        "Relaxing by a campfire",
        "Meditating in a serene environment",
        "Taking a leisurely bath",
        "Lounging in a hammock",
        "Finding a shady spot to rest",
        "Retreating to a tranquil sanctuary",
        "Practicing deep breathing exercises",
    ],
    "Social interaction": [
        "Engaging in a friendly conversation",
        "Joining a group activity",
        "Sharing stories and legends",
        "Participating in a festival",
        "Collaborating on a task",
        "Attending a community gathering",
        "Hosting a dinner party",
        "Organizing a cultural event",
        "Forming a club or guild",
        "Creating and maintaining social bonds",
    ],
    "Mental stimulation": [
        "Reading ancient tomes",
        "Solving challenging puzzles",
        "Studying magical artifacts",
        "Learning a new language",
        "Exploring the depths of a library",
        "Practicing spellcasting",
        "Engaging in philosophical debates",
        "Attending educational workshops",
        "Embarking on intellectual quests",
        "Experimenting with alchemical concoctions",
    ],
    "Health": [
        "Visiting a healer for treatment",
        "Using healing potions or spells",
        "Resting and allowing the body to heal naturally",
        "Applying herbal remedies",
        "Practicing self-care and relaxation techniques",
        "Performing healing rituals",
        "Administering first aid to others",
        "Training in basic medical skills",
        "Researching new medicinal herbs",
        "Creating healing salves and ointments",
    ],
    "Safety": [
        "Building secure fortifications",
        "Setting up traps and alarms",
        "Patrolling the surroundings",
        "Establishing a guard rotation",
        "Seeking shelter during dangerous situations",
        "Training in self-defense techniques",
        "Learning survival skills",
        "Creating emergency evacuation plans",
        "Investigating and neutralizing threats",
        "Forming alliances with neighboring factions for protection",
    ],
    "Cleanliness": [
        "Bathing in a refreshing stream",
        "Washing clothes and belongings",
        "Sweeping and tidying living spaces",
        "Cleaning and organizing personal items",
        "Maintaining a clean environment through regular upkeep",
        "Scrubbing floors and surfaces",
        "Polishing armor and weapons",
        "Cultivating a hygienic culture",
        "Practicing waste management",
        "Recycling and reusing resources",
    ],
    "Exploration": [
        "Venturing into uncharted territories",
        "Mapping new regions",
        "Searching for hidden treasures",
        "Navigating through ancient ruins",
        "Climbing towering mountains",
        "Sailing across uncharted seas",
        "Scouting for valuable resources",
        "Conducting geological surveys",
        "Documenting new flora and fauna",
        "Discovering secret passages and shortcuts",
    ],
    "Entertainment": [
        "Playing musical instruments",
        "Dancing to lively tunes",
        "Watching captivating performances",
        "Engaging in competitive games",
        "Attending a theatrical play",
        "Organizing community celebrations",
        "Arranging storytelling sessions",
        "Hosting talent shows",
        "Creating and performing magical illusions",
        "Arranging outdoor recreational activities",
    ],
    "Knowledge acquisition": [
        "Attending lectures and seminars",
        "Participating in workshops",
        "Reading academic journals",
        "Conducting experiments",
        "Interviewing experts",
        "Exploring ancient manuscripts",
        "Documenting oral histories",
        "Researching and documenting local folklore",
        "Learning from wise elders",
        "Collecting and analyzing data",
    ],
    "Creativity": [
        "Painting or drawing",
        "Sculpting and carving",
        "Writing stories or poetry",
        "Composing music",
        "Designing and crafting intricate jewelry",
        "Building elaborate structures",
        "Brewing unique potions",
        "Inventing new tools or gadgets",
        "Creating magical spells",
        "Embroidering and weaving",
    ],
    "Nature appreciation": [
        "Observing and sketching wildlife",
        "Stargazing and identifying constellations",
        "Tending to a garden",
        "Planting trees and flowers",
        "Taking nature walks",
        "Photographing natural landscapes",
        "Birdwatching and identifying species",
        "Caring for injured animals",
        "Learning about herbal remedies",
        "Preserving and protecting natural habitats",
    ],
    "Achievement": [
        "Completing challenging quests",
        "Obtaining rare and powerful artifacts",
        "Mastering a difficult skill",
        "Winning in competitive tournaments",
        "Earning the respect and recognition of peers",
        "Unlocking secret achievements",
        "Accomplishing personal goals",
        "Overcoming formidable adversaries",
        "Becoming a renowned figure in the realm",
        "Ascending to positions of leadership",
    ],
    "Companionship": [
        "Forming deep friendships",
        "Forging strong bonds with animal companions",
        "Adopting and caring for pets",
        "Building a loyal team or party",
        "Supporting and comforting others",
        "Participating in group activities",
        "Sharing meals and stories together",
        "Taking care of each other's needs",
        "Celebrating special occasions",
        "Offering emotional support and understanding",
    ],
    "Adventure": [
        "Embarking on epic quests",
        "Braving dangerous dungeons",
        "Defeating formidable foes",
        "Rescuing captured allies",
        "Exploring hidden realms",
        "Encountering mythical creatures",
        "Solving ancient riddles",
        "Unraveling mysterious prophecies",
        "Recovering lost treasures",
        "Defending the realm from evil forces",
    ],
    "Sense of purpose": [
        "Serving as protectors of the realm",
        "Preserving ancient traditions",
        "Advocating for justice and equality",
        "Fostering harmony between races",
        "Guarding sacred artifacts",
        "Upholding moral values",
        "Teaching and mentoring others",
        "Exploring personal spirituality",
        "Leading and organizing community initiatives",
        "Working towards a greater cause or mission",
    ],
    "Financial stability": [
        "Engaging in trade and commerce",
        "Managing and investing resources",
        "Building and maintaining economic networks",
        "Crafting valuable goods for sale",
        "Offering services in high demand",
        "Negotiating profitable deals",
        "Creating and running a successful business",
        "Acquiring and managing properties",
        "Saving and investing for the future",
        "Contributing to the local economy",
    ],
    "Emotional well-being": [
        "Practicing mindfulness and meditation",
        "Seeking therapy or counseling",
        "Expressing emotions through art or writing",
        "Engaging in self-reflection and journaling",
        "Participating in support groups",
        "Surrounding oneself with positive influences",
        "Taking breaks and engaging in self-care",
        "Establishing healthy boundaries",
        "Processing emotions through physical activities",
        "Cultivating gratitude and practicing acts of kindness",
    ],
    "Self-improvement": [
        "Training to improve combat skills",
        "Studying magic and mastering spells",
        "Learning new languages and dialects",
        "Developing diplomatic skills",
        "Acquiring knowledge in various subjects",
        "Practicing physical fitness and endurance",
        "Exploring personal strengths and weaknesses",
        "Overcoming fears and phobias",
        "Adopting healthy habits and routines",
        "Cultivating patience and perseverance",
    ],
    "Power and influence": [
        "Rising through the ranks of a guild or organization",
        "Becoming a respected advisor or counselor",
        "Gaining political influence",
        "Establishing oneself as a renowned expert",
        "Commanding a powerful army",
        "Securing alliances with other factions",
        "Influencing key decisions and policies",
        "Controlling valuable resources",
        "Building and ruling a prosperous kingdom",
        "Fulfilling prophecies and destiny",
    ],
    "Spiritual fulfillment": [
        "Practicing religious rituals",
        "Seeking divine guidance",
        "Embarking on pilgrimages",
        "Meditating in sacred places",
        "Studying ancient scriptures",
        "Connecting with ancestral spirits",
        "Performing acts of charity and kindness",
        "Attaining spiritual enlightenment",
        "Becoming a spiritual leader or teacher",
        "Helping others find spiritual solace",
    ],
    "Environmental preservation": [
        "Advocating for sustainable practices",
        "Educating others about conservation",
        "Cleaning and restoring natural habitats",
        "Reducing waste and promoting recycling",
        "Planting trees and engaging in reforestation",
        "Protecting endangered species",
        "Campaigning against pollution and deforestation",
        "Preserving natural resources",
        "Promoting renewable energy sources",
        "Supporting initiatives for ecological balance",
    ],
    "Community involvement": [
        "Volunteering for community projects",
        "Organizing fundraisers for charitable causes",
        "Participating in neighborhood clean-ups",
        "Mentoring and tutoring others",
        "Supporting local businesses and artisans",
        "Serving on local councils or committees",
        "Collaborating with neighboring communities",
        "Promoting cultural diversity and inclusivity",
        "Initiating projects for community development",
        "Taking part in festivals and celebrations",
    ],
    "Introspection": [
        "Engaging in self-reflection",
        "Journaling personal thoughts and emotions",
        "Practicing meditation and mindfulness",
        "Exploring one's past and personal history",
        "Examining personal values and beliefs",
        "Setting and evaluating personal goals",
        "Questioning and challenging assumptions",
        "Embracing solitude for self-discovery",
        "Seeking personal growth and enlightenment",
        "Striving for inner peace and harmony",
    ],
    "Legacy": [
        "Passing down knowledge and traditions",
        "Teaching future generations",
        "Recording personal memoirs and histories",
        "Creating works of art or literature",
        "Establishing charitable foundations",
        "Founding schools or educational institutions",
        "Building monuments or landmarks",
        "Mentoring and shaping young leaders",
        "Establishing family lineages",
        "Leaving a lasting impact on the world",
    ],
    "Conflict resolution": [
        "Mediating disputes between individuals or factions",
        "Facilitating peaceful negotiations",
        "Promoting empathy and understanding",
        "Finding common ground and compromise",
        "Encouraging open dialogue and communication",
        "Implementing conflict resolution strategies",
        "Training others in conflict resolution skills",
        "Addressing root causes of conflicts",
        "Forging diplomatic alliances",
        "Promoting harmony and reconciliation",
    ],
}


class Needs:
    def __init__(self):
        self.need_list = ['Hunger', 'Thirst', 'Rest', 'Health']
        
        for i in range(4):
            need = random.choice(needs_list)
            if need not in self.need_list:
                self.need_list.append(need)
            #self.need_list.append(random.choice(needs_list))
            
        print(self.need_list)
        
        
        
        
    pass
needs = Needs()