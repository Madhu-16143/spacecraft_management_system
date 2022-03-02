import tkinter  
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image
mydb=mysql.connector.connect(host='localhost',port=3306,user="root",passwd="root16143",database="login",auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
lst1=[]
mycursor.execute("select  name from launchingdetails")
for i in mycursor:
    for j in i:
        lst1.append(j)
print(lst1)
root = Tk(className=" SPACE CRAFT MANAGEMENT SYSTEM")   
root.geometry('700x300')
root.configure(background='black')
root.resizable(width = True, height = True) 
lname=Label(root,text="list of satellites::",bg="magenta",fg="black",font="Times 16").grid(row=0,column=0,sticky=W)
var1 = tkinter.StringVar()
drop = tkinter.OptionMenu(root,var1,*lst1).grid(row=0,column=5,sticky=E)
#print(lst1.get())
set
NameVar=StringVar()
NameVar.set("")
print(NameVar)
name=Label(root,text="enter name ofsatellite::",bg="cyan",fg="black",font="Times 16").grid(row=5,column=0,sticky=W)
namel=Entry(root,bd=5,width=20,textvariable=NameVar,bg="yellow",font="Times 16").grid(row=5,column=5,sticky=E)
print(namel.get())
def cancel():
    root.destroy()
def constraint():
    name=NameVar.get()
    mname=name.upper()
    if mname in lst1:
        def cancel1():
          root.destroy()
        x=mname
        n=""
        m="select image from launchingdetials1 where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            h=i[0];
        img = Image.open(h,mode='r')    
        img = img.resize((250, 250), Image.ANTIALIAS) 
        img = ImageTk.PhotoImage(img) 
        panel = Label(root, image = img)
        panel.image = img 
        panel.grid(row = 10)
        cancel1=Button(root,text="done",width=15,pady=5,bd=3,command=cancel1,bg="cyan").grid(row=2000,column=20,sticky=W)
        z=0
        def cancel1():
            root2.destroy()
        x=mname
        m="select name from launchingdetails where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m1=Label(root,text="name of  satellite::",bg="cyan",fg="black",font="Times 16").grid(row=600,column=0,sticky=W)
            m2=Label(root,text=list(i),bg="magenta",fg="black",font="Times 16").grid(row=600,column=1,sticky=E)
        m="select launchvehicle from launchingdetails where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m3=Label(root,text="launchvehicle of  satellite::",bg="red",fg="white",font="Times 16").grid(row=601,column=0,sticky=W)
            m4=Label(root,text=list(i),bg="green",fg="white",font="Times 16").grid(row=601,column=1,sticky=E)
        m="select missionlife from launchingdetails where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m5=Label(root,text="missionduration of  satellite ::",bg="blue",fg="white",font="Times 16").grid(row=602,column=0,sticky=W)
            m6=Label(root,text=list(i),bg="yellow",fg="black",font="Times 16").grid(row=602,column=1,sticky=E)
        m="select placeoflaunch from launchingdetails where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m7=Label(root,text="placeoflaunch of  satellite::",bg="magenta",fg="black",font="Times 16").grid(row=603,column=0,sticky=W)
            m8=Label(root,text=list(i),bg="cyan",fg="black",font="Times 16").grid(row=603,column=1,sticky=E)
        m="select orbittype from spacecraft where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m9=Label(root,text="orbittype of  satellite::",bg="green",fg="white",font="Times 16").grid(row=604,column=0,sticky=W)
            m10=Label(root,text=list(i),bg="red",fg="white",font="Times 16").grid(row=604,column=1,sticky=E)
        m="select satcatno from spacecraft where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m11=Label(root,text="satellite catalog number::",bg="yellow",fg="black",font="Times 16").grid(row=605,column=0,sticky=W)
            m12=Label(root,text=list(i),bg="blue",fg="white",font="Times 16").grid(row=605,column=1,sticky=E)
            z=i
        p=list(z)
        y=str(p[0])
        m="select applications from landingdetails where satcatno=%(satcatno)s"
        mycursor.execute(m, { 'satcatno':y })
        for i in mycursor:
            m13=Label(root,text="application of  satellite::",bg="cyan",fg="black",font="Times 16").grid(row=606,column=0,sticky=W)
            m14=Label(root,text=list(i),bg="magenta",fg="black",font="Times 16").grid(row=606,column=1,sticky=E)
        m="select dateoflaunch from spacecraft where name=%(name)s"
        mycursor.execute(m, { 'name':x })
        for i in mycursor:
            m15=Label(root,text="dateoflaunch of  satellite::",bg="red",fg="white",font="Times 16").grid(row=607,column=0,sticky=W)
            m16=Label(root,text=list(i),bg="green",fg="white",font="Times 16").grid(row=607,column=1,sticky=E)
        mydb.close()
    else:
        messagebox.showinfo("warning","enter valid satellite name")
done=Button(root,text="submit",width=15,pady=5,bd=3,command=constraint,bg="green").grid(row=2000,column=20,sticky=W)
cancel=Button(root,text="cancel",width=15,pady=5,bd=3,command=cancel,bg="red").grid(row=2000,column=60,sticky=E)
root.mainloop()
