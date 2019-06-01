#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 23:27:49 2019

@author: river
"""

import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("下载成功")
ttk.Label(win,text="下载已完成").grid(column=0,row=0)
def click():
	action.configure(text="666")
	
action=ttk.Button(win,text="确定",command=click)
action.grid(column=0,row=1)

win.mainloop()
