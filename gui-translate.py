from tkinter import *
import codecs


class Translator:
    '''
    Translator class 
    Data set : ex1-file
    '''

    def __init__(self) -> None:
        self.eng_list = []
        self.sp_list = []

        self.data = codecs.open(
            "ex1-file", "r", encoding="utf-8").read().split('\n')

    def translate(self, eng_str) -> str:
        # reset and conver to word list.
        self.reset()
        self.eng_list = eng_str.lower().split(' ')

        # translate all words.
        for word in self.eng_list:
            flag = True
            for row in self.data:
                eng_sp = row.split('\t')
                if len(eng_sp) < 2:
                    continue
                if eng_sp[0] == word:
                    self.sp_list.append(eng_sp[1])
                    flag = False
                    break
            if flag:
                self.sp_list.append('NULL')

        # build string and return.
        return self.build_srt()

    def build_srt(self) -> str:
        # merger word list in a string and return
        text = ''
        for word in self.sp_list:
            text += word
            text += ' '
        return text

    def reset(self) -> None:
        # reset
        self.sp_list.clear()
        self.eng_list.clear()


class GUI:
    '''
    GUI for translator
    '''

    def __init__(self) -> None:
        # root
        self.root = Tk()
        self.root.title('Translator')

        # frame
        self.tframe = LabelFrame(
            self.root, text='English to Spanish', padx=50, pady=50)
        self.tframe.grid(row=0, column=0, padx=10, pady=10)

        # eng input label
        self.eng_title_view = Label(
            self.tframe, text='English Word')
        self.eng_title_view.grid(row=0, column=0)

        # eng word text input
        self.eng_entry = Entry(self.tframe)
        self.eng_entry.grid(row=1, column=0)

        # translate button
        self.search_btn = Button(
            self.tframe, text='Search', command=self.search)
        self.search_btn.grid(row=1, column=1)

        # spanish out label
        self.sp_title_view = Label(
            self.tframe, text='Spanish Word')
        self.sp_title_view.grid(row=2, column=0)

        # spanish out text
        self.sp_entry = Entry(self.tframe)
        self.sp_entry.grid(row=3, column=0)

        # clear button
        self.clear_btn = Button(
            self.tframe, text='Clear', command=self.clear)
        self.clear_btn.grid(row=3, column=1)

        # object of Translator class
        self.translator = Translator()

        self.root.mainloop()

    def clear(self, eng=True, sp=True) -> None:
        # clear button action

        # print('clear btn')
        if eng:
            self.eng_entry.delete(0, END)
        if sp:
            self.sp_entry.delete(0, END)

    def search(self) -> None:
        # translate button action

        # print('search btn')
        eng_words = self.eng_entry.get()
        # print('search > ', eng_words)
        # print(self.translator.translate(eng_words))
        self.clear(eng=False)
        self.sp_entry.insert(0, self.translator.translate(eng_words))


GUI()
