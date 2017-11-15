# import the necessary library
import tkinter
"""
def main():
    # create main window widget
    main_window = tkinter.Tk()

    # enter main tkinter loop
    tkinter.mainloop()

main()
"""

class MyGUI:
    def __init__(self):
        # main window widget (Should be the first thing in the class
        self.main_window = tkinter.Tk()

        # create a label widget with "Hello World"
        self.label1 = tkinter.Label(self.main_window, text="Hello World!")
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.')


        # Call the pack method for the label; this is the code that actually makes the label visible in the GUI
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')


        # enter main loop (for simple text based programs this should come last in the class)
        tkinter.mainloop()


# create instance of the class
my_gui = MyGUI()
