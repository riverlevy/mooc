import tkinter as tk
from tkinter import ttk
import types
win =tk.Tk()

win.title("字幕程序")

#win.resizable(False,False)
win.resizable(True,True)
#窗体大小可调

ttk.Label(win,text="enter the url:").grid(column =0,row=0)
url=tk.StringVar()
url_entered =ttk.Entry(win,width=30,textvariable=url)
url_entered.grid(column=0,row=1)
input_url=url.get()

ttk.Label(win,text="user:").grid(column =0,row=2)
user=tk.StringVar()
user_entered =ttk.Entry(win,width=30,textvariable=user)
user_entered.grid(column=0,row=3)
input_user=user.get()

ttk.Label(win,text="password:").grid(column =0,row=4)
pwd=tk.StringVar()
pwd_entered =ttk.Entry(win,width=30,textvariable=pwd)
pwd_entered.grid(column=0,row=5)
input_pwd=pwd.get()

#
def click():
	action.configure(text=url.get()+user.get()+pwd.get())
	
action=ttk.Button(win,text="confirm",command=click)
action.grid(column=1,row=5)
url_entered.focus()
#程序一开始就可以输入这个输入框

chvardis =tk.IntVar()
check=tk.Checkbutton(win,text="确认保存",variable=chvardis)
check.select()
#默认选中,
#check.deselect()
#未选中
check.grid(column=1,row=4,sticky=tk.W)
record=chvardis.get()
#保存记录按钮，默认为保存
#int 保存为1
#int 不保存为0


win.mainloop()
#显示窗口1




