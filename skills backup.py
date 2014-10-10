from Tkinter import *
import ttk
import tkMessageBox as msg

class Skills(object):
	def __init__(self, top):
		#self.SKroot = Toplevel()
		self.SKroot.title("Skills")
		self.createVars()
		self.draw()
	
	def createVars(self):
		self.var = StringVar()
		
	def draw(self):
		self.drawHeader()
		self.drawButton()
		self.update()
		
	def update(self):
		self.SKroot.focus_set()
		#self.setbind()
		self.SKroot.mainloop()
		
	def drawHeader(self):
		self.Ltitle = Label(self.SKroot, relief=RIDGE, text="Skills")
		self.Ltitle.grid(row=0, column=0)
		
		self.CMBvar = ttk.Combobox(self.SKroot, width=4, values=[1,2,3], textvariable=self.var)
		self.CMBvar.grid(row=1, column=1) 
			
	def bind(self):
		self.CMBvar.bind("<<ComboboxSelected>>", self.setvar)
	
	def setvar(self):
		self.var.set(self.var.get())
		
	def drawButton(self):
		self.Bclose = Button(self.SKroot, text="Save Close", command=self.saveClose)
		self.Bclose.grid(row=0, column=3)
		
	def saveClose(self):
		self.SKroot.withdraw()