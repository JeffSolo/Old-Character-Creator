from Tkinter import *
import ttk
import tkMessageBox as msg
import AbilityRoller as roller
from Character import Character
from PopUp import PopUp
from Skills import Skills
from Spells import Spells
from feats import Feats

class CharacterCreator(object):
	def __init__(self):
		self.root = Tk()
		self.createVars()
		self.draw()
		
	def createVars(self):
		self.char = Character('','')
		self.cClass =StringVar()
		self.Race =  StringVar()
		self.size =  StringVar()
		self.align = StringVar()
		self.hp =    StringVar()
		self.baseAtk=StringVar()
		self.spellRes= StringVar()
		self.Languages = StringVar()
		self.speed = IntVar()
		
		self.Abilities = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
		self.abil={}
		
		self.Mabil={}
		self.CMBabil = {}
		self.Labilnote = {}
		self.AC = {}
		
		self.speed.set('')
		self.AC['total']=   StringVar()
		self.AC['size'] =   StringVar()
		self.AC['armor'] =  StringVar()
		self.AC['shield'] = StringVar()
		self.AC['nat'] =    StringVar()
		self.AC['deflect'] =StringVar()
		self.AC['misc'] =   StringVar()
		self.AC['touch'] =  StringVar()
		self.AC['flat'] =   StringVar()
		for key in self.AC.keys():
			self.AC[key].set('')
				
		self.init = {}
		self.init['total'] = StringVar()
		self.init['misc'] =  StringVar()
		for key in self.init.keys():
			self.init[key].set('')
		
		self.traits = {}
		for item in self.Abilities:
			self.traits[item] = StringVar()
			self.abil[item] = StringVar()
			self.Mabil[item] = StringVar()
			
		self.rsave, self.fsave, self.wsave = {}, {} ,{}
		self.fsave['total'] = StringVar()
		self.fsave['base'] =  StringVar()
		self.fsave['magic'] = StringVar()
		self.fsave['misc'] =  StringVar()
		self.rsave['total'] = StringVar()
		self.rsave['base'] =  StringVar()
		self.rsave['magic'] = StringVar()
		self.rsave['misc'] =  StringVar()
		self.wsave['total'] = StringVar()
		self.wsave['base'] =  StringVar()
		self.wsave['magic'] = StringVar()
		self.wsave['misc'] =  StringVar()
		#for key in self.fsave.keys():
		#	self.fsave[key].set('')
		#for key in self.rsave.keys():
		#	self.rsave[key].set('')
		#for key in self.wsave.keys():
		#	self.wsave[key].set('')	
		self.skillsP = None
		self.spellsP = None
		self.featsP = None
		
		self.rollList = []
		self.languagelist = []
		self.unrollDict = {}
		self.backupRollList = []
		
		self.langcount = 0
		#for key in self.abil.keys():
		#	self.abil[key].set('')
		#for key in self.Mabil.keys():
		#	self.Mabil[key].set('')
		self.rollval = StringVar()
		
		self.grapple = {}
		self.grapple['total'] = StringVar()
		self.grapple['misc'] = StringVar()
		self.grapple['size'] = StringVar()
		
	def draw(self):
		self.root.title("Character Creator")
		self.root.geometry("850x650")

		# Selection Lists
		self.levelList = range(1,21)
		self.drawline1()
		self.drawline2()
		self.drawline3()
		self.separator1()
		self.drawAbilities()
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
		
		self.update()
		
	def drawline1(self):
		# Create First Line Objects
		self.LcharName = Label(self.root, text="Character Name:", relief=GROOVE, width=13, anchor=E)
		self.LplayerName = Label(self.root, text="Player Name:",  relief=GROOVE, width=12, anchor=E)
		self.EcharName = Entry(  self.root, width=36)
		self.EplayerName = Entry(self.root, width=36)

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
		self.CMBclass = ttk.Combobox(self.root, width=12, values=self.char.classList, textvariable=self.cClass)
		self.CMBalign = ttk.Combobox(self.root, width=18, values=self.char.align, textvariable=self.align)
		self.CMBlevel = ttk.Combobox(self.root, width=6,  values=self.levelList)
		self.Edeity = Entry(self.root, width=12)

		# Place Line 2 on Grid
		self.Lclass.grid(  row=1, column=0, sticky=EW)
		self.CMBclass.grid(row=1, column=1, sticky=EW, columnspan=2)
		self.Llevel.grid(  row=1, column=3, sticky=EW)
		self.CMBlevel.grid(row=1, column=4, sticky=EW)
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
		self.Lsize   = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Size:")
		self.Lage    = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Age:")
		self.Lgender = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Gender:")
		self.Lheight = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Height:")
		self.Lweight = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Weight:")
		self.Leyes   = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Eyes:")
		self.Lhair   = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Hair:")
		self.Lskin   = Label(self.root, relief=GROOVE, anchor=E, width=6, text="Skin:")
		self.Esize   = Entry(self.root, width=6, state=DISABLED, textvariable=self.size)
		self.Eage    = Entry(self.root, width=6)
		self.Egender = Entry(self.root, width=6)
		self.Eheight = Entry(self.root, width=6)
		self.Eweight = Entry(self.root, width=6)
		self.Eeyes   = Entry(self.root, width=6)
		self.Ehair   = Entry(self.root, width=6)
		self.Eskin   = Entry(self.root, width=6)

		# Place Line 3 on Grid
		self.Lsize.grid(  row=2, column=0,  sticky=EW)
		self.Esize.grid(  row=2, column=1,  sticky=EW)
		self.Lage.grid(   row=2, column=2,  sticky=EW)
		self.Eage.grid(   row=2, column=3,  sticky=EW)
		self.Lgender.grid(row=2, column=4,  sticky=EW)
		self.Egender.grid(row=2, column=5,  sticky=EW)
		self.Lheight.grid(row=2, column=6,  sticky=EW)
		self.Eheight.grid(row=2, column=7,  sticky=EW)
		self.Lweight.grid(row=2, column=8,  sticky=EW)
		self.Eweight.grid(row=2, column=9,  sticky=EW)
		self.Leyes.grid(  row=2, column=10, sticky=EW)
		self.Eeyes.grid(  row=2, column=11, sticky=EW)
		self.Lhair.grid(  row=2, column=12, sticky=EW)
		self.Ehair.grid(  row=2, column=13, sticky=EW)
		self.Lskin.grid(  row=2, column=14, sticky=EW)
		self.Eskin.grid(  row=2, column=15, sticky=EW)

	def updateline3(self):
		self.size = self.char.size
		
	def separator1(self):
		#Create blank space on grid
		self.Fempty = Frame(self.root, height=20, width=5)
		self.Fempty.grid(row=3,column=0,columnspan=16, sticky=NSEW)
		
	def drawAbilities(self):
		self.EabilMod = {}
		self.Babil = {}
	
		# Create Ability Label
		self.Babil['STR'] = Button(self.root, text="STR", relief=GROOVE, anchor=E, width=4, command=PopUp().Bstr)
		self.Babil['DEX'] = Button(self.root, text="DEX", relief=GROOVE, anchor=E, width=4, command=PopUp().Bdex)
		self.Babil['CON'] = Button(self.root, text="CON", relief=GROOVE, anchor=E, width=4)
		self.Babil['INT'] = Button(self.root, text="INT", relief=GROOVE, anchor=E, width=4)
		self.Babil['WIS'] = Button(self.root, text="WIS", relief=GROOVE, anchor=E, width=4)
		self.Babil['CHA'] = Button(self.root, text="CHA", relief=GROOVE, anchor=E, width=4)

		
		for i, item in enumerate(self.Abilities):
			self.CMBabil[item] = ttk.Combobox(self.root, width=4, textvariable=self.abil[item])
			self.EabilMod[item] = Entry(self.root, width=3, state=DISABLED, textvariable=self.Mabil[item])
			self.Labilnote[item] = Label(self.root, width=6, textvariable=self.traits[item])
			
			self.Babil[item].grid(row=i+4, column=0, sticky=E)
			self.CMBabil[item].grid(row=i+4,column=1, sticky=W)
			self.EabilMod[item].grid(row=i+4,column=2, sticky=W)
			self.Labilnote[item].grid(row=i+4,column=3, sticky=EW)
		
		
	def drawRoll(self):
		# Create and Place Roll button
		self.Broll = Button(self.root, text="Roll Abilities", command=self.customRoll)
		self.Broll.grid(row=10, column=0, columnspan=2)		
		self.Broll = Button(self.root, text="Default", width=6, command=self.defaultRoll)
		self.Broll.grid(row=10, column=2)
		self.roll = Label(self.root, width=18, state=DISABLED, textvariable=self.rollval)
		self.roll.grid(row=11, column=0, columnspan=3)
	
	def drawHP(self):
		self.Bhp = Button(self.root, relief=GROOVE, anchor=E, text="HP", command=PopUp().Bhp)
		self.Ehp = Entry(self.root, state=DISABLED, width=4, justify=CENTER, textvariable=self.hp)
		self.Bhp.grid(row=4, column=4, sticky=E)
		self.Ehp.grid(row=4, column=5, sticky=W+N+S)
	
	def drawAC(self):
		self.Bac = Button(self.root, relief=GROOVE, anchor=E, text="AC")
		self.Eac = Entry(self.root, state=DISABLED, width=4, justify=CENTER, textvariable=self.AC['total'])
		self.Lac1 = Label(self.root, text="=")
		self.Lacten = Label(self.root, text="  10 ")
		self.Lacplus1 = Label(self.root, text=" +   ")
		self.Lacplus2 = Label(self.root, text="+")
		self.Lacplus3 = Label(self.root, text="+")
		self.Lacplus4 = Label(self.root, text="+")
		self.Lacplus5 = Label(self.root, text="+")
		self.Lacplus6 = Label(self.root, text="+")
		self.Lacplus7 = Label(self.root, text="+")
		self.Lacplus8 = Label(self.root, text="+")
		self.Lacplus9 = Label(self.root, text="+")
		self.Eac2 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['armor'])
		self.Eac3 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['shield'])
		self.Eac4 = Entry(self.root, justify=CENTER, width=4, state=DISABLED, textvariable=self.Mabil['DEX'])
		self.Eac5 = Entry(self.root, justify=CENTER, width=4, state=DISABLED, textvariable=self.AC['size'])
		self.Eac6 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['nat'])
		self.Eac7 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['deflect'])
		self.Eac8 = Entry(self.root, justify=CENTER, width=4,  textvariable=self.AC['misc'])
				
		self.Bac.grid( row=5, column=4, sticky=E)
		self.Eac.grid( row=5, column=5, sticky=W+N+S)
		self.Lac1.grid(row=5, column=5, sticky=E)
		self.Lacten.grid(row=5, column=6, sticky=W)
		self.Lacplus1.grid(row=5, column=6, sticky=E)
		self.Eac2.grid(row=5, column=7, sticky=W)
		self.Lacplus2.grid(row=5, column=7, sticky=E)
		self.Eac3.grid(row=5, column=8, sticky=W)
		self.Lacplus3.grid(row=5,column=8, sticky=E)
		self.Eac4.grid(row=5, column=9, sticky=W)
		self.Lacplus4.grid(row=5,column=9, sticky=E)
		self.Eac5.grid(row=5, column=10, sticky=W)
		self.Lacplus5.grid(row=5,column=10, sticky=E)
		self.Eac6.grid(row=5, column=11, sticky=W)
		self.Lacplus6.grid(row=5,column=11, sticky=E)
		self.Eac7.grid(row=5, column=12, sticky=W)
		self.Lacplus7.grid(row=5,column=12, sticky=E)
		self.Eac8.grid(row=5, column=13, sticky=W)
		
		self.Lac2 = Label(self.root, font=('TkDefaultFont', 6), text="Armor\nBonus")
		self.Lac3 = Label(self.root, font=('TkDefaultFont', 6), text="Shield\nBonus")
		self.Lac4 = Label(self.root, font=('TkDefaultFont', 6), text="Dex\nModifier")
		self.Lac5 = Label(self.root, font=('TkDefaultFont', 6), text="Size\nModifier")
		self.Lac6 = Label(self.root, font=('TkDefaultFont', 6), text="Natural\nArmor")
		self.Lac7 = Label(self.root, font=('TkDefaultFont', 6), text="Deflection\nModifier")
		self.Lac8 = Label(self.root, font=('TkDefaultFont', 6), text="Misc\nModifier")
		self.Lac2.grid(row=6, column=7 , sticky=W)
		self.Lac3.grid(row=6, column=8 , sticky=W)
		self.Lac4.grid(row=6, column=9 , sticky=W)
		self.Lac5.grid(row=6, column=10, sticky=W)
		self.Lac6.grid(row=6, column=11, sticky=W)
		self.Lac7.grid(row=6, column=12, sticky=W)
		self.Lac8.grid(row=6, column=13, sticky=W)
		
		self.BtouchAC = Button(self.root, relief=GROOVE, anchor=E, text="Touch AC")
		self.EtouchAC = Entry( self.root, width=6, state=DISABLED, textvariable=self.AC['touch'])
		self.BflatAC = Button( self.root, relief=GROOVE, anchor=E, text="Flat-Footed")
		self.EflatAC = Entry(  self.root, width=6, state=DISABLED, textvariable=self.AC['flat'])
		
		self.BtouchAC.grid(row=7, column=4, columnspan=2, sticky=E)
		self.EtouchAC.grid(row=7, column=6, sticky=N+S+W)
		self.BflatAC.grid( row=7, column=7, columnspan=2, sticky=E)
		self.EflatAC.grid( row=7, column=9, sticky=N+S+W)
		
		self.Bdamred = Button(self.root, relief=GROOVE, anchor=E, text="Damage Reduction")
		self.Ldamred = Entry(self.root, width=12)
		
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
		
		self.INSERT = Label(self.root, text="INSERT CONDITIONAL MODIFIERS HERE!\n")
		self.INSERT.grid(row=16, column=1, columnspan=6, rowspan=2)
		
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
		
		
	#self.Bfort.grid(  row=13, column=0, columnspan=3, sticky=E) 
	#self.Eftotal.grid(row=13, column=3)
	#self.Lfeq.grid(   row=13, column=3, columnspan=2)   
	#self.Efbase.grid( row=13, column=4) 
	#self.Lfplus1.grid(row=13, column=4, sticky=E)
	#self.Efabilm.grid(row=13, column=5, sticky=W)
	#self.Lfplus2.grid(row=13, column=5, sticky=E)
	#self.Efmagic.grid(row=13, column=6, sticky=W)
	#self.Lfplus3.grid(row=13, column=6, sticky=E)
	#self.Efmisc.grid( row=13, column=7, sticky=W)
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
	
	def skillsPage(self):
		if not self.skillsP:
			self.skillsP = Toplevel(self.root)
			Skills(self.skillsP, self.Mabil, self.char)
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
		
	def customRoll(self):
		self.rollList = roller.roll(1, 1, 1)
		self.onRoll()
		
	def onRoll(self):
		if self.cClass.get() and self.Race.get():
			self.rollList.append('')
			self.rollList.sort()
			self.backupRollList = self.rollList
			self.rollval.set(str(self.rollList).lstrip('[').rstrip(',\']').replace(',', ' '))
			self.resetAbil()
			for key in self.CMBabil.keys():
				self.CMBabil[key]['values'] = self.rollList
		else:
			PopUp().warn("Abilities", "Please select class and race before altering abilities")
	def resetAbil(self):
		if self.cClass != '' and self.Race != '':
			# empties abilities
			for key in self.abil.keys():
				self.abil[key].set('')
			for key in self.Mabil.keys():
				self.Mabil[key].set('')
			# resets combobox lists - unnecessarry?
			#for key in self.unrollDict:
				#self.rollList.append(self.unrollDict[key])  #put it back in selection list
				#self.rollList.sort()
			self.unrollDict.clear()
			self.unrollDict = {}
			#remake combobox values
			for keyval in self.CMBabil.keys():
				self.CMBabil[keyval]['values'] = self.backupRollList

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
		
	#def resetLang(self):
	#	self.CMBlang['values'] = self.char.bonusLang
	#	self.Llang['text'] = 
	
	def updateAbilities(self, args, key):
		if key:
			val = self.abil[key].get()
		else:
			return
		if val.isdigit():
			# lets you reselect a value without first setting to ''
			if key in self.unrollDict.keys():
				self.pushAbilList(key)
			# removes from combobox and set modifier (with any racial bonus or detriment)
			if key in self.char.traits.keys():
				trait = int(self.char.traits[key])
				self.abil[key].set(int(val) + trait)
				self.Mabil[key].set((int(val) + trait - 10) /2)
			else: # if no racial bonus
				self.Mabil[key].set((int(self.abil[key].get()) - 10) /2)
			self.popAbilList(key, val)
			if self.skillsP:
				self.skillsP.destroy()
				self.skillsP = None
		else:
			self.pushAbilList(key)
		
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
		self.acBind()
		self.abilBind()
		#self.root.bind("<Button-1>", self.clickd)
		
	def abilBind(self):
		#self.CMBabil['STR'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'STR'))
		##self.CMBabil['STR'].bind("<Leave>", lambda event: self.updateAbilities(event, 'STR'))
		#self.CMBabil['DEX'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'DEX'))
		##self.CMBabil['DEX'].bind("<Leave>", lambda event: self.updateAbilities(event, 'DEX'))
		#self.CMBabil['CON'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'CON'))
		##self.CMBabil['CON'].bind("<Leave>", lambda event: self.updateAbilities(event, 'CON'))
		#self.CMBabil['INT'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'INT'))
		##self.CMBabil['INT'].bind("<Leave>", lambda event: self.updateAbilities(event, 'INT'))
		#self.CMBabil['WIS'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'WIS'))
		##self.CMBabil['WIS'].bind("<Leave>", lambda event: self.updateAbilities(event, 'WIS'))
		#self.CMBabil['CHA'].bind("<<ComboboxSelected>>", lambda event: self.updateAbilities(event, 'CHA'))
		##self.CMBabil['CHA'].bind("<Leave>", lambda event: self.updateAbilities(event, 'CHA'))
		for abil in self.CMBabil.keys():
			self.CMBabil[abil].bind("<<ComboboxSelected>>", self.makeLambda(abil))
		
	def makeLambda(self, skill):
		return lambda event: self.updateAbilities(event, skill)
		
	def acBind(self):
		self.Eac2.bind("<Leave>", self.updateAC)
		self.Eac3.bind("<Leave>", self.updateAC)
		self.Eac6.bind("<Leave>", self.updateAC)
		self.Eac7.bind("<Leave>", self.updateAC)
		self.Eac8.bind("<Leave>", self.updateAC)
	
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
			
	def updateInit(self):
		total = 0
		if self.init['misc'].get():
			total += int(self.init['misc'].get())
		if self.Mabil['DEX'].get():
			total += int(self.Mabil['DEX'].get())
		self.init['total'].set(str(total))
			
	def updateGrapple(self):
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
		
	def updateSaves(self):
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
			self.size.set(self.char.size)
		else:
			self.size.set('')
		
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
		
		self.updateAC()
		self.updateline3
		self.updateGrapple()
		self.resetLanguages()
		self.update()
		
	def classSelect(self, *args):
		self.remakeClass()
		self.align.set('')
		# set HP
		self.LspecialsL['text'] = "\n".join(self.char.special)
		if self.char.hitDie:
			self.hp.set(self.char.hitDie)
		if self.char.spellCaster:
			self.Bspells['state'] = 'normal'
		else:
			self.Bspells['state'] = 'disabled'
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
		self.resetAbil()
		
		if self.skillsP:
				self.skillsP.destroy()
				self.skillsP = None
				
	def remakeClass(self):
		del self.char
		self.char = Character(self.Race.get(), self.cClass.get())	
		
	def clickd(self, *args):
		if self.char.size:
			self.size.set(self.char.size)
		#self.draw

x = CharacterCreator()