import random

needs_list = ['hunger', 'thirst', 'rest', 'health', 'social interaction', 'mental stimulation', 'healthcare', 'safety', 'cleanliness', 'exploration', 'entertainment', 'knowledge acquisition', 'creativity', 'nature appreciation', 'achievement', 'companionship', 'adventure', 'sense of purpose', 'financial stability', 'emotional well-being', 'self-improvement', 'power and influence', 'spiritual fulfillment', 'environmental preservation', 'community involvement', 'introspection', 'legacy', 'conflict resolution']



needs_dict= {
"hunger": [
"eating a meal",
"snacking on fruits",
"cooking a hearty stew",
"hunting for fresh meat",
"fishing for a fresh catch",
"baking bread",
"gathering edible plants",
"foraging for mushrooms",
"trading for food supplies",
"planting and tending to a vegetable garden",
],
"thirst": [
"drinking clean water",
"brewing a refreshing potion",
"collecting rainwater",
"searching for a natural spring",
"harvesting juicy fruits",
"creating herbal teas",
"building a water filtration system",
"digging a well",
"exploring underground rivers",
"purifying water with magical spells",
],
"rest": [
"sleeping in a cozy bed",
"napping in a peaceful grove",
"finding a comfortable resting spot",
"relaxing by a campfire",
"meditating in a serene environment",
"taking a leisurely bath",
"lounging in a hammock",
"finding a shady spot to rest",
"retreating to a tranquil sanctuary",
"practicing deep breathing exercises",
],
"social interaction": [
"engaging in a friendly conversation",
"joining a group activity",
"sharing stories and legends",
"participating in a festival",
"collaborating on a task",
"attending a community gathering",
"hosting a dinner party",
"organizing a cultural event",
"forming a club or guild",
"creating and maintaining social bonds",
],
"mental stimulation": [
"reading ancient tomes",
"solving challenging puzzles",
"studying magical artifacts",
"learning a new language",
"exploring the depths of a library",
"practicing spellcasting",
"engaging in philosophical debates",
"attending educational workshops",
"embarking on intellectual quests",
"experimenting with alchemical concoctions",
],
"health": [
"visiting a healer for treatment",
"using healing potions or spells",
"resting and allowing the body to heal naturally",
"applying herbal remedies",
"practicing self-care and relaxation techniques",
"performing healing rituals",
"administering first aid to others",
"training in basic medical skills",
"researching new medicinal herbs",
"creating healing salves and ointments",
],
"safety": [
"building secure fortifications",
"setting up traps and alarms",
"patrolling the surroundings",
"establishing a guard rotation",
"seeking shelter during dangerous situations",
"training in self-defense techniques",
"learning survival skills",
"creating emergency evacuation plans",
"investigating and neutralizing threats",
"forming alliances with neighboring factions for protection",
],
"cleanliness": [
"bathing in a refreshing stream",
"washing clothes and belongings",
"sweeping and tidying living spaces",
"cleaning and organizing personal items",
"maintaining a clean environment through regular upkeep",
"scrubbing floors and surfaces",
"polishing armor and weapons",
"cultivating a hygienic culture",
"practicing waste management",
"recycling and reusing resources",
],
"exploration": [
"venturing into uncharted territories",
"mapping new regions",
"searching for hidden treasures",
"navigating through ancient ruins",
"climbing towering mountains",
"sailing across uncharted seas",
"scouting for valuable resources",
"conducting geological surveys",
"documenting new flora and fauna",
"discovering secret passages and shortcuts",
],
"entertainment": [
"playing musical instruments",
"dancing to lively tunes",
"watching captivating performances",
"engaging in competitive games",
"attending a theatrical play",
"organizing community celebrations",
"arranging storytelling sessions",
"hosting talent shows",
"creating and performing magical illusions",
"arranging outdoor recreational activities",
],
"knowledge acquisition": [
"attending lectures and seminars",
"participating in workshops",
"reading academic journals",
"conducting experiments",
"interviewing experts",
"exploring ancient manuscripts",
"documenting oral histories",
"researching and documenting local folklore",
"learning from wise elders",
"collecting and analyzing data",
],
"creativity": [
"painting or drawing",
"sculpting and carving",
"writing stories or poetry",
"composing music",
"designing and crafting intricate jewelry",
"building elaborate structures",
"brewing unique potions",
"inventing new tools or gadgets",
"creating magical spells",
"embroidering and weaving",
],
"nature appreciation": [
"observing and sketching wildlife",
"stargazing and identifying constellations",
"tending to a garden",
"planting trees and flowers",
"taking nature walks",
"photographing natural landscapes",
"birdwatching and identifying species",
"caring for injured animals",
"learning about herbal remedies",
"preserving and protecting natural habitats",
],
"achievement": [
"completing challenging quests",
"obtaining rare and powerful artifacts",
"mastering a difficult skill",
"winning in competitive tournaments",
"earning the respect and recognition of peers",
"unlocking secret achievements",
"accomplishing personal goals",
"overcoming formidable adversaries",
"becoming a renowned figure in the realm",
"ascending to positions of leadership",
],
"companionship": [
"forming deep friendships",
"forging strong bonds with animal companions",
"adopting and caring for pets",
"building a loyal team or party",
"supporting and comforting others",
"participating in group activities",
"sharing meals and stories together",
"taking care of each other's needs",
"celebrating special occasions",
"offering emotional support and understanding",
],
"adventure": [
"embarking on epic quests",
"braving dangerous dungeons",
"defeating formidable foes",
"rescuing captured allies",
"exploring hidden realms",
"encountering mythical creatures",
"solving ancient riddles",
"unraveling mysterious prophecies",
"recovering lost treasures",
"defending the realm from evil forces",
],
"sense of purpose": [
"serving as protectors of the realm",
"preserving ancient traditions",
"advocating for justice and equality",
"fostering harmony between races",
"guarding sacred artifacts",
"upholding moral values",
"teaching and mentoring others",
"exploring personal spirituality",
"leading and organizing community initiatives",
"working towards a greater cause or mission",
],
"financial stability": [
"engaging in trade and commerce",
"managing and investing resources",
"building and maintaining economic networks",
"crafting valuable goods for sale",
"offering services in high demand",
"negotiating profitable deals",
"creating and running a successful business",
"acquiring and managing properties",
"saving and investing for the future",
"contributing to the local economy",
],
"emotional well-being": [
"practicing mindfulness and meditation",
"seeking therapy or counseling",
"expressing emotions through art or writing",
"engaging in self-reflection and journaling",
"participating in support groups",
"surrounding oneself with positive influences",
"taking breaks and engaging in self-care",
"establishing healthy boundaries",
"processing emotions through physical activities",
"cultivating gratitude and practicing acts of kindness",
],
"self-improvement": [
"training to improve combat skills",
"studying magic and mastering spells",
"learning new languages and dialects",
"developing diplomatic skills",
"acquiring knowledge in various subjects",
"practicing physical fitness and endurance",
"exploring personal strengths and weaknesses",
"overcoming fears and phobias",
"adopting healthy habits and routines",
"cultivating patience and perseverance",
],
"power and influence": [
"rising through the ranks of a guild or organization",
"becoming a respected advisor or counselor",
"gaining political influence",
"establishing oneself as a renowned expert",
"commanding a powerful army",
"securing alliances with other factions",
"influencing key decisions and policies",
"controlling valuable resources",
"building and ruling a prosperous kingdom",
"fulfilling prophecies and destiny",
],
"spiritual fulfillment": [
"practicing religious rituals",
"seeking divine guidance",
"embarking on pilgrimages",
"meditating in sacred places",
"studying ancient scriptures",
"connecting with ancestral spirits",
"performing acts of charity and kindness",
"attaining spiritual enlightenment",
"becoming a spiritual leader or teacher",
"helping others find spiritual solace",
],
"environmental preservation": [
"advocating for sustainable practices",
"educating others about conservation",
"cleaning and restoring natural habitats",
"reducing waste and promoting recycling",
"planting trees and engaging in reforestation",
"protecting endangered species",
"campaigning against pollution and deforestation",
"preserving natural resources",
"promoting renewable energy sources",
"supporting initiatives for ecological balance",
],
"community involvement": [
"volunteering for community projects",
"organizing fundraisers for charitable causes",
"participating in neighborhood clean-ups",
"mentoring and tutoring others",
"supporting local businesses and artisans",
"serving on local councils or committees",
"collaborating with neighboring communities",
"promoting cultural diversity and inclusivity",
"initiating projects for community development",
"taking part in festivals and celebrations",
],
"introspection": [
"engaging in self-reflection",
"journaling personal thoughts and emotions",
"practicing meditation and mindfulness",
"exploring one's past and personal history",
"examining personal values and beliefs",
"setting and evaluating personal goals",
"questioning and challenging assumptions",
"embracing solitude for self-discovery",
"seeking personal growth and enlightenment",
"striving for inner peace and harmony",
],
"legacy": [
"passing down knowledge and traditions",
"teaching future generations",
"recording personal memoirs and histories",
"creating works of art or literature",
"establishing charitable foundations",
"founding schools or educational institutions",
"building monuments or landmarks",
"mentoring and shaping young leaders",
"establishing family lineages",
"leaving a lasting impact on the world",
],
"conflict resolution": [
"mediating disputes between individuals or factions",
"facilitating peaceful negotiations",
"promoting empathy and understanding",
"finding common ground and compromise",
"encouraging open dialogue and communication",
"implementing conflict resolution strategies",
"training others in conflict resolution skills",
"addressing root causes of conflicts",
"forging diplomatic alliances",
"promoting harmony and reconciliation",
    ],
}


class Needs:
    def __init__(self):
        self.need_list = {'hunger':0, 'thirst':0, 'rest':0, 'health':0}
        
        
        for i in range(4):
            need = random.choice(needs_list)
            if need not in self.need_list:
                self.need_list[need] = 0
    
    def __repr__(self):
        string = ''
        for attribute_name, attribute_value in vars(self).items():
            string += (f"{attribute_name}: {attribute_value}\n")
        return string[0:-1]
        
    def reduce_need(self, need):
            pass
