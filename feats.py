from Tkinter import *
import ttk
import tkMessageBox as msg

class Feats(object):
	def __init__(self, root):
		self.root = root
		self.root.protocol("WM_DELETE_WINDOW", self.saveClose)
		self.root.title("Feats")
		self.root.geometry("500x650")
		self.createVars()
		self.draw()
	
	def createVars(self):
		self.var = StringVar()
		
	def draw(self):
		self.drawHeader()
		self.update()
		
	def update(self):
		self.root.focus_set()
		#self.setbind()
		self.root.mainloop()
		
	def drawHeader(self):
		self.Btitle = Label(self.root, relief=RIDGE, text="Feats")
		self.Btitle.grid(row=0, column=0)
			
	def saveClose(self):
		self.root.withdraw()