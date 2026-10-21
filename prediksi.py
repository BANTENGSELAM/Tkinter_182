
import tkinter as tk
import tkinter.messagebox as msg
top=tk.Tk()

Judul = tk.Label(top, text= "Aplikasi Prediksi Prodi")
Judul.pack()

L1=tk.Label(top,text="MTK: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()


L1=tk.Label(top,text="Bahasa Indonesia: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="Bahasa Inggris: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="Informatika: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="IPA: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="IPS: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="Prakarya: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="Penjas: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="PAI: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

L1=tk.Label(top,text="Mekanika Fluida: ");L1.pack()
E1=tk.Entry(top,bd=5);E1.pack()

def helloCallBack():
    msg.showinfo("Hasil Kemungkinan Prodi :  ", 
                 "TEKNOLOGI INFORMASI")
    
top.mainloop()