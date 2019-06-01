#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 23:19:18 2019

@author: river
"""
import tkinter as tk
from tkinter import ttk

win=tk.Tk()

win.title("网络连接错误")
ttk.Label(win,text="网络连接错误，请检查你的网络").grid(column=0,row=0)

def click():
	action.configure(text="ok")
	
action=ttk.Button(win,text="确定",command=click)
action.grid(column=0,row=1)

win.mainloop()

