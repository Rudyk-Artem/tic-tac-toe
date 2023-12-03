from random import randrange
from tkinter import *
g=randrange(1,3)
p=[0]*9
pf=['','O','X']
f=False
def inff(event):
    global f
    if(f):
        return
    global g
    global c
    for i in range(len(str(event))):
        if(str(event)[i:i+2]=='x='):
            d=str(event)[i+2:-1]
            break
    for i in range(len(d)):
        if(d[i]==' '):
            x=int(d[:i])
    for i in range(len(d)):
        if(d[i]=='='):
            y=int(d[i+1:])
    if(g==1):
        for i in range(3):
            for j in range(3):
                if(17+j*117<x and x<117+j*117 and 17+i*117<y and y<117+i*117):
                    if(p[i*3+j]==0):
                        p[i*3+j]=1
                        g=2
    if(g==2):
        for i in range(3):
            for j in range(3):
                if(17+j*117<x and x<117+j*117 and 17+i*117<y and y<117+i*117):
                    if(p[i*3+j]==0):
                        p[i*3+j]=2
                        g=1
    l3['text']=pf[p[0]]
    l4['text']=pf[p[1]]
    l5['text']=pf[p[2]]
    l6['text']=pf[p[3]]
    l7['text']=pf[p[4]]
    l8['text']=pf[p[5]]
    l9['text']=pf[p[6]]
    l10['text']=pf[p[7]]
    l11['text']=pf[p[8]]
    l3['fg']='#000044'
    l4['fg']='#000044'
    l5['fg']='#000044'
    l6['fg']='#000044'
    l7['fg']='#000044'
    l8['fg']='#000044'
    l9['fg']='#000044'
    l10['fg']='#000044'
    l11['fg']='#000044'
    pp=p
    for i in range(3):
        if(pp[i*3]==pp[i*3+1]==pp[i*3+2]!=0):
            if(i==0):
                l3['fg']='#fdd017'
                l4['fg']='#fdd017'
                l5['fg']='#fdd017'
            if(i==1):
                l6['fg']='#fdd017'
                l7['fg']='#fdd017'
                l8['fg']='#fdd017'
            if(i==2):
                l9['fg']='#fdd017'
                l10['fg']='#fdd017'
                l11['fg']='#fdd017'
            f=True
    for i in range(3):
        if(pp[0+i]==pp[3+i]==pp[6+i]!=0):
            if(i==0):
                l3['fg']='#fdd017'
                l6['fg']='#fdd017'
                l9['fg']='#fdd017'
            if(i==1):
                l4['fg']='#fdd017'
                l7['fg']='#fdd017'
                l10['fg']='#fdd017'
            if(i==2):
                l5['fg']='#fdd017'
                l8['fg']='#fdd017'
                l11['fg']='#fdd017'
            f=True
    if(pp[0]==pp[4]==pp[8]!=0):
        l3['fg']='#fdd017'
        l7['fg']='#fdd017'
        l11['fg']='#fdd017'
        f=True
    if(pp[2]==pp[4]==pp[6]!=0):
        l5['fg']='#fdd017'
        l7['fg']='#fdd017'
        l9['fg']='#fdd017'
        f=True
    ca=True
    for i in range(9):
        if(p[i]==0):
            ca=False
    if(ca and not(f)):
        l3['fg']='#ccc'
        l4['fg']='#ccc'
        l5['fg']='#ccc'
        l6['fg']='#ccc'
        l7['fg']='#ccc'
        l8['fg']='#ccc'
        l9['fg']='#ccc'
        l10['fg']='#ccc'
        l11['fg']='#ccc'
        f=True

My_window=Tk()
My_window.title("×0")
My_window.geometry("350x350")
My_window["bg"]="#88ddff"
c=Canvas(My_window,width=350,height=350,bd=1,bg='#55aaff')
c.place(x=-2,y=-2)
c.create_rectangle(17,17,117,117,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(127,17,227,117,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(237,17,337,117,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(17,127,117,227,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(127,127,227,227,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(237,127,337,227,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(17,237,117,337,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(127,237,227,337,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(237,237,337,337,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
l3=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l4=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l5=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l6=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l7=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l8=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l9=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l10=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l11=Label(My_window,text=f'{pf[g]}',fg="#2a8fff",bg="#2288ff",font=("Arial",55))
l3.place(x=36,y=22)
l4.place(x=146,y=22)
l5.place(x=256,y=22)
l6.place(x=36,y=132)
l7.place(x=146,y=132)
l8.place(x=256,y=132)
l9.place(x=36,y=242)
l10.place(x=146,y=242)
l11.place(x=256,y=242)
c.bind('<Button-1>',inff)
My_window.mainloop() 