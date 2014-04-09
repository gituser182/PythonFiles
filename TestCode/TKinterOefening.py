from tkinter import *
#werkt enkel onder Python 3
fen1= Tk()
tex1= Label(fen1, text="Hello TKinter", fg='blue')
tex1.pack()
btn1 = Button(fen1, text="Quit", command = fen1.Destroy)
btn1.pack()
fen1.mainloop()
