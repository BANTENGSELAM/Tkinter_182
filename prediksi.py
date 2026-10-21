
import tkinter as tk
import tkinter.messagebox as msg
top=tk.Tk()

Judul = tk.Label(top, text= "Aplikasi Prediksi Prodi")
Judul.pack()

L1=tk.Label(top,text="MTK: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()


top.mainloop()