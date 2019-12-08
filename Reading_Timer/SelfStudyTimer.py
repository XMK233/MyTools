# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
from win10toast import ToastNotifier

# toaster = ToastNotifier()

root=Tk()
root.wm_attributes('-topmost',1)
root.title("二营长的意大利学习机")
root.geometry("300x50+500+200")#('500x300')

def count_time():
    global b1_run
    global var
    b1['text']='学习真香'
    if not b1_run:
        b1_run=True
        while b1_run:
            time.sleep(0.1)
            var=round(var+0.1,1)
            try:
                l['text']=str(var)
                l.update()
            except:
                break
    else:
        b1_run=False
        b1['text']='学个屁'

def count_zero():
    global var
    if var and not b1_run:
        var=0
        l['text']='0'
def count_back():
    first_run = True
    while float(e.get()):
        if first_run:
            first_run = False
            v=str(round(float(e.get())-0.1,1))
        else:
        	v=str(round(float(r['text'])-0.1,1))
        time.sleep(0.1)
        r['text']=v
        # r.delete(0,END)
        # r.insert(0,v)
        if float(r['text']) == 0.1:
            messagebox.showinfo("张大喵!","给我打下一个精锐!")
       	    # toaster.show_toast("Attension", "Let's start working...")
       	    first_run = True
            continue
        try:
            r.update()
        except:
            break
        # e['text']=v
        # e.delete(0,END)
        # e.insert(0,v)
        # if float(e.get()) == 0.1:
        #     messagebox.showinfo("Time up!","Time up!")
        # try:
        #     e.update()
        # except:
        #     break

var=0

e=Entry(text='0', justify='center')
e.insert(END, '300')
e["width"] = 10
e.pack(side=LEFT)
b3=Button(root,text='学习',command=count_back)
b3.pack(side=LEFT)
r=Label(root,text="Welcome!!")
r.pack(side=LEFT)

l=Label(root,text=str(var))
l.pack(side=RIGHT)
b1_run=False
b1=Button(root,text='学个屁',command=count_time)
b1.pack(side=RIGHT)
b2=Button(root,text='清零',command=count_zero)
b2.pack(side=RIGHT)

mainloop()