from Tkinter import *
import tkFileDialog as tkf
import tkFont
import os, json, ttk
from collections import OrderedDict
import tkMessageBox as msg
import zipfile as zf
import AbilityRoller as roller
import filestructure as fstruct
import SaveLoad as sl
from Character import Character
from PopUp import PopUp
from Skills import Skills
from Spells import Spells
from feats import Feats
from time import sleep



class CharacterCreator(object):
	def __init__(self):
		self.root = Tk()
		self.makeCharacterDirectory = fstruct.initializeFolders()
		self.createVars()
		self.draw()
		
	def createVars(self):
		self.char = Character('','')
		self.Class = StringVar()
		self.Race =  StringVar()
		self.size =  StringVar()
		self.align = StringVar()
		self.deity = StringVar()
		self.hp =    StringVar()
		self.baseAtk=StringVar()
		self.spellRes=StringVar()
		self.Languages=StringVar() 
		self.damagereduction=StringVar()
		
		self.speed = IntVar()
		self.level = IntVar()
		self.level.set(1)
		
		self.LspecialsL = {}
		self.LspecialsL['text'] = ''
		
		self.Names = None
		self.Names = OrderedDict([
				("CharName", StringVar()),
				("PlayerName", StringVar())
		])
		
		self.charInfo = None
		self.charInfo = OrderedDict([
				('size',	StringVar()),
				('age',		StringVar()),
				('gender',	StringVar()),
		        ('height',	StringVar()),
		        ('weight',	StringVar()),
		        ('eyes', 	StringVar()),
		        ('hair',  	StringVar()),
		        ('skin',	StringVar())
		])
		
		abilityList = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
		AClist = ['total', 'size', 'armor', 'shield', 'nat', 'deflect', 'misc', 'touch', 'flat']
		
		self.abil={}
		self.Mabil={}
		self.CMBabil = {}
		self.Labilnote = {}
		self.AC = {}
		
		#self.speed.set('')
		for item in AClist:
			self.AC[item] = StringVar()

			
		self.init = {}
		self.init['total'] = StringVar()
		self.init['misc'] =  StringVar()
		for key in self.init.keys():
			self.init[key].set('')
		
		self.traits = {}
		for item in abilityList:
			self.traits[item] = StringVar()
			self.abil[item] = StringVar()
			self.Mabil[item] = StringVar()
			
		savesList = ['total', 'base', 'magic', 'misc']
		self.rsave, self.fsave, self.wsave = {}, {} ,{}
		for item in savesList:
			self.fsave[item] = StringVar()
			self.rsave[item] = StringVar()
			self.wsave[item] = StringVar()
		
		self.skillsP = None
		self.spellsP = None
		self.featsP = None
		
		self.unrollDict = {}
		self.rollList = []
		self.backupRollList = []
		self.rollval = StringVar()
		self.customRoll = BooleanVar()
		self.customRoll.set(False)
		
		self.languagelist = []
		self.langcount = 0
		
		self.grapple = {}
		self.grapple['total'] = StringVar()
		self.grapple['misc'] = StringVar()
		self.grapple['size'] = StringVar()
		
		#self.levelList = 1
		
		self.savesMods = StringVar()
		self.GetCharacterDict()
		
		#self.canLevel = False # do we meet the requirements to level up yet (set everything?)
				
	def GetCharacterDict(self):
		return OrderedDict( [
			("Player Name", self.Names["PlayerName"].get()),
			("Character Name", self.Names["CharName"].get()),
			("Class", self.Class.get()), 
			("Race", self.Race.get()),
			("Level", self.level.get()),
			("Alignment", self.align.get()),
			("Deity", self.deity.get()),
			("Character Description", OrderedDict(zip([i for i in self.charInfo], [self.charInfo[i].get() for i in self.charInfo.keys()])) ),
			("Abilities", OrderedDict(zip([i for i in self.abil.keys()], [self.abil[i].get() for i in self.abil.keys()]))),
			("Initiative", OrderedDict(zip([i for i in self.init.keys()], [self.init[i].get() for i in self.init.keys()]))),
			("HP", self.hp.get()),
			("AC", OrderedDict(zip([i for i in self.AC.keys()], [self.AC[i].get() for i in self.AC.keys()]))),
			("Speed", self.speed.get()),
			("Saving Throws", OrderedDict([
				("Fortitude",OrderedDict(zip([i for i in self.fsave.keys()], [self.fsave[i].get() for i in self.fsave.keys()]))),
				("Reflex",OrderedDict(zip([i for i in self.rsave.keys()], [self.rsave[i].get() for i in self.rsave.keys()]))),
				("Will",OrderedDict(zip([i for i in self.wsave.keys()], [self.wsave[i].get() for i in self.wsave.keys()]))),
			])),
			("Base Attack Bonus", self.baseAtk.get()),
			("Grapple", OrderedDict(zip([i for i in self.grapple.keys()], [self.grapple[i].get() for i in self.grapple.keys()]))),
			("Spell Resistance", self.spellRes.get()),
			("Damage Reduction", self.damagereduction.get()),
			("Languages", self.languagelist),
			("Special Abilities", self.LspecialsL['text'])
		] )
		'''
	def CharacterInfoList(self):
		return [
			self.Names
			self.Class
			self.Race
			self.level
			self.align
			self.deity
			self.charInfo
			self.abil
			self.init
			self.hp
			self.speed
			self.fsave
			self.rsave
			self.wsave
			self.baseAtk
			self.grapple
			self.spellRes
			self.damagereduction
			self.languagelist
			self.LspecialsL
			self.spellCaster
		]
		
	def SetCharDict(self):
		'''
	
	def draw(self):
		self.root.title("Character Creator")
		self.root.geometry("850x650")
		
		self.drawline1()
		self.drawline2()
		self.drawline3()
		self.separator1()
		self.drawAbilities(['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'])
		self.drawRoll()
		self.drawHP()
		self.drawAC()
		self.drawSpeed()
		self.drawInitiative()
		self.drawSaves()
		self.drawAttackBSpellR()
		self.separator2()
		self.drawGrapple()
		self.drawSkillsSpellsFeats()
		self.drawSpecialFeats()
		self.drawLanguages()
		self.drawSaveLoadCharacter()
		
		self.update()
		
	def drawline1(self):
		# Create First Line Objects
		self.LcharName = Label(self.root, text="Character Name:", relief=GROOVE, width=13, anchor=E)
		self.LplayerName = Label(self.root, text="Player Name:",  relief=GROOVE, width=12, anchor=E)
		self.EcharName = Entry(  self.root, width=36, textvariable=self.Names['CharName'])
		self.EplayerName = Entry(self.root, width=36, textvariable=self.Names['PlayerName']) 

		# Place Line 1 on Grid
		self.LcharName.grid(  row=0, column=0, columnspan=2, sticky=NSEW)
		self.EcharName.grid(  row=0, column=2, columnspan=6, sticky=NSEW)
		self.LplayerName.grid(row=0, column=8, columnspan=2, sticky=NSEW)
		self.EplayerName.grid(row=0, column=10, columnspan=6, sticky=NSEW)

	def drawline2(self):
		# Create Second Line Objects
		self.Lrace =  Label(self.root, width=6, relief=GROOVE, anchor=E, text="Race:") 
		self.Lclass = Label(self.root, width=6, relief=GROOVE, anchor=E, text="Class:")
		self.Lalign = Label(self.root, width=6, relief=GROOVE, anchor=E, text="Alignment:")
		self.Ldeity = Label(self.root, width=6, relief=GROOVE, anchor=E, text="Deity:")
		self.Llevel = Label(self.root, width=6, relief=GROOVE, anchor=E, text="Level:")
		self.CMBrace = ttk.Combobox( self.root, width=12, values=self.char.raceList, textvariable=self.Race)
		self.CMBclass = ttk.Combobox(self.root, width=12, values=self.char.classList, textvariable=self.Class)
		self.CMBalign = ttk.Combobox(self.root, width=18, values=self.char.align, textvariable=self.align)
		self.Edeity = Entry(self.root, width=12, textvariable=self.deity)
		
		self.Blevelup = Label(self.root, width=2, text="+", justify='center', relief='raised') # label that acts like button since button wouldn't fit here
		self.Elevel = Entry(self.root, width=4,textvariable=self.level, justify='center', state='disabled')

		# Place Line 2 on Grid
		self.Lclass.grid(  row=1, column=0, sticky=EW)
		self.CMBclass.grid(row=1, column=1, sticky=EW, columnspan=2)
		self.Llevel.grid(  row=1, column=3, sticky=EW)
		self.Blevelup.grid(row=1, column=4,sticky=E,padx=(0,2))
		self.Elevel.grid(  row=1, column=4,sticky=W)
		self.Lrace.grid(   row=1, column=5, sticky=EW)
		self.CMBrace.grid( row=1, column=6, sticky=EW, columnspan=2)
		self.Lalign.grid(  row=1, column=8, sticky=EW,columnspan=2)
		self.CMBalign.grid(row=1, column=10,sticky=EW, columnspan=3)
		self.Ldeity.grid(  row=1, column=13,sticky=EW,)
		self.Edeity.grid(  row=1, column=14,sticky=EW, columnspan=2)
		
	def updateline2(self):
		self.CMBalign['values'] = self.char.align

	def drawline3(self):
		#Create Third Line Objects
		L, E = {}, {}
		for i, label in enumerate(self.charInfo.keys()):
			L[label] = Label(self.root, relief=GROOVE, anchor='e', width=6, text=label.capitalize()+":")
			E[label] = Entry(self.root, width=6, textvariable=self.charInfo[label],justify='center')
			
			L[label].grid(row=2, column=i*2, sticky=EW)
			E[label].grid(row=2, column=i*2+1, sticky=EW)
			
		E['size']['state'] = 'disabled'

	def updateline3(self):
		self.charInfo['size'] = self.char.size
		
	def separator1(self):
		#Create blank space on grid
		self.Fempty = Frame(self.root, height=20, width=5)
		self.Fempty.grid(row=3,column=0,columnspan=16, sticky=NSEW)
		
	def drawAbilities(self, abilityList):
		EabilMod = {}
		Babil = {}

		for i, item in enumerate(abilityList):
			Babil[item] = Button(self.root, text=item, relief=GROOVE, anchor=E, width=4) # command=PopUp().Bstr???
			
			self.CMBabil[item] = ttk.Combobox(self.root, width=4, state='readonly', textvariable=self.abil[item])
			EabilMod[item] = Entry(self.root, width=3, state=DISABLED, textvariable=self.Mabil[item])
			self.Labilnote[item] = Label(self.root, width=6, textvariable=self.traits[item])
			
			Babil[item].grid(row=i+4, column=0, sticky=E)
			self.CMBabil[item].grid(row=i+4,column=1, sticky=W)
			EabilMod[item].grid(row=i+4,column=2, sticky=W)
			self.Labilnote[item].grid(row=i+4,column=3, sticky=EW)
		
	
	def drawRoll(self):
		# Create and Place Roll button
		self.Broll = Button(self.root, text="Roll Abilities", command=self.autoRoll)
		self.Broll.grid(row=10, column=0, columnspan=2)		
		self.BrollDefault = Button(self.root, text="Default", width=6, command=self.defaultRoll)
		self.BrollDefault.grid(row=10, column=2)
		self.CBcustom = Checkbutton(self.root, text='Custom', variable=self.customRoll, command=self.customRollToggle)
		self.CBcustom.grid(row=10, column=3)
		self.roll = Label(self.root, width=18, state=DISABLED, textvariable=self.rollval)
		self.roll.grid(row=11, column=0, columnspan=3)
	
	
	def drawHP(self):
		self.Bhp = Button(self.root, relief=GROOVE, anchor=E, text="HP", command=PopUp().Bhp)
		self.Ehp = Entry(self.root, state=DISABLED, width=4, justify=CENTER, textvariable=self.hp)
		self.Bhp.grid(row=4, column=4, sticky=E)
		self.Ehp.grid(row=4, column=5, sticky=W+N+S)
	
	def drawAC(self):
		Lacplus = {}
		Lac = {}
		Bac = Button(self.root, relief=GROOVE, anchor=E, text="AC")
		self.Eac = Entry(self.root, state=DISABLED, width=4, justify=CENTER, textvariable=self.AC['total'])
		Lac1 = Label(self.root, text="=")
		Lacten = Label(self.root, text="  10 ")
		Lacplus1 = Label(self.root, text=" +   ")
		
		for i in range(2,8):
			Lacplus[i] = Label(self.root, text="+")
			Lacplus[i].grid(row=5, column=i+5, sticky=E)
	
		self.Eac2 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['armor'])
		self.Eac3 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['shield'])
		self.Eac4 = Entry(self.root, justify=CENTER, width=4, state=DISABLED, textvariable=self.Mabil['DEX'])
		self.Eac5 = Entry(self.root, justify=CENTER, width=4, state=DISABLED, textvariable=self.AC['size'])
		self.Eac6 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['nat'])
		self.Eac7 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['deflect'])
		self.Eac8 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['misc'])

		Bac.grid( row=5, column=4, sticky=E)
		self.Eac.grid( row=5, column=5, sticky=W+N+S)
		Lac1.grid(row=5, column=5, sticky=E)
		Lacten.grid(row=5, column=6, sticky=W)
		Lacplus1.grid(row=5, column=6, sticky=E)
		self.Eac2.grid(row=5, column=7, sticky=W)
		#Lacplus2.grid(row=5, column=7, sticky=E)
		self.Eac3.grid(row=5, column=8, sticky=W)
		#Lacplus3.grid(row=5,column=8, sticky=E)
		self.Eac4.grid(row=5, column=9, sticky=W)
		#Lacplus4.grid(row=5,column=9, sticky=E)
		self.Eac5.grid(row=5, column=10, sticky=W)
		#Lacplus5.grid(row=5,column=10, sticky=E)
		self.Eac6.grid(row=5, column=11, sticky=W)
		#Lacplus6.grid(row=5,column=11, sticky=E)
		self.Eac7.grid(row=5, column=12, sticky=W)
		#Lacplus7.grid(row=5,column=12, sticky=E)
		self.Eac8.grid(row=5, column=13, sticky=W)
		
		textList = ["Armor\nBonus", "Shield\nBonus", "Dex\nModifier", "Size\nModifier", "Natural\nArmor", "Deflection\nModifier","Misc\nModifier"]
		for i in range(2,9):
			Lac[i] = Label(self.root, font=('TkDefaultFont', 6), text=textList[i-2])
			Lac[i].grid(row=6, column=i+5, sticky=W)

		
		self.BtouchAC = Button(self.root, relief=GROOVE, anchor=E, text="Touch AC")
		self.EtouchAC = Entry( self.root, width=6, state=DISABLED, textvariable=self.AC['touch'])
		self.BflatAC = Button( self.root, relief=GROOVE, anchor=E, text="Flat-Footed")
		self.EflatAC = Entry(  self.root, width=6, state=DISABLED, textvariable=self.AC['flat'])
		
		self.BtouchAC.grid(row=7, column=4, columnspan=2, sticky=E)
		self.EtouchAC.grid(row=7, column=6, sticky=N+S+W)
		self.BflatAC.grid( row=7, column=7, columnspan=2, sticky=E)
		self.EflatAC.grid( row=7, column=9, sticky=N+S+W)
		
		self.Bdamred = Button(self.root, relief=GROOVE, anchor=E, text="Damage Reduction")
		self.Ldamred = Entry(self.root, width=12, textvariable=self.damagereduction)
		
		self.Bdamred.grid(row=7, column=11, columnspan=3, sticky=E)
		self.Ldamred.grid(row=7, column=14, columnspan=2, sticky=NSEW)
	
	def drawSpeed(self):
		self.Bspeed = Button(self.root, relief=GROOVE, anchor=E, text="Speed")
		self.Espeed = Entry(self.root, state=DISABLED, width=6, justify=CENTER, textvariable=self.speed)
		self.Bspeed.grid(row=4, column=7, sticky=EW)
		self.Espeed.grid(row=4, column=8, sticky=NSEW)
		
	def drawInitiative(self):
		self.Binit = Button(self.root, relief=GROOVE, anchor=E, text="Initiative")
		self.Einit = Entry(self.root, state=DISABLED, width=5, justify=CENTER, textvariable=self.init['total'])
		self.Liniteq = Label(self.root, text="=")
		self.Linitplus = Label(self.root, text="+")
		self.EinitDex = Entry(self.root, state=DISABLED, width=4, relief=GROOVE, justify=CENTER, textvariable=self.Mabil['DEX'])
		self.EinitMisc = Entry(self.root, width=4, justify=CENTER, textvariable=self.init['misc'])
		self.Linit1 = Label(self.root, font=('TkDefaultFont', 6), text="   Total\n")
		self.Linit2 = Label(self.root, font=('TkDefaultFont', 6), text="Dex\nModifier")
		self.Linit3 = Label(self.root, font=('TkDefaultFont', 6), text="Misc\nModifier")
		
		self.Binit.grid(row=9, column=4, columnspan=2, sticky=E)
		self.Einit.grid(row=9, column=6, sticky=W+S+N)
		self.Liniteq.grid(row=9, column=6, sticky=E)
		self.EinitDex.grid(row=9, column=7, sticky=W+N+S)
		self.Linitplus.grid(row=9, column=7, sticky=E+N+S)
		self.EinitMisc.grid(row=9, column=8, sticky=W+N+S)
		self.Linit1.grid(row=10, column=6, sticky=W)
		self.Linit2.grid(row=10, column=7, sticky=W)
		self.Linit3.grid(row=10, column=8, sticky=W)
		
	def drawSaves(self):
		self.Lsaves   = Label(self.root, font=('TkDefaultFont', 8), text="Saving Throws  ")
		self.Lsttotal = Label(self.root, font=('TkDefaultFont', 8), text="  Total")
		self.Lstbase  = Label(self.root, font=('TkDefaultFont', 6), text="Base\nSave")
		self.Lstabil  = Label(self.root, font=('TkDefaultFont', 6), text="Ability\nModifier")
		self.Lstmagic = Label(self.root, font=('TkDefaultFont', 6), text="Magic\nModifier")
		self.Lstmisc  = Label(self.root, font=('TkDefaultFont', 6), text="Misc\nModifier")
		
		self.Bfort   = Button(self.root, relief=GROOVE, width=12, text="Fortitude (CON)")
		self.Eftotal = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.fsave['total'])
		self.Lfeq    = Label(self.root, text="=")
		self.Efbase  = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.fsave['base'])
		self.Lfplus1 = Label(self.root, text="+")
		self.Efabilm = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.Mabil['CON'])
		self.Lfplus2 = Label(self.root, text="+")
		self.Efmagic = Entry(self.root, width=4, justify=CENTER, textvariable=self.fsave['magic'])
		self.Lfplus3 = Label(self.root, text="+")
		self.Efmisc  = Entry(self.root, width=4, justify=CENTER, textvariable=self.fsave['misc'])
		
		self.Breflex = Button(self.root, relief=GROOVE, width=12, text="Reflex      (DEX)")
		self.Ertotal = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.rsave['total'])
		self.Lreq = Label(self.root, text="=")
		self.Erbase = Entry(self.root, width=4, justify=CENTER,  state=DISABLED, textvariable=self.rsave['base'])
		self.Lrplus1 = Label(self.root, text="+")
		self.Erabilm = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.Mabil['DEX'])
		self.Lrplus2 = Label(self.root, text="+")
		self.Ermagic = Entry(self.root, width=4, justify=CENTER, textvariable=self.rsave['magic'])
		self.Lrplus3 = Label(self.root, text="+")
		self.Ermisc = Entry(self.root, width=4, justify=CENTER, textvariable=self.rsave['misc'])

		self.Bwill = Button(self.root, relief=GROOVE, width=12, text="  Will        (WIS)")
		self.Ewtotal = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.wsave['total'])
		self.Lweq = Label(self.root, text="=")
		self.Ewbase = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.wsave['base'])
		self.Lwplus1 = Label(self.root, text="+")
		self.Ewabilm = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.Mabil['WIS'])
		self.Lwplus2 = Label(self.root, text="+")
		self.Ewmagic = Entry(self.root, width=4, justify=CENTER, textvariable=self.wsave['magic'])
		self.Lwplus3 = Label(self.root, text="+")
		self.Ewmisc = Entry(self.root, width=4, justify=CENTER, textvariable=self.wsave['misc'])
		
		self.Lsaves.grid(  row=12, column=0, columnspan=3, sticky=E)  
		self.Lsttotal.grid(row=12, column=3, sticky=W)
		self.Lstbase.grid( row=12, column=4) 
		self.Lstabil.grid( row=12, column=5, sticky=W) 
		self.Lstmagic.grid(row=12, column=6, sticky=W)
		self.Lstmisc.grid( row=12, column=7, sticky=W) 
		
		self.Bfort.grid(  row=13, column=0, columnspan=3, sticky=E) 
		self.Eftotal.grid(row=13, column=3)
		self.Lfeq.grid(   row=13, column=3, columnspan=2)   
		self.Efbase.grid( row=13, column=4) 
		self.Lfplus1.grid(row=13, column=4, sticky=E)
		self.Efabilm.grid(row=13, column=5, sticky=W)
		self.Lfplus2.grid(row=13, column=5, sticky=E)
		self.Efmagic.grid(row=13, column=6, sticky=W)
		self.Lfplus3.grid(row=13, column=6, sticky=E)
		self.Efmisc.grid( row=13, column=7, sticky=W)
		
		self.Breflex.grid(  row=14, column=0, columnspan=3, sticky=E) 
		self.Ertotal.grid(row=14, column=3)
		self.Lreq.grid(   row=14, column=3, columnspan=2)   
		self.Erbase.grid( row=14, column=4) 
		self.Lrplus1.grid(row=14, column=4, sticky=E)
		self.Erabilm.grid(row=14, column=5, sticky=W)
		self.Lrplus2.grid(row=14, column=5, sticky=E)
		self.Ermagic.grid(row=14, column=6, sticky=W)
		self.Lrplus3.grid(row=14, column=6, sticky=E)
		self.Ermisc.grid( row=14, column=7, sticky=W)
		
		self.Bwill.grid(  row=15, column=0, columnspan=3, sticky=E) 
		self.Ewtotal.grid(row=15, column=3)
		self.Lweq.grid(   row=15, column=3, columnspan=2)   
		self.Ewbase.grid( row=15, column=4) 
		self.Lwplus1.grid(row=15, column=4, sticky=E)
		self.Ewabilm.grid(row=15, column=5, sticky=W)
		self.Lwplus2.grid(row=15, column=5, sticky=E)
		self.Ewmagic.grid(row=15, column=6, sticky=W)
		self.Lwplus3.grid(row=15, column=6, sticky=E)
		self.Ewmisc.grid( row=15, column=7, sticky=W)
		
		self.LsavesCond = Label(self.root, textvariable=self.savesMods)
		self.LsavesCond.grid(row=16, column=1, columnspan=8, rowspan=2)
		
	def drawAttackBSpellR(self):
		self.BbaseAtk =     Button(self.root, relief=GROOVE, width=14, text="Base Attack Bonus")
		self.BspellResist = Button(self.root, relief=GROOVE, width=12, text="Spell Resistance")
		self.EbaseAtk =     Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.baseAtk)
		self.EspellResist = Entry(self.root, width=4, justify=CENTER, textvariable=self.spellRes)
		
		self.BbaseAtk.grid(row=19, column=0, columnspan=3, sticky=E)
		self.EbaseAtk.grid(row=19, column=3)
		self.BspellResist.grid(row=19, column=4, columnspan=2)
		self.EspellResist.grid(row=19, column=6, sticky=W)
		
	def separator2(self):
		#Create blank space on grid
		self.Fempty2 = Frame(self.root, height=20)
		self.Fempty2.grid(row=20,column=0,columnspan=10, sticky = E+W)
		
	def drawGrapple(self):
		self.Bgrapple = Button(self.root, relief=GROOVE, width=6, text="Grapple")
		self.EgrapTotal = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.grapple['total'])
		self.EgrapBaseA = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.baseAtk)
		self.EgrapStr   = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.Mabil['STR'])
		self.EgrapSize  = Entry(self.root, width=4, justify=CENTER, state=DISABLED, textvariable=self.grapple['size'])
		self.EgrapMisc  = Entry(self.root, width=4, justify=CENTER, textvariable=self.grapple['misc'])
		self.LgEq = Label(self.root, text='=')
		self.LgPlus1 = Label(self.root, text='+  ')
		self.LgPlus2 = Label(self.root, text='+')
		self.LgPlus3 = Label(self.root, text='+ ')
		
		self.Bgrapple.grid(  row=21, column=0, columnspan=2, sticky=E)
		self.EgrapTotal.grid(row=21, column=2)
		self.LgEq.grid(      row=21, column=2, columnspan=2)
		self.EgrapBaseA.grid(row=21, column=3)
		self.LgPlus1.grid(   row=21, column=3, columnspan=2)
		self.EgrapStr.grid(  row=21, column=4)
		self.LgPlus2.grid(   row=21, column=4, columnspan=2)
		self.EgrapSize.grid( row=21, column=5, sticky=W)
		self.LgPlus3.grid(   row=21, column=5, sticky=E)
		self.EgrapMisc.grid( row=21, column=6, sticky=W)
		
		self.LgTotal = Label(self.root, font=('TkDefaultFont', 8), text="  Total  ")
		self.LgBaseA = Label(self.root, font=('TkDefaultFont', 6), text="Base\nAttack")
		self.LgStr  =  Label(self.root, font=('TkDefaultFont', 6), text="Strength\nModifier")
		self.LgSize  = Label(self.root, font=('TkDefaultFont', 6), text="Size\nModifier")
		self.LgMisc =   Label(self.root, font=('TkDefaultFont', 6), text="Misc\nModifier")
		
		self.LgTotal.grid(row=22, column=2)
		self.LgBaseA.grid(row=22, column=3)
		self.LgStr.grid(  row=22, column=4)
		self.LgSize.grid( row=22, column=5, sticky=W)
		self.LgMisc.grid( row=22, column=6, sticky=W)
		
	def drawSkillsSpellsFeats(self):
		self.Bfeats = Button(self.root, text="Select Feats", state=DISABLED, command=self.featsPage)
		self.Bfeats.grid(row=9, column=10, columnspan=2)
		self.Bskills = Button(self.root, text="Select Skills", state=DISABLED, command=self.skillsPage)
		self.Bspells= Button(self.root, text="Select Spells", state=DISABLED, command=self.spellsPage)
		self.Bskills.grid(row=9, column=12, columnspan=2)
		self.Bspells.grid(row=9,column=14, columnspan=2)
		
	def drawSpecialFeats(self):
		self.BfeatsL = Label(self.root, relief=FLAT, text="Feats: ")
		self.BspecialsL = Button(self.root, relief=FLAT, text="Special Abilities: ")
		self.LfeatsL = Label(self.root, text="Feat List")
		self.LspecialsL = Label(self.root)

		self.BfeatsL.grid(row=10, column=10, columnspan=3)
		self.BspecialsL.grid(row=10, column=13, columnspan=3)
		self.LfeatsL.grid(row=11, column=10, columnspan=3, rowspan=10, sticky=N)
		self.LspecialsL.grid(row=11, column=13, columnspan=3, rowspan=10, sticky=N)
	
	def drawLanguages(self):
		self.Blang = Button(self.root, width=10, relief=GROOVE, text="Languages")
		self.CMBlang = ttk.Combobox(self.root, width=10, values=self.char.bonusLang, textvariable=self.Languages)
		self.BresetLang = Button(self.root, width=6, text="Reset", command=self.resetLanguages)
		self.Llang = Label(self.root)
		self.LbonusLNum = Label(self.root, width=10, text="Bonus Lang: 0")
		
		self.Blang.grid(row=19, column=7, columnspan=2, sticky=E+W)
		self.LbonusLNum.grid(row=20, column=7, columnspan=2)
		self.CMBlang.grid(row=21, column=7, columnspan=2, sticky=E+W)
		self.Llang.grid(row=22, column=7, columnspan=2, rowspan=7)
		self.BresetLang.grid(row=29, column=7, columnspan=2)
	
	def drawSaveLoadCharacter(self):
		BsaveCharacter = Button(self.root, text="Save Character", command= lambda: sl.saveChar(self))
		BloadCharacter = Button(self.root, text="Load Character", command= lambda: self.loadChar())
		
		BsaveCharacter.grid(row=20, column=12, columnspan=2)
		BloadCharacter.grid(row=22, column=12, columnspan=2)
	
	def skillsPage(self):
		PopUp().warn("Skills", "Changing Class, Race, or Intelligence may cause you to lose all Skill information.")
		if not self.skillsP:
			self.skPage = Toplevel(self.root)
			self.skillsP = Skills(self.skPage, self.Mabil, self.char)
		else:
			self.skillsP.deiconify()
			
	def spellsPage(self):
		if not self.spellsP:
			self.spellsP = Toplevel(self.root)
			Spells(self.spellsP)
		else:
			self.spellsP.deiconify()
			
	def featsPage(self):
		if not self.featsP:
			self.featsP = Toplevel(self.root)
			Feats(self.featsP)
	
	def defaultRoll(self):
		self.rollList=[10, 12, 14, 14, 16, 18]
		self.onRoll()
		
	def autoRoll(self):
		self.rollList = roller.roll(1, 1, 1)
		self.onRoll()
		
	def customRollToggle(self):
		self.rollList = []
		self.onRoll()
		if self.customRoll.get():
			self.Broll['state'] = 'disabled'
			self.BrollDefault['state'] = 'disabled'
			for abil in self.CMBabil.keys():
				self.CMBabil[abil]['state'] = 'normal'
				
		else:
			self.Broll['state'] = 'normal'
			self.BrollDefault['state'] = 'normal'
			for abil in self.CMBabil.keys():
				self.CMBabil[abil]['state'] = 'readonly'
				
		
	def onRoll(self):
		self.rollList.append('')
		self.rollList.sort()
		self.backupRollList = list(self.rollList)
		self.rollval.set(str(self.rollList).lstrip('[').rstrip(',\']').replace(',', ' '))
		self.resetAbil()
		for key in self.CMBabil.keys():
			self.CMBabil[key]['values'] = self.rollList
		#else:
		#	PopUp().warn("Abilities", "Please select class and race before altering abilities")
			
	def resetAbil(self):
		if self.Class != '' and self.Race != '':
			# empties abilities
			for key in self.abil.keys():
				self.abil[key].set('')
			for key in self.Mabil.keys():
				self.Mabil[key].set('')
			# resets combobox lists - unnecessarry?
			self.unrollDict.clear()
			self.unrollDict = {}
			#remake combobox values
			self.rollList = list(self.backupRollList)
			for keyval in self.CMBabil.keys():
				self.CMBabil[keyval]['values'] = self.rollList

	def update(self):
		self.root.focus_set()
		self.setbind()
		self.root.mainloop()
		
	def resetLanguages(self):
		self.langcount = 0
		self.CMBlang['values'] = self.char.bonusLang
		if self.char.language:
			self.Llang['text'] = "\n".join(self.char.language)
		
	def updateLanguages(self, *args):
		if self.Mabil['INT'].get() != '' and self.langcount < int(self.Mabil['INT'].get()):
			self.languagelist = list(self.char.bonusLang)
			self.Llang['text'] = self.Llang['text'] + '\n' + self.Languages.get()
			self.languagelist.pop(self.languagelist.index(self.Languages.get()))
			self.Languages.set('')
			self.CMBlang['values'] = self.languagelist
			self.langcount += 1
	
	def updateAbilities(self, event, key):
		#print event.type # 10 is leave, 2 is RETURN, 35 is comobox selected
		if key:
			val = self.abil[key].get()
		else:
			return

		trait = 0 # racial ability bonus
		if key in self.char.traits.keys():
			trait = int(self.char.traits[key])
					
		if not self.customRoll.get() and (event.type == '35' or event.type == '4'):
			if val.isdigit():
					
					# lets you reselect a value without first setting to ''
					if event.type == '4':
						if key in self.unrollDict.keys():
							self.pushAbilList(key)
					
					else:
						# removes from combobox and set modifier (with any racial bonus or detriment)
						self.popAbilList(key, val)
						self.abil[key].set(int(val) + trait)
			else:
				self.pushAbilList(key)
				
		
		self.updateAbilMod(key)
	
		if key == 'CON':
			self.updateHP()
			self.updateSaves()
		if key == 'DEX':
			self.updateAC()
			self.updateSaves()
			self.updateInit()
		if key == 'WIS':
			self.updateSaves()
		if key == 'STR':
			self.updateGrapple()
		if key == "INT":
			self.LbonusLNum['text'] = "Bonus Lang: " + self.Mabil[key].get()
			self.resetLanguages()
			self.resetSkillsPage()
		
	def updateAbilMod(self, key):
		if self.abil[key].get().isdigit():
			self.Mabil[key].set((int(self.abil[key].get()) - 10) /2)
	
	def popAbilList(self, key, val):
		self.unrollDict[key] = self.rollList.pop(self.rollList.index(int(val)))
		for keyval in self.CMBabil.keys():
			if keyval != key:
				self.CMBabil[keyval]['values'] = self.rollList
		
	def pushAbilList(self, key):
		# check if we have popped an abilibute number for the abilibute
		if key in self.unrollDict:
			self.rollList.append(self.unrollDict[key])  #put it back in selection list
			self.rollList.sort()
			del self.unrollDict[key]
			for keyval in self.CMBabil.keys():
				self.CMBabil[keyval]['values'] = self.rollList
	
	def setbind(self):
		self.CMBrace.bind("<<ComboboxSelected>>", self.raceSelect)
		self.CMBclass.bind("<<ComboboxSelected>>", self.classSelect)
		self.CMBlang.bind("<<ComboboxSelected>>", self.updateLanguages)
		self.EcharName.bind("<FocusOut>", self.nameChange)
		self.EcharName.bind("<Return>", self.nameChange)
		self.EcharName.bind("<Leave>", self.nameChange)
		self.miscBind()
		self.acBind()
		self.abilBind()
		self.levelupBind()

	def miscBind(self):
		self.EinitMisc.bind("<KeyRelease>", self.updateInit)
		self.EgrapMisc.bind("<KeyRelease>", self.updateGrapple)
		self.Efmagic.bind("<KeyRelease>", self.updateSaves)
		self.Efmisc.bind("<KeyRelease>", self.updateSaves)
		self.Ermagic.bind("<KeyRelease>", self.updateSaves)
		self.Ermisc.bind("<KeyRelease>", self.updateSaves)
		self.Ewmagic.bind("<KeyRelease>", self.updateSaves)
		self.Ewmisc.bind("<KeyRelease>", self.updateSaves)
	
	def abilBind(self):
		for abil in self.CMBabil.keys():
			self.CMBabil[abil].bind("<<ComboboxSelected>>", self.makeLambda(abil))
			self.CMBabil[abil].bind("<Button-1>", self.makeLambda(abil))
			self.CMBabil[abil].bind("<FocusOut>", self.makeLambda(abil))
			self.CMBabil[abil].bind("<KeyRelease>", self.makeLambda(abil))
			
		
	def makeLambda(self, skill):
		return lambda event: self.updateAbilities(event, skill)

	def levelupBind(self):
		self.Blevelup.bind("<Button-1>",self.buttonclick)
		self.Blevelup.bind("<ButtonRelease-1>", self.buttonrelease)
	
	def buttonclick(self, event):
		self.Blevelup['relief'] = 'sunken'
		
	def buttonrelease(self, event):
		self.Blevelup['relief'] = 'raised'
		self.levelUp()
		
	def acBind(self):
		self.Eac2.bind("<KeyRelease>", self.updateAC)
		self.Eac3.bind("<KeyRelease>", self.updateAC)
		self.Eac6.bind("<KeyRelease>", self.updateAC)
		self.Eac7.bind("<KeyRelease>", self.updateAC)
		self.Eac8.bind("<KeyRelease>", self.updateAC)
	
	def updateAC(self, *args):
		total = 10
		touch = 10
		flat  = 10
		for key in self.AC.keys():
			test = self.AC[key].get()
			if test.isdigit() and key != 'total' and key != 'touch' and key != 'flat':
				total += int(test)
				if test.isdigit() and key != 'shield' and key != 'armor' and key != 'nat':
					touch += int(test)
				flat += int(test)
		if self.Mabil['DEX'].get():
			total += int(self.Mabil['DEX'].get())
			touch += int(self.Mabil['DEX'].get())
		self.AC['total'].set(str(total))
		self.AC['touch'].set(str(touch))
		self.AC['flat'].set(str(flat))
	
	def updateHP(self):
		con = self.Mabil['CON'].get()
		if con.isdigit() and self.hp.get():
			self.hp.set(int(self.char.hitDie) + int(con))
			
	def updateInit(self, event=None):
		total = 0
		if self.Mabil['DEX'].get():
			total += int(self.Mabil['DEX'].get())
		if self.init['misc'].get().isdigit():
			self.init['misc'].get()
			total += int(self.init['misc'].get())
		self.init['total'].set(str(total))
			
	def updateGrapple(self, *event):
		# calculate grapple
		total = 0
		if self.baseAtk.get():
			total += int(self.baseAtk.get())
		if self.Mabil['STR'].get():
			total += int(self.Mabil['STR'].get())

		for key in self.grapple.keys():
			if key != 'total' and self.grapple[key].get():
				total += int(self.grapple[key].get())
		
		self.grapple['total'].set(total)
		
	def updateSaves(self, *event):
		#calculate fort save total
		total = 0
		for key in self.fsave.keys():
			temp = self.fsave[key].get()
			if temp and key != 'total':
				total += int(temp)
		if self.Mabil['CON'].get():
			total += int(self.Mabil['CON'].get())
		self.fsave['total'].set(total) 
		
		#calculate reflex save total
		total = 0
		for key in self.rsave.keys():
			temp = self.rsave[key].get()
			if temp and key != 'total':
				total += int(temp)
		if self.Mabil['DEX'].get():
			total += int(self.Mabil['DEX'].get())
		self.rsave['total'].set(total)
		
		#calculate will save total
		total = 0
		for key in self.wsave.keys():
			temp = self.wsave[key].get()
			if temp and key != 'total':
				total += int(temp)
		if self.Mabil['WIS'].get():
			total += int(self.Mabil['WIS'].get())
		self.wsave['total'].set(total)
		
	def raceSelect(self, *args):
		self.remakeClass()
		# set size if it iexists
		if self.char.size:
			self.charInfo['size'].set(self.char.size)
		else:
			self.charInfo['size'].set('')
		
		if self.char.speed:
			self.speed.set(self.char.speed)
		else:
			self.speed.set('')
		
		self.AC['size'].set(self.char.ACsize)
		self.resetAbil()
		#remove any ability notes from other races
		for key in self.Labilnote.keys():
			self.traits[key].set('')
		# add ability notes
		for key in self.char.traits:
			self.traits[key].set(str(self.char.traits[key]) + " (Race)")
			
		self.grapple['size'].set(self.char.grappleMod)
		self.savesMods.set('\n'.join(self.char.savesConditions))
		
		self.updateAC()
		self.updateline3
		self.updateGrapple()
		self.resetLanguages()
		self.resetSkillsPage()
		self.update()
		
	def classSelect(self, *args):
		self.remakeClass()
		self.align.set('')
		# set HP
		self.LspecialsL['text'] = "\n".join(self.char.special)
		if self.char.spellCaster:
			self.Bspells['state'] = 'normal'
		else:
			self.Bspells['state'] = 'disabled'
		if self.char.hitDie:
			self.hp.set(self.char.hitDie)
		
		self.Bfeats['state'] = 'normal'
		self.Bskills['state'] = 'normal'
		self.fsave['base'].set(self.char.cfortSave)
		self.rsave['base'].set(self.char.crefSave)
		self.wsave['base'].set(self.char.cwillSave)
		self.baseAtk.set(str(self.char.atkBonus))
		self.updateHP()
		self.updateSaves()
		self.updateline2()
		self.updateGrapple()
		#self.resetAbil()
		self.resetSkillsPage()
			
	def remakeClass(self):
		del self.char
		self.char = Character(self.Race.get(), self.Class.get())	
		
	def resetSkillsPage(self):
		if os.path.isfile(fstruct.SKILLPICKLE):
			os.remove(fstruct.SKILLPICKLE)
	
	def nameChange(self, *args):
		name = self.Names['CharName'].get()
		# currently changes regardless of if name already exists
		fstruct.onNameChange(name)	

	def loadChar(self):

		sl.loadChar(self)
		self.remakeClass()
		for key in self.abil.keys():
			self.updateAbilities(None,key)
		sl.getSkills()
		
		
	def clickd(self, *args):
		if self.char.size:
			self.charInfo['size'].set(self.char.size)
		#self.draw
		
	def levelUp(self):
		def canLevel():
			pass
		
		#if canLevel():
		#	pass