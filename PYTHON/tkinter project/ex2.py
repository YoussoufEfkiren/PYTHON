from tkinter import *
root = Tk()
root.title("Knterets")

capital = Label(root, text='Capital')
capital.grid(row=0, column=0)
entry_result = Entry(root, width=30)
entry_result.grid(row=0, column=1, padx=10, pady=10)

var = StringVar()

label_frame = LabelFrame(root, text="Calcul en")
label_frame.grid(row=0, column=2, padx=10, pady=10)

# Create two radio buttons within the LabelFrame
radio_option1 = Radiobutton(label_frame,variable=var, text="Francs", value="Option 11")
radio_option1.grid(row=1, column=2, padx=10, pady=10)

radio_option2 = Radiobutton(label_frame,variable=var, text="Euros", value="Option 23")
radio_option2.grid(row=2, column=2, padx=10, pady=10)





label_frame1 = LabelFrame(root, text="taux")
label_frame1.grid(row=3, column=2, padx=10, pady=10)

radio_option1 = Radiobutton(label_frame1, text="7%", value="Option 211")
radio_option1.grid(row=4, column=2, padx=10, pady=10)
radio_option2 = Radiobutton(label_frame1, text="8%", value="Option 32")
radio_option2.grid(row=5, column=2, padx=10, pady=10)
radio_option3 = Radiobutton(label_frame1, text="9%", value="Option 13")
radio_option3.grid(row=6, column=2, padx=10,pady=10)




root.mainloop()