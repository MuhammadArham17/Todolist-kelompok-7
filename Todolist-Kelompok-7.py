import os , sys , time

file_path = "your path.txt" #memasukan tugas.txt ke dalam file path

def tambah():
	tugas_baru = input(" Masukan Tugas Baru: ")
	with open(file_path,"a") as file: 
		file.write(tugas_baru + "\n")
		os.system("cls")
		print("-"*52)
		print("|".ljust(15)+"Tugas Baru Ditambahkan.".center(15)+"|".rjust(15))
		print("-"*52)
	time.sleep(2)
	lihat()
		
def lihat():
	try:		
		with open(file_path,"r") as file: 
			todo = file.readlines() 
			if not todo: 	
				os.system("cls")		
				print("-"*45)
				print("|".ljust(15)+"Tugas Kosong..".center(15)+"|".rjust(15))
				print("-"*45)
			else:
				os.system("cls")
				print("-"*45)
				print("|".ljust(15)+"Tugas".center(15)+"|".rjust(15))
				print("-"*45)
				for i,tugas in enumerate(todo, start=1): 
					print("|",i,"| "+(tugas.strip()).ljust(15))
				print("-"*45)
	except FileNotFoundError: 
		print("File tidak Ditemukan. Tambahkan Tugas terlebih dahulu .. yaa")

def edit():
	try: 	
		with open(file_path,"r") as file:	
			todo = file.readlines()		
		if not todo:
			os.system("cls")
			print("-"*54)
			print("|".ljust(13)+"Tidak ada tugas untuk diedit".center(3)+"|".rjust(13)) 
			print("-"*54)
			return
		else:
			os.system("cls")
			print("-"*45)
			print("|".ljust(15)+"Tugas".center(15)+"|".rjust(15))
			print("-"*45)
			for i,tugas in enumerate(todo, start=1): 
				print("|",i,"| "+(tugas.strip()).ljust(15))
			print("-"*45)

		nomor_tugas = int(input("Masukan nomor tugas yang ingin di edit : ")) 
		if 1 <= nomor_tugas <= len(todo):
			tugas_baru = input("Masukan Tugas Baru : ") 
			todo[nomor_tugas -1] = tugas_baru + "\n" 	
			with open(file_path,"w") as file:
				file.writelines(todo)
			os.system("cls")
			print("-"*56) 		
			print(f" Tugas ({tugas.strip()}) Berhasil di edit menjadi ({tugas_baru}).")
			print("-"*56)
			print("\tMohon Tunggu sebentar ya kakak....")
			time.sleep(5)
			lihat()
		else:
			os.system("cls")
			print("-"*53)
			print("|".ljust(15)+"Nomor tugas tidak valid.".center(15)+"|".rjust(15)) 
			print("-"*53)
	except ValueError:
		print("Masukan nomor tugas yang benar dong kaks")

def hapus():
	try:
		with open(file_path,"r") as file:
			todo = file.readlines() 
		if not todo:
			os.system("cls")
			print("-"*54)
			print("|".ljust(13)+"Tidak ada tugas untuk diedit".center(3)+"|".rjust(13)) 
			print("-"*54)
			return
		else:
			os.system("cls")
			print("-"*45)
			print("|".ljust(15)+"Tugas".center(15)+"|".rjust(15))
			print("-"*45)
			for i,tugas in enumerate(todo, start=1): 
				print("|",i,"| "+(tugas.strip()).ljust(15))
			print("-"*45)

		hapus_tugas = int(input("Masukan Nomor Tugas Yang Ingin Dihapus: "))
		if 1 <= hapus_tugas <= len(todo): 
			tugas_yg_dihapus = todo.pop(hapus_tugas - 1)
			with open(file_path,"w") as file:
				file.writelines(todo)
			os.system("cls")
			print("-"*53)
			print(f" Tugas ({tugas_yg_dihapus.strip()}) Berhasil di hapus")
			print("-"*53)
		else:
			print("nomor tugas tidak valid..".title)
	except ValueError:
		print("Masukan nomor tugas yang benar dong kakak")

def hapusLangsung():
	try:
		os.system("cls")
		pilih = input("Yakin mau hapus semua ? (y/n)")
		if pilih == "y":
			os.remove(file_path)
			os.system("cls")
			print("-"*50)
			print("|".ljust(15)+"Tugas Sudah di hapus".center(15)+"|".rjust(15))
			print("-"*50)
		elif pilih == "n":
			os.system("cls")
			print("-"*50)
			print("|".ljust(15)+"Tugas Tidak di hapus".center(15)+"|".rjust(15))
			print("-"*50)
	except FileExistsError as f:
		print(f)

def main():
	os.system("cls")
	while True:
		print("-"*45)
		print("|".ljust(0)+"Selamat Datang Di Program To-Do-List".center(43)+"|".rjust(-1))
		print("-"*45)
		print("|1.|".ljust(6)+"Tambah Tugas"+"|".rjust(27))
		print("|2.|".ljust(6)+"Lihat Tugas"+"|".rjust(28))
		print("|3.|".ljust(6)+"Edit Tugas"+"|".rjust(29))
		print("|4.|".ljust(6)+"Hapus Tugas"+"|".rjust(28))
		print("|5.|".ljust(6)+"Hapus Semua Tugas"+"|".rjust(22))
		print("|6.|".ljust(6)+"Exit"+"|".rjust(35))
		print("-"*45)
		print()
		pilihan = int(input("Pilihan Menu (1/2/3/4/5/6) : ")) #input untuk aksi selanjutnya

		if pilihan == 1:
			os.system("cls")
			tambah()
		elif pilihan == 2:
			lihat()
		elif pilihan == 3:
			edit()
		elif pilihan == 4:
			hapus()
		elif pilihan == 5:
			hapusLangsung()
		elif pilihan == 6:
			terima_kasih = "Terima Kasih ya kakak"
			os.system("cls")
			print("-"*51)
			print("|".ljust(15)+terima_kasih+"|".rjust(15))
			print("-"*51)
			sys.exit()
		else:
			print("masukan angka yg benar")

		kembali = input("Kembali ke menu utama (y/n) : ").lower()
		os.system("cls")
		if kembali == "y":
			continue
		elif kembali == "n":
			os.system("cls")
			print("-"*51)
			print("|".ljust(15)+"Terima Kasih Ya kakak"+"|".rjust(15))
			print("-"*51)
			break
		else:
			os.system("cls")
			print("INPUT ERROR masukan pilihan y atau n...")
			time.sleep(0.5)
			for i in range(5):
				time.sleep(1)
				os.system("cls")
				print(f"silahkan tunggu 5 detik... {i+1}")
			os.system("cls")
			continue
			
if __name__ == '__main__': 				 
	if not os.path.exists(file_path): 
		with open(file_path, "w"):
			pass
	main()
