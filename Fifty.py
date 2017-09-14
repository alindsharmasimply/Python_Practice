from Tkinter import *

def function1():
	print "Menu item clicked"

root = Tk()

myMenu = Menu(root)
root.config(menu = myMenu)

subMenu1 = Menu(myMenu)
myMenu.add_cascade(label = "File", menu = subMenu1)
subMenu1.add_command(label = "Project", command = function1)
subMenu1.add_command(label = "Save", command = function1)

subMenu1.add_separator()
subMenu1.add_command(label = "Exit", command = function1)

subMenu2 = Menu(myMenu)
myMenu.add_cascade(label = "Edit", menu = subMenu2)
subMenu2.add_command(label = "Cut", command = function1)
subMenu2.add_command(label = "Copy", command = function1)

root.mainloop()