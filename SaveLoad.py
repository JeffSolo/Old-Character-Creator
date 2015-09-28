#saveload
import os, json
import zipfile as zf
import tkFileDialog as tkf
import filestructure as fstruct
from collections import OrderedDict

def saveChar(char):
	opts = {}
	opts['defaultextension'] ='.dnd'
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
		json.dump(char, outfile, indent=4, separators=('', ': '))

		
	zipSave(savefile, charfile)
	
def zipSave(savefile, charfile):
	with zf.ZipFile(savefile, 'w') as save:
		save.write(charfile, os.path.basename(charfile))
		if os.path.isfile(fstruct.SKILLPICKLE):
			save.write(fstruct.SKILLPICKLE, os.path.basename(fstruct.SKILLPICKLE))
		if os.path.isfile(fstruct.FEATPICKLE):
			save.write(fstruct.FEATPICKLE, os.path.basename(fstruct.FEATPICKLE))