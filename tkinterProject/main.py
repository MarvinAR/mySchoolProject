#import tkinter
from tkinter import Tk, ttk

#membuat sebuah instance / object nyata
my_apps = Tk()

#title itu method (fungsi di dlm objek) didalam object Tk()
my_apps.title("My first Python apps")

#supaya windowsnya tidak bisa di resize
my_apps.resizable(True, True)

#menambahkan label / tulisan 
label1 = ttk.Label(my_apps, text = "Nama Lengkap \t:")
label1.grid(column = 0, row = 0)
label2 = ttk.Label(my_apps, text = "Marvin Alvianus Rainhard\t\t")
label2.grid(column = 1, row = 0)

label3= ttk.Label(my_apps, text = "Tanggal lahir \t:")
label3.grid(column = 0, row = 1)
label4 = ttk.Label(my_apps, text = "19 Maret 2007\t\t\t")
label4.grid(column = 1, row = 1)

label5 = ttk.Label(my_apps, text = "Alamat \t\t:")
label5.grid(column = 0, row = 2)
label6 = ttk.Label(my_apps, text = "Jalan Puncak Sekuning no.758\t")
label6.grid(column = 1, row = 2)

label7 = ttk.Label(my_apps, text = "Umur \t\t:")
label7.grid(column = 0, row = 3)
label8 = ttk.Label(my_apps, text = "13 Tahun\t\t\t")
label8.grid(column = 1, row = 3)

label9 = ttk.Label(my_apps, text = "Tempat lahir \t:")
label9.grid(column = 0, row = 4)
label10 = ttk.Label(my_apps, text = "Palembang\t\t\t")
label10.grid(column = 1, row = 4)

def change_color():
	button1.configure(text = "Color has been changed")
	label1.configure(foreground = "red")
	label2.configure(foreground = "red")
	label3.configure(foreground = "red")
	label4.configure(foreground = "red")
	label5.configure(foreground = "red")
	label6.configure(foreground = "red")
	label7.configure(foreground = "red")
	label8.configure(foreground = "red")
	label9.configure(foreground = "red")
	label10.configure(foreground = "red")
#membuat tombol / button
button1 = ttk.Button(my_apps, text = "Change Color", command = change_color)
button1.grid(row = 5, column = 0)

#method untuk memulai GUI apps
if  __name__ == "__main__":
	my_apps.mainloop()