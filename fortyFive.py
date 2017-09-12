from Tkinter import *

root = Tk()

label1 = Label(root, text = "First", bg = "BLACK", fg = "GREEN")
label1.pack(fill = X)

label2 = Label(root, text = "Second", bg = "BLUE", fg = "WHITE")
label2.pack(side = LEFT, fill = Y)

root.mainloop()