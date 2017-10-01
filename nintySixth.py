from Tkinter import *
import ttk


class HelloApp:
    """docstring for HelloApp"""

    def __init__(self, master):
        self.label = Label(master, text="Hello World!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Germany", command=self.Germany).grid(row=1, column=0, columnspan=1)
        ttk.Button(master, text="India", command=self.India).grid(row=1, column=1, columnspan=1)

    def Germany(self):
        self.label['text'] = "Halo alle"

    def India(self):
        self.label['text'] = "Namaskaar"


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
