from Tkinter import *
import Tkinter as tk
import ttk
import tkMessageBox as msg

class Skills(object):
	def __init__(self, root, abilities):
		self.root = root
		self.canvas = tk.Canvas(root)
		self.frame = tk.Frame(self.canvas)
		self.vsb = tk.Scrollbar(root, orient='vertical', command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		self.vsb.pack(side='right', fill='y')
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")
		self.frame.bind("<Configure>", self.OnFrameConfigure)
								  
		self.root.protocol("WM_DELETE_WINDOW", self.saveClose)
		self.root.title("Skills")
		self.root.geometry("700x800")
		self.Mabil = abilities
		self.createVars()
		self.draw()
		
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
		self.TotalMod = {}
		self.Ranks = {}
		self.MiscMod = {}
		self.classSkill = {}
		self.CBskill = {}
		self.Bskillname = {}
		self.Lkeyabil = {}
		self.EskillMod = {}
		self.EabilMod =  {}
		self.LEquals = {}
		self.LPlusOne = {}
		self.CMBranks = {}
		self.LPlusTwo = {}
		self.EmiscMod = {}
		
		for key in self.SkillList.keys():
			self.TotalMod[key]	 = StringVar()
			self.Ranks[key] 	 = StringVar()
			self.MiscMod[key]	 = StringVar()
			self.classSkill[key] = StringVar()

		
	def draw(self):
		self.drawHeader()
		self.drawEverythingElse()
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
			self.CBskill[item] 		= Checkbutton(self.frame, state=DISABLED) # checkboxes
			self.Bskillname[item] 	= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text=item) # skill names
			self.Lkeyabil[item] 	= Label(self.frame,  width=4, text=self.SkillList[item])
			self.EskillMod[item] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.TotalMod[item])
			self.LEquals[item]		= Label(self.frame,  width=2, text='=')
			self.EabilMod[item] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil[self.SkillList[item].strip('*')])
			self.LPlusOne[item]		= Label(self.frame,  width=2, text='+')
			self.CMBranks[item]		= ttk.Combobox(self.frame, width=5, values='', textvariable=self.Ranks[item])
			self.LPlusTwo[item]		= Label(self.frame,  width=2, text='+')
			self.EmiscMod[item] 	= Entry(self.frame,  width=3, justify=CENTER, textvariable=self.MiscMod[item])
			
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
			
	def bind(self):
		self.CMBvar.bind("<<ComboboxSelected>>", self.setvar)
	
	def setvar(self):
		self.var.set(self.var.get())
		
	def drawButton(self):
		self.Bclose = Button(self.root, text="Save Close", command=self.saveClose)
		self.Bclose.grid(row=0, column=3)
		
	def saveClose(self):
		self.root.withdraw()
		
	def setbind(self):
		for item in self.SkillSet:
			self.CMBranks[item].bind("<<ComboboxSelected>>", lambda event: self.updateSkills(event, item))
			
	def updateSkills(self, args, key):
		print key
			
			