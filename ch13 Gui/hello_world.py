import tkinter

class MyGui:
    def __int__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text='Hello world')

        self.label.pack()
        tkinter.mainloop()


my_gui = MyGui()
