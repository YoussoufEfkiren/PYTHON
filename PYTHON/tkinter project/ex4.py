from tkinter import *
from tkinter import scrolledtext


root= Tk()
root.title('Tp5- conversions')
root.geometry("450x300")

label=Label(text='Debut')
label.grid(row=0,column=0)
entry=Entry()
entry.grid(row=0,column=1)
label=Label(text='Fin')
label.grid(row=0,column=2)
entry=Entry()
entry.grid(row=0,column=3)


text_area = scrolledtext.ScrolledText(root,
                                      wrap=WORD,
                                      width=20,
                                      height=10,
                                      font=("Times New Roman",15))
text_area.grid(row=1,column=1, pady=10, padx=10)

label_frame1 = LabelFrame(root, text="taux")
label_frame1.grid(row=1, column=3, padx=10, pady=10)

radio_option1 = Radiobutton(label_frame1, text="1", value="Option 1")
radio_option1.grid(row=2, column=3, padx=10, pady=10)
radio_option2 = Radiobutton(label_frame1, text="2", value="Option 2")
radio_option2.grid(row=3, column=3, padx=10, pady=10)
radio_option3 = Radiobutton(label_frame1, text="5", value="Option 3")
radio_option3.grid(row=4, column=3, padx=10,pady=10)
radio_option4 = Radiobutton(label_frame1, text="10", value="Option 4")
radio_option4.grid(row=5, column=3, padx=10,pady=10)

btn=Button(root,text='Conversion')
btn.grid(row=6,column=1)
btn=Button(root,text='Fin')
btn.grid(row=6,column=2)




root.mainloop()