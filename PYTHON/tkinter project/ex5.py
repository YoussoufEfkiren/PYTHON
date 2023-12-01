from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.title('Tp6-Analyse de chaine de caracteres')

label=Label(root,text='Saisir une chaine de caracteres',font='poppins,20')
label.grid(row=0,column=0)
entry=Entry(width=40)
entry.grid(row=1,column=0)

label=Label(root,text='type de recherche',font='poppins,20')
label.grid(row=2,column=0)


options = ["", "Voyelles", "Cosonnes","Chiffres","Speciaux"]
combobox =Combobox(root,values=options, state="readonly")
combobox.grid(row=2,column=1)

btn=Button(text='afficher')
btn.grid(row=4,column=0,padx=15,pady=15)
btn=Button(text='afficher')
btn.grid(row=4,column=1,padx=15,pady=15)
btn=Button(text='afficher')
btn.grid(row=4,column=2,padx=15,pady=15)

# Set a default option
combobox.set(options[0])




root.mainloop()