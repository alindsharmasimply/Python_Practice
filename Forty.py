from Tkinter import *

root = Tk()

newFrame = Frame(root)
newFrame.pack()

otherFrame = Frame(root)
otherFrame.pack(side = BOTTOM)

button1 = Button(newFrame,text = "Click Here", fg="Red")
button2 = Button(otherFrame, text = "Click Here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()