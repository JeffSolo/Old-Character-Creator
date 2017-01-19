#saveload
import os, json
import zipfile as zf
import tkFileDialog as tkf
import filestructure as fstruct
from collections import OrderedDict

def saveChar(obj):
	char = GetCharacterDict(obj)
	opts = {}
	opts['defaultextension'] = '.dnd'
	opts['initialdir'] = fstruct.CPATH
	opts['initialfile'] = fstruct.NAME		
	savefile = tkf.asksaveasfilename(**opts)
	charfile = os.path.splitext(savefile)[0]+".char"
	'''
	data = OrderedDict( [
		("Player Name", self.Names["PlayerName"].get()),
		("Character Name", self.Names["CharName"].get()),
		("Class", self.Class.get()), 
		("Race", self.Race.get()),
		("Character info", OrderedDict(zip([i for i in char], [charInfo[i].get() for i in char.keys()])) )
	] )
	'''
	with open(charfile, 'w+') as outfile:
		#json.dump(data, outfile, indent=4, separators=(',', ': '))
		json.dump(char, outfile, indent=4)

		
	zipSave(savefile, charfile)
	
def zipSave(savefile, charfile):
	with zf.ZipFile(savefile, 'w') as save:
		save.write(charfile, os.path.basename(charfile))
		if os.path.isfile(fstruct.SKILLPICKLE):
			save.write(fstruct.SKILLPICKLE, os.path.basename(fstruct.SKILLPICKLE))
		if os.path.isfile(fstruct.FEATPICKLE):
			save.write(fstruct.FEATPICKLE, os.path.basename(fstruct.FEATPICKLE))
			
def loadChar(obj):
	opts = {}
	opts['filetypes'] = [('dnd files', '.dnd')]
	opts['defaultextension'] = '.dnd'
	opts['initialfile'] = fstruct.NAME
	opts['initialdir'] = fstruct.CPATH
	loadfile = tkf.askopenfilename(**opts)
	charfile = os.path.splitext(loadfile)[0]+".char"
	
	info = unzipLoad(loadfile, charfile)
	SetCharacterDict(obj, info)	
		
def unzipLoad(loadfile, charfile):
	with zf.ZipFile(loadfile, 'r') as loadf:
		return json.load(loadf.open(os.path.basename(charfile)))
		
			
def GetCharacterDict(obj):
	return OrderedDict( [
		("Player Name", obj.Names["PlayerName"].get()),
		("Character Name", obj.Names["CharName"].get()),
		("Class", obj.Class.get()), 
		("Race", obj.Race.get()),
		("Level", obj.level.get()),
		("Alignment", obj.align.get()),
		("Deity", obj.deity.get()),
		("Character Description", OrderedDict(zip([i for i in obj.charInfo], [obj.charInfo[i].get() for i in obj.charInfo.keys()])) ),
		("Abilities", OrderedDict(zip([i for i in obj.abil.keys()], [obj.abil[i].get() for i in obj.abil.keys()]))),
		("Initiative", OrderedDict(zip([i for i in obj.init.keys()], [obj.init[i].get() for i in obj.init.keys()]))),
		("HP", obj.hp.get()),
		("AC", OrderedDict(zip([i for i in obj.AC.keys()], [obj.AC[i].get() for i in obj.AC.keys()]))),
		("Speed", obj.speed.get()),
		("Saving Throws", OrderedDict([
			("Fortitude",OrderedDict(zip([i for i in obj.fsave.keys()], [obj.fsave[i].get() for i in obj.fsave.keys()]))),
			("Reflex",OrderedDict(zip([i for i in obj.rsave.keys()], [obj.rsave[i].get() for i in obj.rsave.keys()]))),
			("Will",OrderedDict(zip([i for i in obj.wsave.keys()], [obj.wsave[i].get() for i in obj.wsave.keys()]))),
		])),
		("Base Attack Bonus", obj.baseAtk.get()),
		("Grapple", OrderedDict(
			zip([i for i in obj.grapple.keys()], [obj.grapple[i].get() for i in obj.grapple.keys()]))
		),
		("Spell Resistance", obj.spellRes.get()),
		("Damage Reduction", obj.damagereduction.get()),
		("Languages", OrderedDict(zip(["Known", "Bonus"], [obj.Llang['text'].split('\n'), 
		obj.LbonusLNum['text'] ]))),
		("Special Abilities", obj.LspecialsL['text'].split('\n')),
		("miscellaneous", {
			"alignCMB": obj.CMBalign['values'], 
			"abilityCMB": obj.rollList,
			"rollVal": obj.rollval.get(),
			"unroll": obj.unrollDict,
			"languageCMB": obj.CMBlang['values'],
			#"traits": {zip([key for key in obj.traits.keys()],[obj.traits[key].get() for key in obj.traits.keys()])}
			"traits": OrderedDict(zip([key for key in obj.traits.keys()],[obj.traits[key].get() for key in obj.traits.keys()]))
		})	
	] )
	
	## possible alignments CMB
	## ability roller info, including list and CMBs
	## include available language CMB
	# allow proper changes in CMBs after load
	# race ability + -
	# way of checking how many languages selected out of total?
	# feat list when implemented
	# conditional modifiers when implemented
	
		
def SetCharacterDict(obj, valsDict):

	mydict =  setDict(obj)
	
	for key in valsDict.keys():
		mydict[key](valsDict[key])
			
		
def setDict(obj):
	return {
		"Player Name": lambda val: obj.Names["PlayerName"].set(val),
		"Character Name": lambda val: obj.Names["CharName"].set(val),
		"Class": lambda val: obj.Class.set(val), 
		"Race": lambda val: obj.Race.set(val),
		"Level": lambda val: obj.level.set(val),
		"Alignment": lambda val: obj.align.set(val),
		"Deity": lambda val: obj.deity.set(val),
		"Character Description": lambda subdict: [obj.charInfo[item].set(subdict[item]) for item in obj.charInfo.keys()],
		"Abilities": lambda subdict: [obj.abil[item].set(subdict[item]) for item in obj.abil.keys()],
		"Initiative": lambda subdict: [obj.init[item].set(subdict[item]) for item in obj.init.keys()],
		"HP": lambda val: obj.hp.set(val),
		"AC": lambda subdict: [obj.AC[item].set(subdict[item]) for item in obj.AC.keys()],
		"Speed": lambda val: obj.speed.set(val),
		"Saving Throws": lambda subdict: setSaves(obj, subdict),
		"Base Attack Bonus": lambda val: obj.baseAtk.set(val),
		"Grapple": lambda subdict: [obj.grapple[item].set(subdict[item]) for item in obj.grapple.keys()],
		"Spell Resistance": lambda val: obj.spellRes.set(val),
		"Damage Reduction": lambda val: obj.damagereduction.set(val),
		"Languages": lambda val: setLang(obj, val),
		"Special Abilities": lambda val: setSpecial(obj, val),
		"miscellaneous": lambda subdict: setMisc(obj, subdict)
	}


def setMisc(obj, miscDict):	
	for key in miscDict.keys():		
		if key == "alignCMB":
			obj.CMBalign['values'] =  miscDict[key]
		elif key == "rollVal":
			obj.rollval.set(str(miscDict[key]).lstrip('[').rstrip(',\']').replace(',', ' '))
		elif key == "unroll":
			obj.unrollDict = miscDict[key]
		elif key == "abilityCMB":
			obj.rollList = miscDict[key]
			for a in obj.abil.keys():
				obj.CMBabil[a]['values'] = miscDict[key]
		elif key == "languageCMB":
			obj.CMBlang['values'] = miscDict[key]
		elif key == "traits":
			for a in obj.abil.keys():
				obj.traits[a].set(miscDict[a])
				
				#from GUI
				#if key in self.char.traits.keys():
				#trait = int(self.char.traits[key])
				#self.abil[key].set(int(val) + trait)
				#self.Mabil[key].set((int(val) + trait - 10) /2)

def setSpecial(obj, val):
	obj.LspecialsL['text'] = '\n'.join(val)
	
def setLang(obj, languagesDict):
	obj.Llang['text'] = '\n'.join(languagesDict['Known'])
	obj.LbonusLNum['text'] = languagesDict['Bonus']

def setSaves(obj, savesdict):
	setDict = {
		"Will": lambda subdict: [obj.wsave[item].set(subdict[item]) for item in obj.wsave.keys()],
		"Fortitude": lambda subdict: [obj.fsave[item].set(subdict[item]) for item in obj.fsave.keys()],
		"Reflex": lambda subdict: [obj.rsave[item].set(subdict[item]) for item in obj.fsave.keys()]
	}
	
	for key in savesdict.keys():
		setDict[key](savesdict[key])