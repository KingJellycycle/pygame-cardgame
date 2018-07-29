from tkinter import *


class Display(Frame):
  
    def __init__(self,parent=0):
        Frame.__init__(self,parent)
        self.output = Text(self)
        self.output.pack()
        self.output1 = Text(self)
        self.output1.pack()
        sys.stdout = self
        self.pack()

    def write(self,txt,output=-1):
        if (output == 0):
            self.output.insert(END,str(txt))

        if (output == 1):
            self.output1.insert(END,str(txt))

        if (output == -1):
            self.output.insert(END,str(txt))
            self.output1.insert(END,str(txt))

        
