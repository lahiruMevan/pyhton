import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window,
        text = 'Click Me!',command=self.do_something)

        self.my_button.pack()
        tkinter.mainloop()

    
    def do_something(self):
        tkinter.messagebox.showinfo('Response','Thanks for clicking the button')

my_gui = MyGUI()


