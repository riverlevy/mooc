import tkinter as tk
from tkinter import ttk
win =tk.Tk()

win.title("字幕程序")

#win.resizable(False,False)
win.resizable(True,True)
#窗体大小可调

#ttk.Label(win,text='A label').grid(column=0,row=0)

a_label=ttk.Label(win,text="S label")
a_label.grid(column=0,row=0)
def click():
	action.configure(text="** I have been clicked")
	a_label.configure(foreground ='red')
	#the ziti red
	#background red   diffrent
	a_label.configure(text="A red label")

action=ttk.Button(win,text="click me",command=click)
action.grid(column=1,row=0)
win.mainloop()
