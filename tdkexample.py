from Tkinter import *
import ttk
import tkMessageBox as msg

root= Tk()


choice_var = StringVar()
choices = ['lion', 'tigerbear']
combo = ttk.Combobox(root, textvariable=choice_var, values=choices)
combo.pack()
def clicked():
    print combo.get()
btn = Button(root, text="click", command=clicked)
btn.pack()
'''
cbox = Checkbutton(text="cwap")
cbox['state'] = DISABLED
cbox.pack()
'''
'''
choice_var = StringVar()
choices = ['lion', 'tigerbear']
opt_menu = OptionMenu(root, choice_var, *choices)
choice_var = choices[0]
opt_menu.pack()
'''
'''
cboxval = IntVar()

def clicked():
    msg.showinfo("click!", "teehee")
    btn['text'] = ":D"

def click2():
    msg.showinfo("oh no", "you didn't!")
    btn2['text'] = ":("

def cbox_click():
    if cboxval.get() == 1:
        msg.showinfo("check", ":)")
    else:
        msg.showwarning("uncheck", ":(")

cbox = Checkbutton(root,text="Disable?", variable=cboxval, command=cbox_click)
btn = Button(root, text="Hellor!", command=clicked)
btn2 = Button(root, text="beware!", command=click2)
btn3 = Button(root, text="ddg", command=click2)
btn.grid(row=0, column=0)
btn2.grid(row=3, column=5)
btn3.grid(row=5, column=2)
cbox.grid()

'''
'''
cvt_from = StringVar()
cvt_to = StringVar()

def do_convert():
    try:
        feet_val = float(cvt_from.get())
        meters_val = feet_val * .3048
        cvt_to.set('%s meters' % meters_val)
    except ValueError:
        msg.showerror("Bad Input!", "Do better")

lbl = Label(root, text='Convert from feet to meters:')
lbl.grid(row=0, column=0, columnspan=2)

from_lbl = Label(root, text='Enter feet:')
from_lbl.grid(row=1, column=0)

from_entry = Entry(root, textvariable=cvt_from)
from_entry.grid(row=1, column=1)

to_lbl = Label(root, text='Result:')
to_lbl.grid(row=2, column=0)

result_lbl=Label(root, textvariable=cvt_to)
result_lbl.grid(row=2, column=1)

convert_btn = Button(root, text='Convert!', command=do_convert)
convert_btn.grid(row=3, column=1)
'''
root.mainloop()

