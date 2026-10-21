# import tkinter as tk
# import tkinter.messagebox as msg
# top = tk.Tk() 

# # Code to add widgets will go here... 
# def helloCallback():
#     msg.showinfo("Hello Python!", "HI")

# w=tk.Button(top,text="Hello!", command=helloCallback)
# w.pack()

# top.mainloop() 


# import tkinter as tk
# from tkinter import messagebox

# top = tk.Tk()
# C = tk.Canvas(top, bg="blue", height=250, width=300)
# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")
# C.pack()
# top.mainloop() 


# import tkinter as tk
# from tkinter import messagebox
# top = tk.Tk()
# CheckVar1 = tk.IntVar()
# CheckVar2 = tk.IntVar()
# C1 = tk.Checkbutton(top, text="Music", variable=CheckVar1,
# onvalue=1, offvalue=0, height=5, width=20)
# C2 = tk.Checkbutton(top, text="Video", variable=CheckVar2,
# onvalue=1, offvalue=0, height=5, width=20)
# C1.pack()
# C2.pack()
# top.mainloop()


# import tkinter as tk
# top = tk.Tk()
# L1 = tk.Label(top, text="User Name")
# L1.pack(side=tk.LEFT)
# E1 = tk.Entry(top, bd=5)
# E1.pack(side=tk.RIGHT)
# top.mainloop()


# import tkinter as tk

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
# bottomframe = tk.Frame(root)
# bottomframe.pack(side=tk.BOTTOM)
# redbutton = tk.Button(frame, text="Red", fg="red")
# redbutton.pack(side=tk.LEFT)
# greenbutton = tk.Button(frame, text="Brown", fg="brown")
# greenbutton.pack(side=tk.LEFT)
# bluebutton = tk.Button(frame, text="Blue", fg="blue")
# bluebutton.pack(side=tk.LEFT)
# blackbutton = tk.Button(bottomframe, text="Black", fg="black")
# blackbutton.pack(side=tk.BOTTOM)
# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# var = tk.StringVar()
# label = tk.Label(root, textvariable=var, relief=tk.RAISED)
# var.set("Hey!? How are you doing?")
# label.pack()

# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# top = tk.Tk()
# Lb1 = tk.Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
# Lb1.pack()
# top.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# top = tk.Tk()
# mb = tk.Menubutton(top, text="condiments", relief=tk.RAISED)
# mb.grid()
# mb.menu = tk.Menu(mb, tearoff=0)
# mb["menu"] = mb.menu
# mayoVar = tk.IntVar()
# ketchVar = tk.IntVar()
# mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
# mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

# mb.pack()
# top.mainloop()


# import tkinter as tk

# def sel():
#     selection = "You selected the option " + str(var.get())
#     label.config(text=selection)
# root = tk.Tk()
# var = tk.IntVar()
# R1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
# R1.pack(anchor=tk.W)
# R2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
# R2.pack(anchor=tk.W)
# R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
# R3.pack(anchor=tk.W)
# label = tk.Label(root)
# label.pack()
# root.mainloop()

import tkinter as tk
import tkinter.messagebox as msg
top=tk.Tk()
CheckVar1=tk.StringVar()
CheckVar1.set("Cantik")
C=tk.Checkbutton(top,text="Gender, check kalau laki2", variable=CheckVar1, onvalue="Tampan", offvalue="Cantik", height=5)
C.pack()
L1=tk.Label(top,text="Nama: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()
def helloCallBack():
    msg.showinfo("Belajara GUI","Sup "
                 +E1.get()+"! Kamu " +CheckVar1.get()+ " Sekali hari ini!")
w1=tk.Button(top,text="Klik saya!", command=helloCallBack)
w1.pack()
top.mainloop()