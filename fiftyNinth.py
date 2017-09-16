from Tkinter import *

root = Tk()

canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

newline = canvas.create_line(0,0,100,100)
otherline = canvas.create_line(0,0,200,50,fill = "red")

root.mainloop()