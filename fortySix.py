from Tkinter import *

root = Tk()

def doSomething():
	print "You clicked the button"

button1 = Button(root, text = "Click Here", command = doSomething)
button1.pack()

root.mainloop()