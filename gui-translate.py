from tkinter import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Translator')

        self.tframe = LabelFrame(
            self.root, text='English to Spanish', padx=50, pady=50)
        self.tframe.grid(row=0, column=0, padx=10, pady=10)

        self.eng_title_view = Label(
            self.tframe, text='English Word')
        self.eng_title_view.grid(row=0, column=0)

        self.eng_entry = Entry(self.tframe)
        self.eng_entry.grid(row=1, column=0)
        self.search_btn = Button(
            self.tframe, text='Search', command=self.search)
        self.search_btn.grid(row=1, column=1)

        self.sp_title_view = Label(
            self.tframe, text='Spanish Word')
        self.sp_title_view.grid(row=2, column=0)

        self.sp_entry = Entry(self.tframe)
        self.sp_entry.grid(row=3, column=0)

        self.clear_btn = Button(
            self.tframe, text='Clear', command=self.clear)
        self.clear_btn.grid(row=3, column=1)

        self.root.mainloop()

    def clear(self, eng=True, sp=True):
        print('clear btn')
        if eng:
            self.eng_entry.delete(0, END)
        if sp:
            self.sp_entry.delete(0, END)

    def search(self):
        print('search btn')
        eng_word = self.eng_entry.get()
        print('search > ', eng_word)


GUI()
