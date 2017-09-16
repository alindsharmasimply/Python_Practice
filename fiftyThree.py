from Tkinter import *

root = Tk()

def function():
	print "Ye Waala"

toolbar = Frame(root, bg = "blue")
insertbutton = Button(toolbar, text = "Insert file", command = function)
insertbutton.pack(side = LEFT,padx = 2, pady = 3)

printbutton = Button(toolbar, text = "Print file", command = function)
printbutton.pack(side = LEFT)

toolbar.pack(side = TOP, fill = X)
root.mainloop()