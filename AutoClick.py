# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:25:53 2024

@author: 318-yan
"""

import tkinter as tk
import pyautogui
import keyboard as kb
import time
from tkinter import ttk 


left_time=0
status='on'

def disrup():
    global status
    if kb.is_pressed('ESC'):
        status='off'


def time_wait(t):
    global left_time
    global status
    
    t=int(t)
    while t>0:
        left_time=t
        time_lab= tk.Label(tab1,text=str(left_time)+'s for next click')
        time_lab.place(x=250, y=420)
        
        time.sleep(1)
        t-=1
        baseGround.update()
        disrup()
        if status=='off':
            break
        pass
        
    
    
    
def get_mouse_position():
    time.sleep(2)
    po=str(pyautogui.position())
    messa=('x,y ='+po)
    tk.messagebox.showwarning(title=' ', message=messa)
    f=po.split()
    f1=f[0]
    f2=f[1]
    num1=""
    for s1 in f1:
        if s1. isdigit():
            num1=num1+s1
                    
    num2=""
    for s2 in f2:
        if s2. isdigit():
            num2=num2+s2
            
    X_co.delete(0, tk.END) 
    Y_co.delete(0, tk.END) 
    X_co.insert(0,num1)
    Y_co.insert(0,num2)
    
  
    
def Au_click():
        xc_=X_co.get()
        yc_=Y_co.get()
        xc=int(xc_)
        yc=int(yc_)
        fre=Freq_inp.get()
        fre=int(fre)
        while fre>0:
            global status
            if status=='off':
                break
            pyautogui.click(xc, yc)
            time.sleep(0.5) #Click interval during 1 cycle, it can be changed depends on situation
            fre-=1
            disrup()
            
def main():
    try:
        global status
        status='on'
   
        cyc_=Cyc.get()
        xc_=X_co.get()
        yc_=Y_co.get()
        interval=time_.get()
        freq=Freq_inp.get()
        time.sleep(2)
        if cyc_=='' or xc_=='' or yc_=='' or interval=='' or freq == '':
            pass
        else:
            cyc_=int(cyc_)
            interval=int(interval)
            try:
                while cyc_>1:
                    disrup()
                    if status=='off':
                        break
                    Au_click()
                    time_wait(interval)
                    cyc_-=1
                Au_click()
                
                tk.messagebox.showwarning(title=' ', message='Auto click finished')
  
            except:
                tk.messagebox.showwarning(title=' ', message='Stop by user')
    except:
        tk.messagebox.showwarning(title=' ', message='Error')
  
    
baseGround = tk.Tk()
baseGround.geometry('400x500')
baseGround.title('Auto click')
tabControl = ttk.Notebook(baseGround) 
tab1 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='1 phase ') 
tabControl.pack(expand = True, fill ="both") 

X_co_lab= tk.Label(tab1,text='X')
X_co_lab.place(x=30, y=55)
X_co = tk.Entry(tab1,width=10)
X_co.place(x=30, y=90)

Y_co_lab= tk.Label(tab1,text='Y')
Y_co_lab.place(x=30, y=125)
Y_co = tk.Entry(tab1,width=10)
Y_co.place(x=30, y=160)

Freq_lab= tk.Label(tab1,text='Click count')
Freq_lab.place(x=30, y=195)
Freq_inp = tk.Entry(tab1,width=10)
Freq_inp.place(x=30, y=230)

Cyc_lab= tk.Label(tab1,text='Cycle')
Cyc_lab.place(x=30, y=265)
Cyc = tk.Entry(tab1,width=10)
Cyc.place(x=30, y=300)

time_lab= tk.Label(tab1,text='Interval')
time_lab.place(x=30, y=335)
time_ = tk.Entry(tab1,width=10)
time_.place(x=30, y=370)


btn1 = tk.Button(tab1,text = 'Start',
                command=main).place(x=30, y=420)
btn2 = tk.Button(tab1, text = 'get mouse position',
                command=get_mouse_position).place(x=150, y=80)


baseGround.mainloop()
