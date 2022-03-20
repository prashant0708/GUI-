#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter
tw=tkinter.Tk()
tw.mainloop()


# In[10]:


from tkinter import *
root=Tk()
root.geometry('200x200')
b1=Button(root,text='Click me')
b1.pack
root.mainloop()


# In[11]:


from tkinter import *

def changecolor(e):
    root.config(bg="red")

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
b1.bind("<Button-1>",changecolor)
b1.pack()
root.mainloop()


# In[14]:


from tkinter import *
oldcolor=""

def enterkey(e):
    root.config(bg="red")

def escapekey(e):
    root.config(bg="SystemButtonFace")

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
root.bind("<Return>",enterkey)
root.bind("<Escape>",escapekey)
oldcolor=root["bg"]
print(oldcolor)
b1.pack()
root.mainloop()


# In[16]:


from tkinter import *
def changecolor(e):
    ch=e.char
    if ch=="r":
       root.config(bg="red")
    elif ch=="b":
        root.config(bg="blue")
    elif ch=="g":
        root.config(bg="green")

root = Tk()
root.geometry('200x200')
root.bind("<Key>",changecolor)
root.mainloop()


# In[21]:


from tkinter import *
root = Tk()
root.geometery('200x600')
l1=Label(root, text="First Name")
l2=Label(root, text="Last Name")
e1 = Entry(root)
e2 = Entry(root)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.mainloop( )


# In[23]:


from tkinter import *
def finish():
    root.destroy()

def show():
    fname = e1.get()
    lname = e2.get()
    fullname = fname +" "+lname
    l3.config(text = fullname)
root = Tk()
l1=Label(root, text="First Name")
l2=Label(root, text="Last Name")
l3=Label(root,width=20,anchor=W,font="Arial 10 bold")
e1 = Entry(root)
e2 = Entry(root)
b1=Button(root, text='Show', command=show)
b2=Button(root, text='Quit', command=finish)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
l3.grid(row=2,columnspan=2,sticky=W)
b1.grid(row=3, column=0, sticky=W, pady=4)
b2.grid(row=3, column=1, sticky=W, pady=4)
root.mainloop( )


# In[ ]:





# In[24]:


from tkinter import *
def divide():
    a = float(e1.get())
    b = float(e2.get())
    divide = a/b
    e3.insert(0,divide)
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
def finish():
    root.destroy()
root = Tk()
root.geometry('400x200+100+200')
l1=Label(root, text="Number Division Program",font="Arial 18 bold")
l2=Label(root, text="First No:")
l3=Label(root, text="Second No:")
l4=Label(root,text="Result:")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="Divide",command=divide)
b2=Button(root,text="Clear",command=clear)
b3=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
l4.grid(row=3,column=0,sticky=E)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
root.mainloop()


# In[26]:


from tkinter import *
from tkinter import messagebox

def divide():
    try:
        e3.delete(0, END)
        a=int(e1.get())
        b=int(e2.get())
        c=a/b
        e3.insert(0,str(c))
    except ZeroDivisionError:
        messagebox.showerror("Arithmetic Error!","Denominator should not be positive!")
    except ValueError:
        messagebox.showerror("Conversion Error!", "Only digits allowed!")
    
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    
def finish():
    root.destroy()
    
root = Tk()
root.geometry('400x200+100+200')
l1=Label(root, text="Number Division Program",font="Arial 18 bold")
l2=Label(root, text="First No:")
l3=Label(root, text="Second No:")
l4=Label(root,text="Result:")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="Divide",command=divide)
b2=Button(root,text="Clear",command=clear)
b3=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
l4.grid(row=3,column=0,sticky=E)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
root.mainloop()


# In[27]:


from tkinter import *
#from tkinter import messagebox
def divide():
    try:
        e3.delete(0, END)
        a=int(e1.get())
        b=int(e2.get())
        c=a/b
        e3.insert(0,str(c))
    except ZeroDivisionError:
        messagebox.showerror("Arithmetic Error!","Denominator should not be positive!")
    except ValueError:
        messagebox.showerror("Conversion Error!", "Only digits allowed!")
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0,END)
    e1.focus()
    root.config(bg=oldcolor) # correct this code remove green colour after first execution

def finish():
    answer = messagebox.askokcancel("Quitting!", "Are you sure you want to quit?")
    if answer==True:
        root.destroy()

root = Tk()
root.geometry('400x200+100+200')
l1=Label(root, text="Number Division Program",font="Arial 18 bold")
l2=Label(root, text="First No:")
l3=Label(root, text="Second No:")
l4=Label(root,text="Result:")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="Divide",command=divide)
b2=Button(root,text="Clear",command=clear)
b3=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
l4.grid(row=3,column=0,sticky=E)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
root.mainloop()


# In[28]:


from tkinter import *
from tkinter import filedialog, messagebox
def showopen():
  file_name=filedialog.askopenfilename(title="Select your fav song",filetypes=[("mp3 files","*.mp3")])
  if file_name!="":
    messagebox.showinfo("Your selections",file_name)
  else:
    messagebox.showinfo("Your selections", "You did not select any file")
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=showopen)
btn.pack()
root.mainloop()


# In[29]:


from tkinter import *
from tkinter import colorchooser, messagebox

def showopen():
  chosen_color=colorchooser.askcolor(color="#ff0000",title="Select a color")
  if chosen_color[0] is None:
    messagebox.showinfo("Color","No color selected")
  else:
    root.configure(bg=chosen_color[1])
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Choose Color",command=showopen)
btn.pack()
root.mainloop()


# In[31]:


from tkinter import *

def changecolor():
    if x.get()==1:
        root.configure(bg="#ff0000")
    else:root.configure(bg=old_color)

root = Tk()
root.geometry("200x200")
old_color=root["bg"]
x=IntVar()
cb=Checkbutton(root,text="Red",command=changecolor,variable=x)
cb.pack()
root.mainloop()


# In[32]:


from tkinter import *
from tkinter import messagebox


def showgender():
    value=x.get()
    if value==1:
        messagebox.showinfo("Gender","You selected Male")
    else:
        messagebox.showinfo("Gender", "You selected Female")

root = Tk()
root.geometry("200x200")
x=IntVar()
l1=Label(root,text="Select your gender")
rb1=Radiobutton(root,text="Male",command=showgender,variable=x,value=1)
rb2=Radiobutton(root,text="Female",command=showgender,variable=x,value=2)
l1.grid(row=0,column=0)
rb1.grid(row=1,column=0,sticky=W)
rb2.grid(row=2,column=0,sticky=W)

root.mainloop()


# In[34]:


from tkinter import *
root = Tk()
root.geometry("200x200")
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]
pos=0
for x in sports:
    lb1.insert(pos,x)
    pos=pos+1
lb1.grid(row=1,column=0,sticky=W)
root.mainloop()


# In[35]:


from tkinter import *
from tkinter import simpledialog,messagebox

def show_item():
    pos=simpledialog.askinteger("Input","Enter item no",minvalue=1,maxvalue=lb1.size())
    if type(pos) is int:
        item=lb1.get(pos-1)
        l1.configure(text="You selected:"+item)
    else:
        messagebox.showinfo("Cancel Pressed!","You didn't input any value")
root = Tk()
root.geometry("300x300")
l1=Label(root,text="Your selection will appear here")
b1=Button(root,text="show item",command=show_item)
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]
for x in sports:
    lb1.insert(END,x)

lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop()


# In[39]:


from tkinter import *
def set_red_color(val):
    red=hex(int(val))
    red=red[2:]
    if len(red)==1:
        red="0"+red
    color="#"+red+"0000"
    root.configure(bg=color)
root = Tk()
root.geometry('200x200')
sc=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_red_color)
sc.pack()
root.configure(bg="#000")
root.mainloop()


# In[ ]:




