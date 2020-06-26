from json import load, dump
from time import sleep
from getpass import getpass
from datetime import datetime
from os import system
import random
import string

fileData = 'data.json'
fileUser = 'user.json'

data = {}
user = {}

def loadData():

	global data, user
	with open(fileData) as f:
		data = load(f)
	with open(fileUser) as f:
		user = load(f)

	return True

def saveData():
	global data, user
	with open (fileData,"w") as f:
		dump(data,f)
	with open (fileUser,"w") as f:
		dump(user,f)

	return True

def login():
	print("Aplikasi Daftar Belanjaan\n")
	counter = 1
	Username = input('Masukkan Username : ')
	Password = getpass('Masukkan Password : ')
	dataCheck = False
	passLogin = False  
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)
	else:
		dataCheck = False
		passLogin = False

	while not dataCheck or not passLogin:
		counter += 1
		if counter > 3:
			return False
		print('\nKombinasi Username dan Password salah\n')
		Username = input('Masukkan Username : ')
		Password = getpass('Masukkan Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
		else:
			dataCheck = False
			passLogin = False 
		
	else:
		print('Login Pass !')
		return True

def print_menu():

	print('Selamat datang \n')
	print("1. Tambahkan barang belanjaan")
	print("2. Lihat barang belanjaan")
	print("3. Hapus barang belanjaan")
	print("4. Info aplikasi")
	'''
	print("5. Lihat berdasarkan ID")
	print("6. Lihat berdasarkan Nama")
	'''	
	print("Q. Keluar\n")

def tambah():


	system("cls")
	data_sementara = {}
	hari  = datetime.now().day
	bulan = datetime.now().month
	tahun = datetime.now().year
	date  = str(tahun) + str(bulan) + str(hari)
	jumlah_barang = input(f"Masukkan jumlah barang yang ingin dimasukkan pada tanggal {hari} - {bulan} - {tahun} : ")
	for barang in range(int(jumlah_barang)):
		nama_barang = input('\nMasukkan nama barang belanjaan   : ')
		harga = input('Masukkan harga barang belanjaan  : ')
		kuantitas = input('Masukkan jumlah barang belanjaan : ')

		alphabet = string.ascii_uppercase
		alpha_numeric = string.digits
		A = random.choice(alphabet)
		B = random.choice(alpha_numeric)
		C = random.choice(alphabet)
		D = random.choice(alpha_numeric)
		E = random.choice(alphabet)
		F = random.choice(alpha_numeric)

		ID = f"{A}{B}{C}{D}{E}{F}"
		ex_date = int(bulan) + 2

		data_sementara[nama_barang] = {
			"harga" : harga,
			"kuantitas" : kuantitas,
			"ID" : ID,
			"ex_date" : ex_date
		}
	data[date] = data_sementara
	
	saveData()
	sleep(1)
	print('Data Saved.')

def lihat():

	system("cls")
	if len(data) > 0:

		hari =  input("Masukkan tanggal : ")
		bulan = input("Masukkan bulan   : ")
		tahun = input("Masukkan tahun   : ")
		date = str(tahun) + str(bulan) + str(hari)

		
		if date in data:
			#Template header
			system("cls")
			no = 1
			print(f"Daftar belanja tanggal {hari} - {bulan} - {tahun} : \n")
			print("| No | Nama Barang\t| Harga\t\t| Jumlah\t| Ex.Date\t| ID Barang\t|")
			for info in data[date]:
				barang = info
				harga =  data[date][info]["harga"]
				jumlah = data[date][info]["kuantitas"]
				ID = data[date][info]["ID"]
				ex_date = data[date][info]["ex_date"]



				if ex_date > 12:
					bulan_ex = int(bulan) - 12
					tahun_ex = tahun + 1
					print("=========================================================================================")
					print(f"| {no} | {barang}\t\t| {harga}\t\t| {jumlah}\t\t| {hari} - {bulan_ex} - {tahun_ex}\t| {ID}\t|")
					no += 1
					saveData()
				else:
					bulan_ex = int(bulan) + 2
					print("=========================================================================================")
					print(f"| {no} | {barang}\t\t| {harga}\t\t| {jumlah}\t\t| {hari} - {bulan_ex} - {tahun}\t| {ID}\t|")
					no += 1
					saveData()
			print("=========================================================================================")

		input("ENTER untuk kembali ke menu utama ")
			
	else:
		print("Anda belum mendaftarkan barang belanjaan anda di aplikasi ini")

def remove():

	system("cls")
	hari =  input("Masukkan tanggal : ")
	bulan = input("Masukkan bulan   : ")
	tahun = input("Masukkan tahun   : ")
	date = str(tahun) + str(bulan) + str(hari)

	if date in data:
		del data[date]
		saveData()
		sleep(1)
		print("Data Removed")
	else:
		print(f"Anda belum mendaftarkan barang belanjaan anda di tanggal {hari} - {bulan} - {tahun}")

def about():

	system("cls")
	print("Aplikasi Penyimpan Data Barang belanjaan\n")
	print("Tugas Project membuat aplikasi ")
	print("Dibuat oleh Marvin AR dengan bimbingan dari Sir Anas")
	print("Dibuat dari tanggal 23 Juni 2020")
	print("Dalam membuat aplikasi ini, saya menggunakan aplikasi Sublime Text")
'''
def lihat_berdasar_ID():

	system("cls")
	if len(data) > 0:

		ID =  input("Masukkan ID barang : ")

		if ID in data:
			for info in data[ID]:
				break
				
		else:
			print(f"Tidak ada barang yang memiliki ID {ID}")

	else:
		print(f"Anda belum mendaftarkan barang belanjaan anda di aplikasi ini")

def lihat_berdasar_nama():

	system("cls")
	if len(data) > 0:

		nama = input("Masukkan nama barang : ")

		if nama in data:
			for info in data[nama]:
				break

		else:
			print(f"Tidak ada barang yang memiliki nama {nama}")
	else:
		print(f"Anda belum mendaftarkan barang belanjaan anda di aplikasi ini")
'''



