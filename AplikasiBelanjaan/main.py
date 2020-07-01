from json import load, dump
from os import system
import fitur
from time import sleep

statusLoading = fitur.loadData()

system("cls")

if statusLoading :

	role = input("Masukkan role anda ( Admin atau User ) : ")
	if role.lower() == "user":

		passlogin = fitur.login()
		if passlogin :
			print("Welcome")	
			menuchoice = ""

			while menuchoice.lower() != 'q':
				system('cls')
				fitur.print_menu()
				menuchoice = input('Masukkan opsi anda : ').lower()

				if menuchoice == '1':
					fitur.tambah()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice == '2':
					fitur.lihat()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice == '3':
					fitur.remove()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice == '4':
					fitur.about()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice.lower() == 'q':
					system("cls")
					print("Terima kasih telah menggunakan aplikasi ini")
					sleep(2)
					system("cls")
					break
				else :
					print("Masukkan pilihan dengan benar")
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu :)')

	elif role.lower() == "admin":

		passlogin = fitur.loginAdmin()
		if passlogin :
			print("Welcome")	
			menuchoice = ""

			while menuchoice.lower() != 'q':
				system('cls')
				fitur.menu_admin()
				menuchoice = input('Masukkan opsi anda : ').lower()
				if menuchoice == '1':
					fitur.lihat_user()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice == '2':
					fitur.diskon()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				elif menuchoice == '3':
					fitur.total()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
				else :
					print("Masukkan pilihan dengan benar")
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu :)')
				
	else:
		print("\nGagal untuk Log In")
else:
	print("Aplikasi tidak bisa berjalan")

			