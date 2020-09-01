from json import load, dump
from os import system
import fitur
import buatPDF
from time import sleep

statusLoading = fitur.loadData()

system("cls")

if statusLoading :

	system('cls')
	passlogin = fitur.login()

	if passlogin[0]:

		role = "" 
		print("Welcome")	

		system('cls')
		role = passlogin[1]

		if role.upper() == 'USER':

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

				elif menuchoice == '5':

					buatPDF.buat()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')

				elif menuchoice.lower() == 'q':
				
					system("cls")
					print("Terima kasih telah menggunakan aplikasi ini")
					sleep(2)
					system("cls")
					break

				else :

					print("Masukkan pilihan dengan benar")
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu')

		elif role.lower() == "admin":

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

				elif menuchoice == '4':

					fitur.lihat_tanggal()
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')
					
				elif menuchoice.lower() == 'q':

					system("cls")
					print("Terima kasih telah menggunakan aplikasi ini")
					sleep(2)
					system("cls")
					break
					
				else :
					print("Masukkan pilihan dengan benar")
					input('\nKlik tombol [ ENTER ] untuk kembali ke menu ')

				
	else:
		print("\nGagal untuk melakukan login")

else:
	print("Aplikasi tidak bisa berjalan")

			