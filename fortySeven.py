from Tkinter import *

class myButtons(object):
	"""docstring for myButtons"""
	def __init__(self, root1):

		frame = Frame(root1)
		frame.pack()

		self.printButton = Button(frame, text = "Click Here to print", command = self.display)
		self.printButton.pack()
		
		self.quitButton = Button(frame, text = "Click Here to quit", command = frame.quit)
		self.quitButton.pack(side = LEFT)

	def display(self):
		print "Button Clicked"

root = Tk()

b = myButtons(root)

root.mainloop()