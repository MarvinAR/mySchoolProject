from tkinter import Tk, ttk, StringVar
#Tk untuk window, ttk object turunan tkinter

students_data = {}

myApps = Tk()
myApps.title("My Apps")
#myApps.resizable(False, False) #vertikal atau horizontal

counterButton1 = 0

label1 = ttk.Label(myApps, text = "Enter a name")
label1.grid(column = 0, row = 0)

label2 = ttk.Label(myApps, text = "My Age")
label2.grid(column = 1, row = 0)

def action_button1():
	global counterButton1, students_data
	button1.configure(text = "Already Clicked")
	if counterButton1 % 2 == 0 :
		label1.configure(foreground = "blue")
		label2.configure(foreground = "blue")
	else:
		label1.configure(foreground = "red")
		label2.configure(foreground = "red")
	label1.configure(text = data_name.get())
	label2.configure(text = data_age.get())
	counterButton1 += 1
	students_data[data_name.get()] = data_age.get()
	print(students_data)

#button
button1 = ttk.Button(myApps, text = "Click here", command = action_button1)
button1.grid(column = 2, row = 1)

#entry
data_name = StringVar()
data_name_entry= ttk.Entry(myApps, width = 12, textvariable = data_name)
data_name_entry.grid(column = 0, row = 1)

#data_name = input("Name : ")
#focus
data_name_entry.focus()

#combobox dropdown list
data_age = StringVar()
#data_age_combobox = ttk.Combobox(myApps, width = 12, textvariable = data_age)
data_age_combobox = ttk.Combobox(myApps, width = 12, textvariable = data_age, state = "readonly") # state = "readonly"
data_age_combobox["values"] = ["YOUNGER",12,13,14,15,"OLDER"]
data_age_combobox.grid(column = 1, row = 1)
data_age_combobox.current(0)


if __name__ == "__main__":
	myApps.mainloop()