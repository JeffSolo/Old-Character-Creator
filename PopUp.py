from Tkinter import *
import ttk
import tkMessageBox as msg

class PopUp(object):
	def Bstr(self):
		msg.showinfo("STR", "What is strength, really? - dude, totally add a button on the disabled labels popups to manually edit (such as HP)\nAlso add buttons for age and height, etc and explain averages based on race")
	
	def Bdex(self):
		msg.showinfo("DEX","Dexterity measures hand-eye coordination, agility, reflexes and balance. This ability is the most important one for rogues, but it's also high on the list for characters who typically wear light or medium armor....")
		
	def Bhp(self):
		print "l"
		
	def warn(self, label, err):
		msg.showwarning(label, err)
	
	def error(self, label, err):
		msg.showerror(label, err)