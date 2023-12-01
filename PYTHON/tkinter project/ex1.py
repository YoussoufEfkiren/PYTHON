from tkinter import *
def montant_():
    C = float(entry_capital.get())
    T = float(entry_taux.get())
    D = float(entry_duree.get())

    M=C*(1+T/36500)**(D*365)
    entry_result.delete(0, END)
    entry_result.insert(0, f"{M:.2f}")
root = Tk()
root.title("Tp-Calcul d'interets")

capital = Label(root, text='Capital')
capital.grid(row=0, column=0, padx=10, pady=10)
entry_capital = Entry(root, width=30)
entry_capital.grid(row=0, column=1, padx=10, pady=10)
btn=Button(root,command=montant_,text='calculer',width=10)
btn.grid(row=0,column=2)

capital = Label(root, text='Taux')
capital.grid(row=1, column=0, padx=10, pady=10)
entry_taux = Entry(root, width=30)
entry_taux.grid(row=1, column=1, padx=10, pady=10)
btn=Button(root,text='Fin',width=10)
btn.grid(row=1,column=2)

capital = Label(root, text='Duree')
capital.grid(row=2, column=0, padx=10, pady=10)
entry_duree = Entry(root, width=30)
entry_duree.grid(row=2, column=1, padx=10, pady=10)
btn=Button(root,text='Initialisation',width=10)
btn.grid(row=2,column=2)

capital = Label(root, text='Montant Calcile')
capital.grid(row=3, column=0, padx=10, pady=10)
entry_result = Entry(root, width=30)
entry_result.grid(row=3, column=1, padx=10, pady=10)
btn=Button(root,text='Aide',width=10)
btn.grid(row=3,column=2)

root.mainloop()
