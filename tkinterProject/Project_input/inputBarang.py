from tkinter import Tk, ttk, StringVar
from json import load, dump
#Tk untuk window, ttk object turunan tkinter

fileData = "data.json"
data = {}

def saveData():
	global data

	with open (fileData,"w") as f:
		dump(data,f)

def loadData():
	global data

	with open(fileData) as f:
		data = load(f)

loadData()

myApps = Tk()
myApps.title("My Apps")
#myApps.resizable(False, False) #vertikal atau horizontal

counterButton1 = 0

label1 = ttk.Label(myApps, text = "Nama Barang")
label1.grid(column = 0, row = 0)

label2 = ttk.Label(myApps, text = "Harga")
label2.grid(column = 1, row = 0)

label3 = ttk.Label(myApps, text = "Jumlah")
label3.grid(column = 2, row = 0)

label4 = ttk.Label(myApps, text = "ID")
label4.grid(column = 3, row = 0)

label5 = ttk.Label(myApps, text = "Exp.Date")
label5.grid(column = 4, row = 0)

def action_button1():
	global counterButton1, students_data
	button1.configure(text = "Already Clicked")
	if counterButton1 % 2 == 0 :
		label1.configure(foreground = "blue")
		label2.configure(foreground = "blue")
		label3.configure(foreground = "blue")
		label4.configure(foreground = "blue")
		label5.configure(foreground = "blue")
	else:
		label1.configure(foreground = "red")
		label2.configure(foreground = "red")
		label3.configure(foreground = "red")
		label4.configure(foreground = "red")
		label5.configure(foreground = "red")

	label1.configure(text = data_name.get())
	label2.configure(text = data_harga.get())
	label3.configure(text = data_jumlah.get())
	label4.configure(text = data_ID.get())
	label5.configure(text = data_expdate.get())
	counterButton1 += 1
	data[data_name.get()] = data_harga.get() , data_jumlah.get() , data_ID.get() , data_expdate.get()
	saveData()
	print(data)

#button
button1 = ttk.Button(myApps, text = "Click here", command = action_button1)
button1.grid(column = 5, row = 1)

#entry
data_name = StringVar()
data_name_entry1= ttk.Entry(myApps, width = 12, textvariable = data_name)
data_name_entry1.grid(column = 0, row = 1)

data_harga = StringVar()
data_name_entry2= ttk.Entry(myApps, width = 12, textvariable = data_harga)
data_name_entry2.grid(column = 1, row = 1)

data_jumlah = StringVar()
data_name_entry3= ttk.Entry(myApps, width = 12, textvariable = data_jumlah)
data_name_entry3.grid(column = 2, row = 1)

data_ID = StringVar()
data_name_entry4= ttk.Entry(myApps, width = 12, textvariable = data_ID)
data_name_entry4.grid(column = 3, row = 1)

data_expdate = StringVar()
data_name_entry5= ttk.Entry(myApps, width = 12, textvariable = data_expdate)
data_name_entry5.grid(column = 4, row = 1)




#data_name = input("Name : ")
#focus
data_name_entry1.focus()
data_name_entry2.focus()
data_name_entry3.focus()
data_name_entry4.focus()
data_name_entry5.focus()

#combobox dropdown list
#data_age_combobox = ttk.Combobox(myApps, width = 12, textvariable = data_age)
'''
data_age_combobox = ttk.Combobox(myApps, width = 12, textvariable = data_age, state = "readonly") # state = "readonly"
data_age_combobox["values"] = ["YOUNGER",12,13,14,15,"OLDER"]
data_age_combobox.grid(column = 1, row = 1)
data_age_combobox.current(0)
'''
data_age_combobox = ttk.Combobox(myApps, width = 12, textvariable = data_jumlah, state = "readonly")
data_age_combobox["values"] = [1,2,3,4,5," > 5"]
data_age_combobox.grid(column = 2, row = 1)
data_age_combobox.current(0)
if __name__ == "__main__":
	myApps.mainloop()