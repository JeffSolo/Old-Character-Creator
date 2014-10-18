import inspect

class Classes(object):
	def __init__(self, keyword):
		self.EmptyC()
		self.classList = [function for function in vars(Classes).keys() if not (function.startswith('_') or function == 'EmptyC' or function == 'anyAlign')]
		for name, method in inspect.getmembers(self, inspect.ismethod):
			if name == keyword:
				method()
				break	
	
	# for leveling up, we can keep things like atkBonus in a list, and have it check the index with the level to retrieve proper
	def EmptyC(self):
		self.cClass = None
		self.align = None
		self.atkBonus = None
		self.cfortSave = None
		self.crefSave = None
		self.cwillSave = None
		self.special= None
		self.hitDie = ''
		self.classSkills= None
		self.spellCaster = False
		self.spellsKnown = {}	
		self.classSkillPoints=None
		#self.skillPointsOnLevel = None
	
	def Barbarian(self): 
		self.cClass = "Barbarian"
		self.align = ["Neutral Good", "Chaotic Good",
		              "True Neutral", "Chaotic Neutral",
		              "Neutral Evil", "Chaotic Evil"]
		self.atkBonus = 1
		self.cfortSave = 2
		self.crefSave = 0
		self.cwillSave = 0
		self.special= ["Rage 1/day", "Fast Movement"]
		self.hitDie = 12
		self.classSkills= ["Climb","Craft","Handle Animal","Intimidate","Intuit Direction","Jump","Listen","Ride","Swim","Wilderness Lore"]
		self.classSkillPoints = 4
		
	def Bard(self): 
		self.cClass = "Bard"
		self.align = ["Neutral Good", "Chaotic Good",
		              "True Neutral", "Chaotic Neutral",
		              "Neutral Evil", "Chaotic Evil"]
		self.atkBonus = 0
		self.cfortSave = 0
		self.crefSave = 2
		self.cwillSave = 2
		self.special= ["Bardic Music", "Bardic Knowledge"]
		self.hitDie = 6
		self.classSkills= ["Alchemy","Appraise","Balance","Bluff","Climb","Concentration","Craft","Decipher Script","Diplomacy",
							"Disguise","Escape Artist","Gather Information","Hide","Intuit Direction","Jump","Knowledge","Listen",
							"Move Silently","Perform","Pick Pocket","Profession","Scry","Sense Motive","Speak Language","Spellcraft",
							"Swim","Tumble","Use Magic Device"]
		self.classSkillPoints = 4
		self.spellCaster = True
		self.spellsKnown={"0":4}
		
		
	def Cleric(self):
		self.cclass = "Cleric"
		self.align = ["Dependent on Deity"]
		self.atkBonus = 0
		self.cfortSave = 2
		self.crefSave = 0
		self.cwillSave = 2
		self.special = ["Domain Spells", "Turn/rebuke undead"]
		self.hitDie = 8
		self.classSkills = ["Concentration", "Craft", "Diplomacy", "Heal", "Knowledge (arcana)","Knowledge (religion)", "Profession", 
							"Scry", "Spellcraft"]
		self.classSkillPoints = 2
		self.spellCaster = True
		self.spellsKnown={"0":3, "1":1+1} 
		
	def Druid(self):
		self.cClass = "Druid"
		self.align = ["Lawful Neutral", "True Neutral", "Chaotic Neutral"]
		self.atkBonus = 0
		self.cfortSave = 2
		self.crefSave = 0
		self.cwillSave = 2
		self.special = ["Druidic Language", "Nature Sense", "Animal Companion"]
		self.hitDie = 8
		self.classSkills = ["Animal Empathy","Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Intuit Direction", 
							"Knowledge (nature)", "Profession", "Scry", "Spellcraft", "Swim", "Wilderness Lore"]
		self.classSkillPoints = 4
		self.spellCaster = True
		self.spellsKnown = {"0":3, "1":1}
	
	def Fighter(self):
		self.cClass = "Fighter"
		self.align = self.anyAlign()
		self.atkBonus = 1
		self.cfortSave = 2
		self.crefSave = 0
		self.cwillSave = 0
		self.special=["Bonus Feat"]
		self.hitDie = 10
		self.classSkills=["Climb", "Craft", "Handle Animal", "Jump", "Ride", "Swim"]
		self.classSkillPoints = 2#(2+int)*4 # just use 2? 
		#self.skillPointsOnLevel = 2+int
	
	def anyAlign(self):
		return ["Lawful Good",    "Neutral Good", "Chaotic Good",
				"Lawful Neutral", "True Neutral", "Chaotic Neutral",
				"Lawful Evil",    "Neutral Evil", "Chaotic Evil"]