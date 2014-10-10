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
							"Other(1)": '', 
							"Other(2)": '', 
							"Other(3)": ''}
		self.TotalMod = {}
		self.Ranks = {}
		self.MiscMod = {}
		self.classSkill = {}
		self.CBskill = {}
		self.Bskillname = {}
		self.Lkeyabil = {}
		self.EskillMod = {}
		self.EabilMod =  {}
		for key in self.SkillList.keys():
			self.TotalMod[key]	 = StringVar()
			self.Ranks[key] 	 = StringVar()
			self.MiscMod[key]	 = StringVar()
			self.classSkill[key] = StringVar()
		#self.TotalMod['Appraise'] = StringVar()  
		#self.TotalMod['Balance'] = StringVar()  
		#self.TotalMod['Bluff'] = StringVar()  
		#self.TotalMod['Climb'] = StringVar()  
		#self.TotalMod['Concentration'] = StringVar()  
		#self.TotalMod['Craft(1)'] = StringVar()  
		#self.TotalMod['Craft(2)'] = StringVar()  
		#self.TotalMod['Craft(3)'] = StringVar()  
		#self.TotalMod['Decipher Script'] = StringVar()  
		#self.TotalMod['Diplomacy'] = StringVar()  
		#self.TotalMod['Disable Device'] = StringVar()  
		#self.TotalMod['Disguise'] = StringVar()  
		#self.TotalMod['Forgery'] = StringVar()  
		#self.TotalMod['Gather Information'] = StringVar()  
		#self.TotalMod['Handle Animal'] = StringVar()  
		#self.TotalMod['Heal'] = StringVar()  
		#self.TotalMod['Hide'] = StringVar()  
		#self.TotalMod['Intimidate'] = StringVar()  
		#self.TotalMod['Jump'] = StringVar()  
		#self.TotalMod['Knowledge(1)'] = StringVar()  
		#self.TotalMod['Knowledge(2)'] = StringVar()  
		#self.TotalMod['Knowledge(3)'] = StringVar()  
		#self.TotalMod['Knowledge(4)'] = StringVar()  
		#self.TotalMod['Knowledge(5)'] = StringVar()  
		#self.TotalMod['Listen'] = StringVar()  
		#self.TotalMod['Move Silently'] = StringVar()  
		#self.TotalMod['Open Lock'] = StringVar()  
		#self.TotalMod['Perform(1)'] = StringVar()  
		#self.TotalMod['Perform(2)'] = StringVar()  
		#self.TotalMod['Perform(3)'] = StringVar()  
		#self.TotalMod['Profession(1)'] = StringVar()  
		#self.TotalMod['Profession(2)'] = StringVar()  
		#self.TotalMod['Ride'] = StringVar()  
		#self.TotalMod['Search'] = StringVar()  
		#self.TotalMod['Sense Motive'] = StringVar()  
		#self.TotalMod['Sleight of Hand'] = StringVar()  
		#self.TotalMod['Spellcraft'] = StringVar()  
		#self.TotalMod['Spot'] = StringVar()  
		#self.TotalMod['Survival'] = StringVar()  
		#self.TotalMod['Swim'] = StringVar()  
		#self.TotalMod['Tumble'] = StringVar()  
		#self.TotalMod['Use Magic Device'] = StringVar()  
		#self.TotalMod['Use Rope'] = StringVar()  
		#self.TotalMod['Other(1)'] = StringVar()  
		#self.TotalMod['Other(2)'] = StringVar()  
		#self.TotalMod['Other(3)'] = StringVar()  
		
		#self.Ranks['Appraise'] = StringVar()  
		#self.Ranks['Balance'] = StringVar()  
		#self.Ranks['Bluff'] = StringVar()  
		#self.Ranks['Climb'] = StringVar()  
		#self.Ranks['Concentration'] = StringVar()  
		#self.Ranks['Craft(1)'] = StringVar()  
		#self.Ranks['Craft(2)'] = StringVar()  
		#self.Ranks['Craft(3)'] = StringVar()  
		#self.Ranks['Decipher Script'] = StringVar()  
		#self.Ranks['Diplomacy'] = StringVar()  
		#self.Ranks['Disable Device'] = StringVar()  
		#self.Ranks['Disguise'] = StringVar()  
		#self.Ranks['Disguise'] = StringVar()  
		#self.Ranks['Escape Artist'] = StringVar()  
		#self.Ranks['Forgery'] = StringVar()  
		#self.Ranks['Gather Information'] = StringVar()  
		#self.Ranks['Handle Animal'] = StringVar()  
		#self.Ranks['Heal'] = StringVar()  
		#self.Ranks['Hide'] = StringVar()  
		#self.Ranks['Intimidate'] = StringVar()  
		#self.Ranks['Jump'] = StringVar()  
		#self.Ranks['Knowledge(1)'] = StringVar()  
		#self.Ranks['Knowledge(2)'] = StringVar()  
		#self.Ranks['Knowledge(3)'] = StringVar()  
		#self.Ranks['Knowledge(4)'] = StringVar()  
		#self.Ranks['Knowledge(5)'] = StringVar()  
		#self.Ranks['Listen'] = StringVar()  
		#self.Ranks['Move Silently'] = StringVar()  
		#self.Ranks['Open Lock'] = StringVar()  
		#self.Ranks['Perform(1)'] = StringVar()  
		#self.Ranks['Perform(2)'] = StringVar()  
		#self.Ranks['Perform(3)'] = StringVar()  
		#self.Ranks['Profession(1)'] = StringVar()  
		#self.Ranks['Profession(2)'] = StringVar()  
		#self.Ranks['Ride'] = StringVar()  
		#self.Ranks['Search'] = StringVar()  
		#self.Ranks['Sense Motive'] = StringVar()  
		#self.Ranks['Sleight of Hand'] = StringVar()  
		#self.Ranks['Spellcraft'] = StringVar()  
		#self.Ranks['Spot'] = StringVar()  
		#self.Ranks['Survival'] = StringVar()  
		#self.Ranks['Swim'] = StringVar()  
		#self.Ranks['Tumble'] = StringVar()  
		#self.Ranks['Use Magic Device'] = StringVar()  
		#self.Ranks['Use Rope'] = StringVar()  
		#self.Ranks['Other(1)'] = StringVar()  
		#self.Ranks['Other(2)'] = StringVar()  
		#self.Ranks['Other(3)'] = StringVar()  
		
		#self.MiscMod['Appraise'] = StringVar()  
		#self.MiscMod['Balance'] = StringVar()  
		#self.MiscMod['Bluff'] = StringVar()  
		#self.MiscMod['Climb'] = StringVar()  
		#self.MiscMod['Concentration'] = StringVar()  
		#self.MiscMod['Craft(1)'] = StringVar()  
		#self.MiscMod['Craft(2)'] = StringVar()  
		#self.MiscMod['Craft(3)'] = StringVar()  
		#self.MiscMod['Decipher Script'] = StringVar()  
		#self.MiscMod['Diplomacy'] = StringVar()  
		#self.MiscMod['Disable Device'] = StringVar()  
		#self.MiscMod['Disguise'] = StringVar()  
		#self.MiscMod['Disguise'] = StringVar()  
		#self.MiscMod['Escape Artist'] = StringVar()  
		#self.MiscMod['Forgery'] = StringVar()  
		#self.MiscMod['Gather Information'] = StringVar()  
		#self.MiscMod['Handle Animal'] = StringVar()  
		#self.MiscMod['Heal'] = StringVar()  
		#self.MiscMod['Hide'] = StringVar()  
		#self.MiscMod['Intimidate'] = StringVar()  
		#self.MiscMod['Jump'] = StringVar()  
		#self.MiscMod['Knowledge(1)'] = StringVar()  
		#self.MiscMod['Knowledge(2)'] = StringVar()  
		#self.MiscMod['Knowledge(3)'] = StringVar()  
		#self.MiscMod['Knowledge(4)'] = StringVar()  
		#self.MiscMod['Knowledge(5)'] = StringVar()  
		#self.MiscMod['Listen'] = StringVar()  
		#self.MiscMod['Move Silently'] = StringVar()  
		#self.MiscMod['Open Lock'] = StringVar()  
		#self.MiscMod['Perform(1)'] = StringVar()  
		#self.MiscMod['Perform(2)'] = StringVar()  
		#self.MiscMod['Perform(3)'] = StringVar()  
		#self.MiscMod['Profession(1)'] = StringVar()  
		#self.MiscMod['Profession(2)'] = StringVar()  
		#self.MiscMod['Ride'] = StringVar()  
		#self.MiscMod['Search'] = StringVar()  
		#self.MiscMod['Sense Motive'] = StringVar()  
		#self.MiscMod['Sleight of Hand'] = StringVar()  
		#self.MiscMod['Spellcraft'] = StringVar()  
		#self.MiscMod['Spot'] = StringVar()  
		#self.MiscMod['Survival'] = StringVar()  
		#self.MiscMod['Swim'] = StringVar()  
		#self.MiscMod['Tumble'] = StringVar()  
		#self.MiscMod['Use Magic Device'] = StringVar()  
		#self.MiscMod['Use Rope'] = StringVar()  
		#self.MiscMod['Other(1)'] = StringVar()  
		#self.MiscMod['Other(2)'] = StringVar()  
		#self.MiscMod['Other(3)'] = StringVar()  
		
		#self.classSkill['Appraise'] 			= StringVar()  
		#self.classSkill['Balance']				= StringVar()  
		#self.classSkill['Bluff'] 				= StringVar()  
		#self.classSkill['Climb'] 				= StringVar()  
		#self.classSkill['Concentration'] 		= StringVar()  
		#self.classSkill['Craft(1)'] 			= StringVar()  
		#self.classSkill['Craft(2)'] 			= StringVar()  
		#self.classSkill['Craft(3)'] 			= StringVar()  
		#self.classSkill['Decipher Script'] 		= StringVar()  
		#self.classSkill['Diplomacy'] 			= StringVar()  
		#self.classSkill['Disable Device'] 		= StringVar()  
		#self.classSkill['Disguise'] 			= StringVar()  
		#self.classSkill['Disguise'] 			= StringVar()  
		#self.classSkill['Escape Artist'] 		= StringVar()  
		#self.classSkill['Forgery'] 				= StringVar()  
		#self.classSkill['Gather Information'] 	= StringVar()  
		#self.classSkill['Handle Animal'] 		= StringVar()  
		#self.classSkill['Heal'] 				= StringVar()  
		#self.classSkill['Hide'] 				= StringVar()  
		#self.classSkill['Intimidate'] 			= StringVar()  
		#self.classSkill['Jump'] 				= StringVar()  
		#self.classSkill['Knowledge(1)'] 		= StringVar()  
		#self.classSkill['Knowledge(2)'] 		= StringVar()  
		#self.classSkill['Knowledge(3)'] 		= StringVar()  
		#self.classSkill['Knowledge(4)'] 		= StringVar()  
		#self.classSkill['Knowledge(5)'] 		= StringVar()  
		#self.classSkill['Listen'] 				= StringVar()  
		#self.classSkill['Move Silently'] 		= StringVar()  
		#self.classSkill['Open Lock'] 			= StringVar()  
		#self.classSkill['Perform(1)'] 			= StringVar()  
		#self.classSkill['Perform(2)'] 			= StringVar()  
		#self.classSkill['Perform(3)'] 			= StringVar()  
		#self.classSkill['Profession(1)'] 		= StringVar()  
		#self.classSkill['Profession(2)'] 		= StringVar()  
		#self.classSkill['Ride'] 				= StringVar()  
		#self.classSkill['Search'] 				= StringVar()  
		#self.classSkill['Sense Motive'] 		= StringVar()  
		#self.classSkill['Sleight of Hand'] 		= StringVar()  
		#self.classSkill['Spellcraft'] 			= StringVar()  
		#self.classSkill['Spot'] 				= StringVar()  
		#self.classSkill['Survival'] 			= StringVar()  
		#self.classSkill['Swim'] 				= StringVar()  
		#self.classSkill['Tumble'] 				= StringVar()  
		#self.classSkill['Use Magic Device'] 	= StringVar()  
		#self.classSkill['Use Rope'] 			= StringVar()  
		#self.classSkill['Other(1)'] 			= StringVar()  
		#self.classSkill['Other(2)'] 			= StringVar()  
		#self.classSkill['Other(3)'] 			= StringVar()  
		
	def draw(self):
		self.drawHeader()
		self.drawCheckbox()
		self.drawButtons()
		self.drawKeyAbil()
		self.drawSkillMod()
		self.drawEq()
		self.drawAbilMod()
		self.update()
		
	def update(self):
		self.frame.focus_set()
		#self.setbind()
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
		self.LabilMod.grid(row=0, column=4)
		self.Lranks.grid(row=0, column=5)
		self.LmiscMod.grid(row=0, column=6)
			
	def drawCheckbox(self):
		for i, item in enumerate(sorted(self.classSkill)):
			self.CBskill[item] = Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Appraise'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Balance']				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Bluff'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Climb'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Concentration'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Craft(1)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Craft(2)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Craft(3)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Decipher Script'] 	= Checkbutton(self.frame, state=DISABLED)	
		#self.CBskill['Diplomacy'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Disable Device'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Disguise'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Escape Artist'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Forgery'] 			= Checkbutton(self.frame, state=DISABLED)	
		#self.CBskill['Gather Information'] 	= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Handle Animal'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Heal'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Hide'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Intimidate'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Jump'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Knowledge(1)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Knowledge(2)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Knowledge(3)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Knowledge(4)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Knowledge(5)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Listen'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Move Silently'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Open Lock'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Perform(1)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Perform(2)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Perform(3)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Profession(1)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Profession(2)'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Ride'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Search'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Sense Motive'] 		= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Sleight of Hand'] 	= Checkbutton(self.frame, state=DISABLED)	
		#self.CBskill['Spellcraft'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Spot'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Survival'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Swim'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Tumble'] 				= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Use Magic Device'] 	= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Use Rope'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Other(1)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Other(2)'] 			= Checkbutton(self.frame, state=DISABLED)
		#self.CBskill['Other(3)'] 			= Checkbutton(self.frame, state=DISABLED)
		
		for i, item in enumerate(sorted(self.CBskill)):
			self.CBskill[item].grid(row = i+1, column=0, sticky=E+W)
	                                                
	def drawButtons(self):
		self.Bskillname['Appraise'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Appraise")
		self.Bskillname['Balance']				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Balance")
		self.Bskillname['Bluff'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Bluff")
		self.Bskillname['Climb'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Climb")
		self.Bskillname['Concentration'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Concentration")
		self.Bskillname['Craft(1)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Craft(1)")
		self.Bskillname['Craft(2)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Craft(2)")
		self.Bskillname['Craft(3)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Craft(3)")
		self.Bskillname['Decipher Script'] 	    = Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Decipher Script")
		self.Bskillname['Diplomacy'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Diplomacy")
		self.Bskillname['Disable Device'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Disable Device")
		self.Bskillname['Disguise'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Disguise")
		self.Bskillname['Escape Artist'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Escape Artist")
		self.Bskillname['Forgery'] 			    = Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Forgery")
		self.Bskillname['Gather Information'] 	= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Gather Information")
		self.Bskillname['Handle Animal'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Handle Animal")
		self.Bskillname['Heal'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Heal")
		self.Bskillname['Hide'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Hide")
		self.Bskillname['Intimidate'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Intimidate")
		self.Bskillname['Jump'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Jump")
		self.Bskillname['Knowledge(1)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Knowledge(1)")
		self.Bskillname['Knowledge(2)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Knowledge(2)")
		self.Bskillname['Knowledge(3)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Knowledge(3)")
		self.Bskillname['Knowledge(4)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Knowledge(4)")
		self.Bskillname['Knowledge(5)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Knowledge(5)")
		self.Bskillname['Listen'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Listen")
		self.Bskillname['Move Silently'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Move Silently")
		self.Bskillname['Open Lock'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Open Lock")
		self.Bskillname['Perform(1)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Perform(1)")
		self.Bskillname['Perform(2)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Perform(2)")
		self.Bskillname['Perform(3)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Perform(3)")
		self.Bskillname['Profession(1)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Profession(1)")
		self.Bskillname['Profession(2)'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Profession(2)")
		self.Bskillname['Ride'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Ride")
		self.Bskillname['Search'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Search")
		self.Bskillname['Sense Motive'] 		= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Sense Motive")
		self.Bskillname['Sleight of Hand'] 	    = Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Sleight of Hand")
		self.Bskillname['Spellcraft'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Spellcraft")
		self.Bskillname['Spot'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Spot")
		self.Bskillname['Survival'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Survival")
		self.Bskillname['Swim'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Swim")
		self.Bskillname['Tumble'] 				= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Tumble")
		self.Bskillname['Use Magic Device'] 	= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Use Magic Device")
		self.Bskillname['Use Rope'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Use Rope")
		#self.Bskillname['Other(1)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Other(1)")
		#self.Bskillname['Other(2)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Other(2)")
		#self.Bskillname['Other(3)'] 			= Button(self.frame, relief=GROOVE, anchor=W,  width=18, text="Other(3)")
		
		
		for i, item in enumerate(sorted(self.Bskillname)):
			self.Bskillname[item].grid(row = i+1, column=1, sticky=E+W)

	def drawKeyAbil(self):
		self.Lkeyabil['Appraise'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Balance']			= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Bluff'] 				= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Climb'] 				= Label(self.frame,  width=4, text="STR*")
		self.Lkeyabil['Concentration'] 		= Label(self.frame,  width=4, text="CON")
		self.Lkeyabil['Craft(1)'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Craft(2)'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Craft(3)'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Decipher Script'] 	= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Diplomacy'] 			= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Disable Device'] 	= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Disguise'] 			= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Escape Artist'] 		= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Forgery'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Gather Information'] = Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Handle Animal'] 		= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Heal'] 				= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Hide'] 				= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Intimidate'] 		= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Jump'] 				= Label(self.frame,  width=4, text="STR*")
		self.Lkeyabil['Knowledge(1)'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Knowledge(2)'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Knowledge(3)'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Knowledge(4)'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Knowledge(5)'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Listen'] 			= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Move Silently'] 		= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Open Lock'] 			= Label(self.frame,  width=4, text="DEX")
		self.Lkeyabil['Perform(1)'] 		= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Perform(2)'] 		= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Perform(3)'] 		= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Profession(1)'] 		= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Profession(2)'] 		= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Ride'] 				= Label(self.frame,  width=4, text="DEX")
		self.Lkeyabil['Search'] 			= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Sense Motive'] 		= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Sleight of Hand'] 	= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Spellcraft'] 		= Label(self.frame,  width=4, text="INT")
		self.Lkeyabil['Spot'] 				= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Survival'] 			= Label(self.frame,  width=4, text="WIS")
		self.Lkeyabil['Swim'] 				= Label(self.frame,  width=4, text="STR*")
		self.Lkeyabil['Tumble'] 			= Label(self.frame,  width=4, text="DEX*")
		self.Lkeyabil['Use Magic Device'] 	= Label(self.frame,  width=4, text="CHA")
		self.Lkeyabil['Use Rope'] 			= Label(self.frame,  width=4, text="DEX")
		#self.Lkeyabil['Other(1)'] 			= Label(self.frame,  width=4, text="	")
		#self.Lkeyabil['Other(2)'] 			= Label(self.frame,  width=4, text="	")
		#self.Lkeyabil['Other(3)'] 			= Label(self.frame,  width=4, text="	")
		
		for i, item in enumerate(sorted(self.Lkeyabil)):
			self.Lkeyabil[item].grid(row = i+1, column=2, sticky=E+W)
	
	def drawSkillMod(self):
		self.EskillMod['Appraise'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil['INT'])
		self.EskillMod['Balance']			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Bluff'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Climb'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EskillMod['Concentration'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CON"])
		self.EskillMod['Craft(1)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Craft(2)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Craft(3)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Decipher Script'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Diplomacy'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Disable Device'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Disguise'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Escape Artist'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Forgery'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Gather Information']= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Handle Animal'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Heal'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Hide'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Intimidate'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Jump'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EskillMod['Knowledge(1)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Knowledge(2)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Knowledge(3)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Knowledge(4)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Knowledge(5)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Listen'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Move Silently'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Open Lock'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Perform(1)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Perform(2)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Perform(3)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Profession(1)'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Profession(2)'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Ride'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Search'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Sense Motive'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Sleight of Hand'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Spellcraft'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EskillMod['Spot'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Survival'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EskillMod['Swim'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EskillMod['Tumble'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EskillMod['Use Magic Device'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EskillMod['Use Rope'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		#self.EskillMod['Other(1)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		#self.EskillMod['Other(2)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		#self.EskillMod['Other(3)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		 
		for i, item in enumerate(sorted(self.EskillMod)):
			self.EskillMod[item].grid(row = i+1, column=3, sticky=E+W)	
	
	def drawAbilMod(self):
		self.EabilMod['Appraise'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil['INT'])
		self.EabilMod['Balance']			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Bluff'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Climb'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EabilMod['Concentration'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CON"])
		self.EabilMod['Craft(1)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Craft(2)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Craft(3)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Decipher Script'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Diplomacy'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Disable Device'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Disguise'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Escape Artist'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Forgery'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Gather Information'] = Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Handle Animal'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Heal'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Hide'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Intimidate'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Jump'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EabilMod['Knowledge(1)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Knowledge(2)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Knowledge(3)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Knowledge(4)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Knowledge(5)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Listen'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Move Silently'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Open Lock'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Perform(1)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Perform(2)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Perform(3)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Profession(1)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Profession(2)'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Ride'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Search'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Sense Motive'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Sleight of Hand'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Spellcraft'] 		= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["INT"])
		self.EabilMod['Spot'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Survival'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["WIS"])
		self.EabilMod['Swim'] 				= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["STR"])
		self.EabilMod['Tumble'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		self.EabilMod['Use Magic Device'] 	= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["CHA"])
		self.EabilMod['Use Rope'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER, textvariable=self.Mabil["DEX"])
		#self.EabilMod['Other(1)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		#self.EabilMod['Other(2)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		#self.EabilMod['Other(3)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
		  
		for i, item in enumerate(sorted(self.EabilMod)):
			self.EabilMod[item].grid(row = i+1, column=4, sticky=E+W)

	def drawEq(self):
		print "x"
		#for i in self.EabilMod:
		#	self.
		#	
		#self.EabilMod['Other(3)'] 			= Entry(self.frame,  width=3, state=DISABLED, justify=CENTER,)
	
	def bind(self):
		self.CMBvar.bind("<<ComboboxSelected>>", self.setvar)
	
	def setvar(self):
		self.var.set(self.var.get())
		
	def drawButton(self):
		self.Bclose = Button(self.root, text="Save Close", command=self.saveClose)
		self.Bclose.grid(row=0, column=3)
		
	def saveClose(self):
		self.root.withdraw()