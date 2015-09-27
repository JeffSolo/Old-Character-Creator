#global file and folder names
import os 

SKILLPICKLE = ''
FEATPICKLE = ''
NAME = 'Kaladin'
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '\\Characters\\'
CPATH = os.path.dirname(os.path.realpath(__file__)) + '\\Characters\\' + NAME

def initializeFolders():
	makeCharacterDirectory()
	setSKILLP(CPATH)
	setFEATP(CPATH)

def makeCharacterDirectory(name=NAME, i=0):
	if not os.path.exists(BASEPATH):
		os.mkdir(BASEPATH)
	global CPATH
	CPATH = BASEPATH + name + '_' + str(i)
	if not os.path.exists(CPATH):
		os.mkdir(CPATH)
	else:
		i += 1
		makeCharacterDirectory(name, i)

def renameCharacterDirectory(newName):
	newPath = BASEPATH + newName
	if not os.path.exists(newPath):
		os.rename(CPATH, newPath)
		setCPATH(newPath)
	
def onNameChange(newName):
	renameCharacterDirectory(newName)
	setNAME(newName)
	setSKILLP(CPATH)
	setFEATP(CPATH)
	
def setCPATH(newpath):
	global CPATH
	CPATH = newpath
	
def setNAME(newname):
	global NAME
	NAME = newname
	
def setSKILLP(path=CPATH):
	global SKILLPICKLE
	SKILLPICKLE = CPATH + '\\skills.p'

def setFEATP(path=CPATH):
	global FEATPICKLE
	FEATPICKLE = CPATH + '\\feats.p'



