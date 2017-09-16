from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo("Title","This is awesome")
response = tkMessageBox.askquestion("Question1","Do you like Coffee?")

if response == 'yes':
	print "Here is a coffee for you"

root.mainloop()