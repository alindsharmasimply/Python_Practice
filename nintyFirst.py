from Tkinter import *

root = Tk()

L = []
def file_submission_ADD():
    L.append(entry1)

def file_submission_SAVE():
	with open("text_submission_GUI.txt", "a+") as fp:
		L.append(entry1)
		for i in L:
			fp.write(i + '\n')
		fp.close()
	L = []
			
def file_submission_SAVE_and_CLOSE():
	with open("text_submission_GUI.txt", "a+") as fp:
		L.append(entry1)
		for i in L:
			fp.write(i + '\n')
		fp.close()
	L = []

label1 = Button(root, text="Add File", COMMAND=file_submission_ADD)
label2 = Button(root, text="Add and Save", COMMAND=file_submission_SAVE)
label3 = Button(root, text="Save and Close", COMMAND=file_submission_SAVE_and_CLOSE)
entry1 = Entry(root)

label1.grid(row=0, column=1)
label2.grid(row=0, column=2)
label3.grid(row=0, column=3)
entry1.grid(row=0, column=0)


root.mainloop()
