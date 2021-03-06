# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
from win10toast import ToastNotifier
from PIL import Image, ImageTk

# toaster = ToastNotifier()

root=Tk()
root.wm_attributes('-topmost',1)
root.title("二营长的意大利学习机")
root.geometry("300x100+500+200")#('500x300')
# win = Toplevel(root)
root.attributes("-alpha", 0.5)

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
        # print(e.get())
        if first_run:
            first_run = False
            v=str(round(float(e.get())*60-0.1,1))
        else:
        	v=str(round(float(r['text'])-0.1,1))
        time.sleep(0.1)

        ## every a certain period of time, change color and font size to remind. 
        v_num = int(float(v))
        if v_num % REMIND_PERIOD in [2, 1, 0, REMIND_PERIOD - 1, REMIND_PERIOD - 2]:
            r['fg'] = "red"
            r['font'] = ('DejaVuSansMono', 20)
        else:
            r['fg'] = "black"
            r['font'] = "TkDefaultFont"
            # r['size'] = '2'

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

REMIND_PERIOD = 300

var=0

## 按钮
b3=Button(root,text='学习',command=count_back)
b3.place(x=0, y = 0)
# b3.pack(side=LEFT)

## 输入分钟数
e=Entry(text='0', justify='center')
e.place(x = 60, y = 0)
e.insert(END, '5')
e["width"] = 10
# e.pack(side=LEFT)

## 一些固定字符显示
l_min=Label(root,text="分钟")
l_min.place(x = 150, y = 0)

## 固定字符显示
r_haisheng = Label(root,text="还剩: ")
# r_haisheng.pack(side=LEFT)
r_haisheng.place(x = 0, y = 30)

## 剩余秒数
r=Label(root,text="Welcome!!")
r.place(x = 70, y = 30)
# r.pack(side=LEFT)

## 一些固定字符显示
l_sec=Label(root,text="秒")
l_sec.place(x = 150, y = 30)

## 暂停学习
b1_run=False
b1=Button(root,text='学个屁',command=count_time)
b1.place(x = 0, y = 60)
# b1.pack(side=RIGHT)

## 
l=Label(root,text=str(var))
# l.pack(side=RIGHT)
l.place(x = 80, y = 60)

## 清零
b2=Button(root,text='清零',command=count_zero)
# b2.pack(side=RIGHT)
b2.place(x = 150, y = 60)

## 装饰图
_ = Image.open("yidalipao.gif")
resized_img = _.resize((90, 90), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_img)
label_img = Label(root, image = img)
label_img.place(x = 200, y = 0)

mainloop()