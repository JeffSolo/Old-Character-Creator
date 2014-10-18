import inspect

class Races(object):
	def __init__(self, keyword):
		self.EmptyR()
		self.raceList = [function for function in vars(Races).keys() if not (function.startswith('_') or function == 'EmptyR')]
		for name, method in inspect.getmembers(self, inspect.ismethod):
			if name == keyword:
				method()
				break
			
	def EmptyR(self):
		self.race = None
		self.language= None
		self.bonusLang= None
		self.traits = {}
		self.size = None
		self.speed= None
		self.favClass= None
		self.bonusSkills= None
		self.ACsize = 0
		self.AttackBonus = None
		self.bonusFeat = None
		self.baseRaceSkillPoints = None
		self.levelRaceSkillPoints = None
		#self.levelAdjust= None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		self.grappleMod = 0
		
	def Elf(self):
		self.Race = "Elf"
		self.language=["Common", "Elven"]
		self.bonusLang=["Draconic", "Gnoll", "Gnome", "Goblin", "Orc", "Sylvan"]
		self.traits = {"DEX":'+2', "CON":'-2'}
		self.size = 'M'
		self.ACsize = 0
		self.AttackBonus = None
		self.speed=30
		self.favClass="Wizard"
		self.bonusSkills={"Listen":2, "Search":2, "Spot":2}
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Dwarf(self):
		self.Race = "Dwarf"
		self.language = ["Common", "Dwarven"]
		self.bonusLang = ["Giant", "Gnome", "Goblin", "Orc", "Terran", "Undercommon"]
		self.traits = {"CON":'+2', "CHA":'-2'}
		self.size = 'M'
		self.ACsize = 0
		self.AttackBonus = None
		self.speed = 20
		self.favClass = "Fighter"
		self.bonusSkills = None
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Human(self):
		self.Race = "Human"
		self.language= ["Common"]
		self.bonusLang = ["Abyssal","Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", 
							"Gnome", "Goblin", "Giant", "Gnoll", "Halfling", "Ignan", "Infernal", 
							"Orc", "Sylvan", "Terran", "Undercommon"]
		self.traits = {}
		self.size = 'M'
		self.ACsize = 0
		self.AttackBonus = None
		self.speed = 30
		self.favClass = "Any"
		self.bonusSkills = None
		self.bonusFeat = 1
		self.baseRaceSkillPoints = 4
		self.levelRaceSkillPoints= 1
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Gnome(self):
		self.Race = "Gnome"
		self.language= ["Common", "Gnome"]
		self.bonusLang = ["Draconic", "Dwarven", "Elven", "Giant", "Goblin", "Orc"]
		self.traits = {'CON':'+2','STR':'-2'}
		self.size = 'S'
		self.ACsize = 1
		self.AttackBonus = 1
		self.speed = 20
		self.favClass = "Bard"
		self.bonusSkills = {"Listen":2, "Alchemy":2, "Hide":4}
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Half_Elf(self):
		self.Race = "Half-Elf"
		self.language= ["Common", "Elven"]
		self.bonusLang = ["Abyssal","Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", 
							"Gnome", "Goblin", "Giant", "Gnoll", "Halfling", "Ignan", "Infernal", 
							"Orc", "Sylvan", "Terran", "Undercommon"]
		self.traits = {}
		self.size = 'M'
		self.ACsize = 0
		self.AttackBonus = None
		self.speed = 30
		self.favClass = "Any"
		self.bonusSkills = {"Listen":1, "Search":1, "Spot":1}
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Half_Orc(self):
		self.Race = "Half-Orc"
		self.language= ["Common", "Orc"]
		self.bonusLang = ["Draconic", "Goblin", "Giant", "Gnoll", "Infernal"]
		self.traits = {"STR":'+2', "INT":'-2'}
		self.size = 'M'
		self.ACsize = 0
		self.AttackBonus = None
		self.speed = 30
		self.favClass = "Barbarian"
		self.bonusSkills = {}
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = None
		self.FortSave = None
		self.WillSave = None
		
	def Halfling(self):
		self.Race = "Halfling"
		self.language= ["Common", "Halfling"]
		self.bonusLang = ["Dwarven", "Elven", "Gnome", "Goblin", "Orc"]
		self.traits = {"STR":'-2', "DEX":'+2'}
		self.size = 'S'
		self.ACsize = 1
		self.AttackBonus = 1
		self.speed = 20
		self.favClass = "Rogue"
		self.bonusSkills = {"Climb":2, "Jump":2, "Move Silently":2, "Listen":2, "Hide":4}
		self.bonusFeat = None
		self.extraSkillPoints = None
		self.ReflexSave = 1
		self.FortSave = 1
		self.WillSave = 1