from Tkinter import *
import ttk, os, pickle
import Tkinter as tk
import tkMessageBox as msg
import filestructure as fstruct
from PopUp import PopUp

class Skills(object):
	def __init__(self, topl, abilities, character):
		self.topl = topl
		self.canvas = tk.Canvas(topl)
		self.frame = tk.Frame(self.canvas)
		self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
		self.vsb = tk.Scrollbar(topl, orient='vertical', command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		self.vsb.pack(side='right', fill='y')
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
		self.frame.bind("<Configure>", self.OnFrameConfigure)
								  
		self.topl.protocol("WM_DELETE_WINDOW", self.saveClose)
		self.topl.title("Skills")
		self.topl.geometry("700x800")
		self.Mabil = abilities
		self.char = character
		self.createVars()		
		self.calcsp()
		self.RemaingingSP.set(self.NumSP.get())
		self.loadSP()
		self.draw()
		
		
	def _on_mousewheel(self, event):
		self.canvas.yview_scroll(-1*(event.delta/120), "units")
		
	def OnFrameConfigure(self, event):
        #'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
		
	def createVars(self):	
		self.SkillList = {	"Appraise": 'INT', 
							"Balance": 'DEX*', 
							"Bluff": 'CHA', 
							"Climb": 'STR*', 
							"Concentration": 'CON', 
							"Craft(1)": 'INT', 
							"Craft(2)": 'INT', 
							"Craft(3)": 'INT', 
							"Decipher Script": 'INT', 
							"Diplomacy": 'CHA', 
							"Disable Device": 'INT',
							"Disguise": 'CHA', 
							"Escape Artist": 'DEX*', 
							"Forgery": 'INT', 
							"Gather Information": 'CHA', 
							"Handle Animal": 'CHA', 
							"Heal": 'WIS', 
							"Hide": 'DEX*', 
							"Intimidate": 'CHA', 
							"Jump": 'STR*', 
							"Knowledge(1)": 'INT', 
							"Knowledge(2)": 'INT', 
							"Knowledge(3)": 'INT', 
							"Knowledge(4)": 'INT', 
							"Knowledge(5)": 'INT', 
							"Listen": 'WIS', 
							"Move Silently": 'DEX*', 
							"Open Lock": 'DEX', 
							"Perform(1)": 'CHA', 
							"Perform(2)": 'CHA', 
							"Perform(3)": 'CHA', 
							"Profession(1)": 'WIS', 
							"Profession(2)": 'WIS', 
							"Ride": 'DEX', 
							"Search": 'INT', 
							"Sense Motive": 'WIS', 
							"Sleight of Hand": 'DEX*', 
							"Spellcraft": 'INT', 
							"Spot": 'WIS', 
							"Survival": 'WIS', 
							"Swim": 'STR*', 
							"Tumble": 'DEX*', 
							"Use Magic Device": 'CHA', 
							"Use Rope": 'DEX', 
							#"Other(1)": '', 
							#"Other(2)": '', 
							#"Other(3)": ''
							}
		self.SkillSet = set(self.SkillList)
		self.onoff = {}
		for key in self.SkillSet:
			self.onoff[key] = self.cbonoff(key)
		self.TotalMod = {}
		self.Ranks = {}
		self.MiscMod = {}
		self.classSkill = {}
		self.CBskill = {}
		self.Bskillname = {}
		self.Lkeyabil = {}
		self.EskillMod = {}
		self.EabilMod =  {}
		self.LclassMod =  {}
		self.LEquals = {}
		self.LPlusOne = {}
		self.CMBranks = {}
		self.LPlusTwo = {}
		self.EmiscMod = {}
		self.NumSP = IntVar()
		self.RemaingingSP = IntVar()
		
		for key in self.SkillList.keys():
			self.TotalMod[key]	 = StringVar()
			self.Ranks[key] 	 = StringVar()
			self.MiscMod[key]	 = StringVar()
			self.classSkill[key] = StringVar()
		self.flag = False # used to check calcSP()
				
		
	def draw(self):
		self.drawHeader()
		self.drawEverythingElse()
		self.drawEmptyCol()
		self.drawButtons()
		self.drawSkillPointinfo()
		self.update()
		
	def update(self):
		self.frame.focus_set()
		self.setbind()
		self.frame.mainloop()
		
	
	def drawHeader(self):
		self.Lname = Button(self.frame, relief=GROOVE, width=12, text="Skill Name")	
		self.LclassSkill = Label(self.frame, font=('TkDefaultFont', 6), text="Class\nSkill")
		self.LkeyAbil = Label(self.frame, font=('TkDefaultFont', 6), text="Key\nAbility")
		self.LskillMod = Label(self.frame, font=('TkDefaultFont', 6), text="Skill\nModifier")
		self.LabilMod = Label(self.frame, font=('TkDefaultFont', 6), text="Ability\nModifier")
		self.Lranks = Label(self.frame, font=('TkDefaultFont', 6), text="Ranks")
		self.LmiscMod = Label(self.frame, font=('TkDefaultFont', 6), text="Misc\nModifier")
		
		self.Lname.grid(row=0, column=1)
		self.LclassSkill.grid(row=0, column=0)
		self.LkeyAbil.grid(row=0, column=2)
		self.LskillMod.grid(row=0, column=3)
		self.LabilMod.grid(row=0, column=5)
		self.Lranks.grid(row=0, column=7)
		self.LmiscMod.grid(row=0, column=9)
	
	def drawEverythingElse(self):
		for i, item in enumerate(sorted(self.SkillList.keys())):
			#make everything
			self.CBskill[item] 		= Checkbutton(self.frame, state=DISABLED, variable=self.onoff[item]) # checkboxes
			self.Bskillname[item] 	= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text=item) # skill names
			self.Lkeyabil[item] 	= Label(self.frame,  width=4, text=self.SkillList[item])
			self.EskillMod[item] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.TotalMod[item])
			self.LEquals[item]		= Label(self.frame,  width=2, text='=')
			self.EabilMod[item] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil[self.SkillList[item].strip('*')])
			self.LPlusOne[item]		= Label(self.frame,  width=2, text='+')
			self.CMBranks[item]		= ttk.Combobox(self.frame, width=5, values=self.UpdateRankList(item), textvariable=self.Ranks[item])
			self.LPlusTwo[item]		= Label(self.frame,  width=2, text='+')
			self.EmiscMod[item] 	= Entry(self.frame,  width=3, justify=CENTER, textvariable=self.MiscMod[item])
			self.LclassMod[item]	= Label(self.frame, width=7, textvariable=self.getBonusSkills(item))
			
			#draw everything
			self.CBskill[item].grid(	row = i+1, column=0, sticky=E+W)
			self.Bskillname[item].grid(	row = i+1, column=1, sticky=E+W)
			self.Lkeyabil[item].grid(	row = i+1, column=2, sticky=E+W)	
			self.EskillMod[item].grid(	row = i+1, column=3, sticky=E+W)
			self.LEquals[item].grid(	row = i+1, column=4, sticky=E+W)			
			self.EabilMod[item].grid(	row = i+1, column=5, sticky=E+W)
			self.LPlusOne[item].grid(	row = i+1, column=6, sticky=E+W)
			self.CMBranks[item].grid(	row = i+1, column=7, sticky=E+W)
			self.LPlusTwo[item].grid(	row = i+1, column=8, sticky=E+W)
			self.EmiscMod[item].grid(	row = i+1, column=9, sticky=E+W)
			self.LclassMod[item].grid(	row = i+1, column=11, sticky=E+W)
	
	def getBonusSkills(self, key):
		x = StringVar()
		if self.char.bonusSkills and key in self.char.bonusSkills:
			val = self.char.bonusSkills[key]
			if val > 0:
				x.set("+"+str(val)+" (Race)")
			elif val < 0:
				x.set("-"+str(val)+" (Race)")
		return x
		
				
	def drawEmptyCol(self):
		self.EmptyCol = Label(self.frame, width=5)
		self.EmptyCol.grid(row=0, column=12)
		
	def drawButtons(self):
		self.Bclose = Button(self.frame, text="Save Close", command=self.saveClose)
		self.Breset = Button(self.frame, text="Reset", command=self.reset)
		#self.Bsave  = Button(self.frame, text="Save", command=self.save)
		
		self.Bclose.grid(row=1, column=13)
		self.Breset.grid(row=2, column=13)
		#self.Bsave.grid( row=4, column=12)
		
	def drawSkillPointinfo(self):
		self.Btotalsp = Button(self.frame, relief=GROOVE, text="Total Skill Points")
		self.BspRemaining = Button(self.frame,relief=GROOVE, text="Skill Points Remaining")
		
		self.Ltotalsp = Label(self.frame, width=6, textvariable=self.NumSP)
		self.Lremainingsp = Label(self.frame, width=6, textvariable=self.RemaingingSP)
		
		self.Btotalsp.grid(row = 15, column=13)
		self.Ltotalsp.grid(row = 16, column=13)
		self.BspRemaining.grid(row = 17, column=13)
		self.Lremainingsp.grid(row = 18, column=13)
		
	
	def calcsp(self, *arg):
		skillpoints = 0
		if self.char.classSkillPoints and self.Mabil['INT'].get():
			skillpoints += (self.char.classSkillPoints+int(self.Mabil['INT'].get()))*4
		if skillpoints < 4:
			skillpoints = 4		
		if self.char.baseRaceSkillPoints:
			skillpoints += self.char.baseRaceSkillPoints
		self.NumSP.set(str(skillpoints))
		self.calcRemaingingSP()
		if self.RemaingingSP.get() < 0 and self.flag == False:
			#self.close()
			self.flag = True
			PopUp().error('','Too many skill points assigned, resetting')		
			self.reset()
			self.flag = False
	
	def reset(self):
		self.calcsp()
		self.RemaingingSP.set(self.NumSP.get())
		for skill in self.SkillSet:
			self.CMBranks[skill]['values'] = self.UpdateRankList(skill)
			self.CMBranks[skill].set('')
			self.Ranks[skill].set('')
			self.MiscMod[skill].set('')
			self.TotalMod[skill].set('')
			#self.updateSkills(skill, False)
			
	def save(self):
		pickledict = {'Rank':{},'Misc':{}}
		for skill in self.SkillSet:
			pickledict['Rank'][skill] = self.Ranks[skill].get()	
			pickledict['Misc'][skill] = self.MiscMod[skill].get()
			
		with open(fstruct.SKILLPICKLE, "wb+") as f:
			pickle.dump(pickledict, f)
	
	def close(self):
		self.topl.destroy()
	
	def saveClose(self):
		self.save()
		self.close()
		
	def loadSP(self):
		# load pickle file 
		flag = False
		if os.path.isfile(fstruct.SKILLPICKLE):
			with open(fstruct.SKILLPICKLE, "rb") as f:
				pdict = pickle.load(f)
	
			for key in self.SkillSet:
				self.Ranks[key].set(pdict['Rank'][key])
				self.MiscMod[key].set(pdict['Misc'][key])
				self.updateSkills(key, None)
	
	def setbind(self):
		for skill in self.SkillSet:
			self.canvas.bind_all("<Enter>", self.calcsp)
			self.canvas.bind_all("<Leave>", self.calcsp)
			self.CMBranks[skill].bind("<<ComboboxSelected>>", self.makeLambda(skill))
			self.EmiscMod[skill].bind("<FocusOut>", self.makeLambda(skill)) 
			self.EmiscMod[skill].bind("<KeyRelease>", self.makeLambda(skill)) 
	
	def makeLambda(self, skill):
		return lambda event: self.updateSkills(skill, event)
		
	def cbonoff(self, skillname):
		ret = IntVar()
		if skillname in self.char.classSkills:
			ret.set(1)
			return ret
		else:
			return ret
	
	def UpdateRankList(self, skillname):		
		if skillname in self.char.classSkills:	
			return [i for i in xrange(min(self.char.characterLevel+4, self.RemaingingSP.get()+1))] #+1 since xrange is noninclusive
		else:
			return [i for i in xrange(min((self.char.characterLevel+3)/2+1, self.RemaingingSP.get()+1))]  #+1 since xrange is noninclusive

	# Could make different functions for setbind, so we don't have to do multiple checks each time
	def updateSkills(self, key, args=False):
		setval = 0
		if self.Mabil[self.SkillList[key].strip('*')].get().isdigit():
			setval += int(self.Mabil[self.SkillList[key].strip('*')].get())
		if self.Ranks[key].get().isdigit():
			self.calcRemaingingSP()
			if args != None: # set in self.loadSP(), skips if we've opened before
				for skill in self.SkillSet: 
					self.CMBranks[skill]['values'] = self.UpdateRankList(skill)
			setval += int(self.Ranks[key].get())
		if self.MiscMod[key].get().isdigit():
			setval += int(self.MiscMod[key].get())
		if self.char.bonusSkills and key in self.char.bonusSkills:
			setval += self.char.bonusSkills[key]
		if setval > 0:
			self.TotalMod[key].set(setval)
		else:
			self.TotalMod[key].set(0)
		
	def calcRemaingingSP(self):
		rem = 0
		for skill in self.SkillSet:
			if self.Ranks[skill].get().isdigit():
				rem += int(self.Ranks[skill].get())
		return self.RemaingingSP.set(self.NumSP.get() - rem)
		