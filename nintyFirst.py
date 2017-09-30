from Tkinter import *

root = Tk()

L = []
def file_submission_ADD():
    global L
    L.append(display.get())
    display.delete(0, END)

def file_submission_SAVE():
	global L
	with open("text_submission_GUI.txt", "a+") as fp:
		L.append(display.get())
		for i in L:
			fp.write(i)
		fp.close()
	L = []
	display.delete(0, END)
			
def file_submission_SAVE_and_CLOSE():
	global L
	with open("text_submission_GUI.txt", "a+") as fp:
		L.append(display.get())
		for i in L:
			fp.write(i)
		fp.close() 
	L = []
	root.destroy()

label1 = Button(root, text="Add File", command=file_submission_ADD)
label2 = Button(root, text="Add and Save", command=file_submission_SAVE)
label3 = Button(root, text="Save and Close", command=file_submission_SAVE_and_CLOSE)
display = Entry(root)

label1.grid(row=0, column=1)
label2.grid(row=0, column=2)
label3.grid(row=0, column=3)
display.grid(row=0, column=0)


root.mainloop()
