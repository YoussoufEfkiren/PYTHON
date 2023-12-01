from tkinter import scrolledtext
from tkinter import *


# creating tkinter window
root = Tk()
root.title('Tp4 Equations')
root.geometry("400x250")
# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
action = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Action', menu = action)
action.add_command(label ='Effacer')
action.add_command(label ='Quitter')


# Adding Edit Menu and commands
equation = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Equation', menu = equation)
equation.add_command(label ='1er degre')
equation.add_command(label ='2eme degre')


# Adding Help Menu
info_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Information', menu = info_)
info_.add_command(label ='Date')
info_.add_command(label ='Heure')

# display Menu
root.config(menu = menubar)


a=Label(text='A',font=('poppins,20'),foreground='red')
a.grid(row=0,column=0)
entry=Entry()
entry.grid(row=0,column=1,)
label =Label(root, text="1er degre--> A,B",font=('poppins,20'),background='yellow')
label.grid(row=0,column=2,padx=20)


b=Label(text='B',font=('poppins,20'),foreground='red')
b.grid(row=1,column=0)
entry=Entry()
entry.grid(row=1,column=1,)
label =Label(root, text="2eme degre--> A,B,C",font=('poppins,20'),background='yellow')
label.grid(row=1,column=2,padx=20)

c=Label(text='C',font=('poppins,20'),foreground='red')
c.grid(row=2,column=0)
entry=Entry()
entry.grid(row=2,column=1,)


label=Label(text='Resultats',font='poppins,20',foreground='red')
label.grid(row=6,column=1)
entry=Entry()
entry.grid(row=6,column=2)
text_area = scrolledtext.ScrolledText(root,
                                      wrap=WORD,
                                      width=15,
                                      height=5,
                                      font=("Times New Roman",15))

text_area.grid(row=6,column=2, pady=10, padx=10)
mainloop()
