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

	system('cls')
	print("Aplikasi Daftar Belanjaan\n")

	counter = 1

	Username = input('Masukkan Username : ')
	Password = getpass('Masukkan Password : ')

	dataCheck = False
	passLogin = False  

	if Username in user:
		dataCheck = True
		passLogin = (user[Username][0] == Password)
	
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
			passLogin = (user[Username][0] == Password)

		else:
			dataCheck = False
			passLogin = False 
		
	else:
		level = user[Username][1]
		print('Login Pass !')
		return True, level



def print_menu():

	print('Selamat datang User\n')
	print("1. Tambahkan barang belanjaan")
	print("2. Lihat barang belanjaan")
	print("3. Hapus barang belanjaan")
	print("4. Info aplikasi")
	print("Q. Keluar\n")

def menu_admin():
	
	print("Selamat Datang Admin\n")
	print("1. Melihat User dan password")
	print("2. Menghitung diskon")
	print("3. Lihat total daftar belanjaan")
	print("4. Lihat tanggal daftar belanjaan")
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

	counter = 0
	
	while counter != 1:
		pilihan = input(f"\nApakah anda yakin ingin menambahkan barang di atas pada tanggal {hari} - {bulan} - {tahun} (Y/N) : ")
		
		if pilihan.upper() == 'Y':
			saveData()
			sleep(1)
			print('Data Saved.')
			counter += 1
		
		elif pilihan.upper() == 'N':
			sleep(1)
			print("Penambahan barang dibatalkan")
			counter += 1
		
		else:
			print("Masukkan pilihan dengan benar")
			sleep(1.5)
			system('cls')

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
			print("| No | Nama Barang\t| Harga\t\t| Jumlah\t| Ex.Date\t| ID \t\t| Diskon \t\t\t\t|")
			
			for info in data[date]:

				barang = info
				harga =  data[date][info]["harga"]
				jumlah = data[date][info]["kuantitas"]
				ID = data[date][info]["ID"]
				ex_date = data[date][info]["ex_date"]

				if ex_date > 12:
					bulan_ex = int(bulan) - 12
					tahun_ex = tahun + 1
					print("====================================================================================================================================")
					print(f"| {no}  | {barang}\t\t| Rp {harga},-\t| {jumlah}\t\t| {hari} - {bulan_ex} - {tahun_ex}\t\t| {ID}\t| Hanya dapat ditampilkan di mode admin\t|")
					no += 1
					saveData()
				
				else:
					bulan_ex = int(bulan) + 2
					print("=================================================================================================================================")
					print(f"| {no}  | {barang}\t\t| Rp {harga},-\t| {jumlah}\t\t| {hari} - {bulan_ex} - {tahun}\t| {ID}\t| Hanya dapat ditampilkan di mode admin\t|")
					no += 1
					saveData()
			
			print("=================================================================================================================================")
		
		else:
			print(f"Anda belum mendaftarkan barang belanjaan anda di tanggal {hari} - {bulan} - {tahun}")
			
	else:
		print("Anda belum mendaftarkan barang belanjaan anda di aplikasi ini")

def remove():

	system("cls")
	hari =  input("Masukkan tanggal : ")
	bulan = input("Masukkan bulan   : ")
	tahun = input("Masukkan tahun   : ")
	date = str(tahun) + str(bulan) + str(hari)
	
	if date in data:
		counter = 0
		pilihan = ""
		
		while counter != 1:

			pilihan = input(f"\nApakah anda yakin ingin menghapus barang di tanggal {hari} - {bulan} - {tahun} (Y/N) : ")
			
			if pilihan.upper() == 'Y':
				del data[date]
				saveData()
				sleep(1)
				print("Data Removed")
				counter += 1
			
			elif pilihan.upper() == 'N':
				sleep(1)
				print("Penghapusan barang dibatalkan")
				counter += 1
			
			else:
				print("Masukkan pilihan dengan benar ")
				sleep(1.5)
				system('cls')
	
	else:
		print(f"Anda belum mendaftarkan barang belanjaan anda di tanggal {hari} - {bulan} - {tahun}")

def about():

	system("cls")
	print("Aplikasi Penyimpan Data Barang belanjaan\n")
	print("Tugas Project membuat aplikasi ")
	print("Dibuat oleh Marvin AR dengan bimbingan dari Sir Anas")
	print("Dibuat dari tanggal 23 Juni 2020")
	print("Dalam membuat aplikasi ini, saya menggunakan aplikasi Sublime Text 3")

def total():
	
	system("cls")
	
	if len(data) > 0:
		hari =  input("Masukkan tanggal : ")
		bulan = input("Masukkan bulan   : ")
		tahun = input("Masukkan tahun   : ")
		date = str(tahun) + str(bulan) + str(hari)
		system('cls')
		
		if date in data:

			print(f"Total harga barang barang di tanggal {hari} - {bulan} - {tahun} : \n")
			
			grand_total_barang = 0

			for info in data[date]:

				barang = info
				harga =  data[date][info]["harga"]
				jumlah = data[date][info]["kuantitas"]
				A = int(harga) * int(jumlah)
				grand_total_barang += A
				print(f"{barang} : Rp {harga},- ( {jumlah} buah ) : Rp {A},-")

			print(f"\nTotal keseluruhan belanja pada tanggal {hari} - {bulan} - {tahun} : Rp {grand_total_barang},-")

def lihat_user():

	system('cls')
	print("Nama - nama user beserta passwordnya : \n")
	print("| No | Nama User \t| Password \t|")

	no = 1
	
	for info in user:
		nama_user = info
		password  = user[info][0]
		print("=========================================")
		print(f"| {no}  | {nama_user}\t\t| {password}\t\t| ")
		no += 1
	
	print("=========================================")

def diskon():

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
			print("| No | Nama Barang\t| Harga\t\t| Jumlah\t|")
			
			for info in data[date]:

				barang = info
				harga =  data[date][info]["harga"]
				jumlah = data[date][info]["kuantitas"]
				
				print("=========================================================")
				print(f"| {no}  | {barang}\t\t| Rp {harga},-\t| {jumlah}\t\t|")
				no += 1
					
			print("=========================================================")

			counter = 0
			while counter != 1:
				diskon = int(input("Masukkan jumlah diskon yang ingin dimasukkan ( ... % ) : "))
				system('cls')

				if diskon < 100:
					counter +=1
					print(f"Daftar belanja tanggal  {hari} - {bulan} - {tahun} setelah di diskon {diskon}% : \n")
					print("| No | Nama Barang\t| Harga\t\t\t\t\t| Jumlah\t|")
					
					for info in data[date]:
						barang = info
						harga =  data[date][info]["harga"]
						jumlah = data[date][info]["kuantitas"]
						diskon_dikurangi = 100 - diskon
						harga_diskon = int(harga) * int(diskon_dikurangi) / 100
						harga_diskon = int(harga_diskon)
						no = 1
						print("=================================================================================")
						print(f"| {no}  | {barang}\t\t| Rp {harga_diskon},- ( Di diskon {diskon}% )\t\t| {jumlah}\t\t|")
						no += 1
				
					print("=================================================================================")
				
				elif diskon > 100 or diskon < 0:
					print("Mohon Masukkan angka dibawah 100 dan diatas 0")
				
				else:
					print("Mohon masukkan diskon dalam bentuk angka")

		else:
			print(f"Anda belum mendaftarkan barang belanjaan anda di tanggal {hari} - {bulan} - {tahun}")
			
	else:
		print("Anda belum mendaftarkan barang belanjaan anda di aplikasi ini")

def lihat_tanggal():

	system('cls')

	no = 1

	if len(data) > 0:

		print("Daftar Tanggal Yang Terdapat Daftar Belanjaan\n")
		print("| No | Tanggal \t|")

		for info in data:

			print("=================")
			tanggal = info
			print(f"| {no}  | {info} \t|")
			no += 1

		print("=================")