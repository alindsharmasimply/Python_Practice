from Tkinter import *

root = Tk()

status = Label(root, text = "This is the status", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

root.mainloop()