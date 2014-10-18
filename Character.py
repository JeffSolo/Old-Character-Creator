from races import Races
from classes import Classes

class Character(Races, Classes):
	def __init__(self, cRace, cClass):		
		Races.__init__(self, cRace)
		Classes.__init__(self, cClass)
		self.characterLevel = 1
	def printAttr(self):
		for attr in self.__dict__:
			print attr
			
#x = Character('','')
#x.printAttr()
#print x.align

