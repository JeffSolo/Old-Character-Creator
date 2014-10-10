from races import Races
import class2

class Character(Races):
	def __init__(self, cRace, cClass):
		#Races.create(cClass)
		class2.create(cClass)
		
	def printAttr(self):
		for attr in self.__dict__:
			print attr
			
x = Character('', '')
print x.cClass
#x.printAttr()	
#print x.atkBonus
#print x.language
#print x.raceDict.keys()