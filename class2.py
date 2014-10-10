class Classes(object):
	
	def __init__(self, keyword):
		#self.create()
		#return getattr()
		#__dict__
		print ""
	def __dict__(self):
		
	def create(self, keyword):
		self.classDict = {}#"": self.Empty(), "Fighter":Fighter(), 'Frog':Frog()}
		self.cClass = keyword	 	
		if keyword in self.classDict:
			print self.classDict
			return self.classDict[keyword]
		else:
			return self.Empty()
			
	def Empty(self):
		self.cClass = None
		self.align = self.anyAlign
		self.atkBonus = None
		self.fortSave = None
		self.refSave = None
		self.willSave = None
		self.special= None
		self.hitDie = None
		self.classSkills= None
		#self.skillPoints=None
		#self.skillPointsOnLevel = None
		print "no"
		
	def Fighter(self):
		self.cClass = "Fighter"
		self.align = ["none", "some"]#self.anyAlign() # no alignment restrictions
		self.atkBonus = 1
		self.fortSave = 2
		self.refSave = 0
		self.willSave = 0
		self.special=["Bonus Feat"]
		self.hitDie = 10
		self.classSkills=["Climb", "Craft", "Handle Animal", "Jump", "Ride", "Swim"]
		#self.skillPoints=(2+int)*4 # just use 2? 
		#self.skillPointsOnLevel = 2+int
		print"f"
		
	def Frog(self):
		self.cClass = "frog"
		self.align=["chripo=", "ribbit"]
		print "nof"
		
	def anyAlign(self):
		return ["Lawful Good", "Lawful Neutral", "Lawful Evil", 
				"Neutral Good", "True Neutral", "Neutral Evil",
				"Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
	