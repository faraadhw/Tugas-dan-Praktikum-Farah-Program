#Farah Diyanah Adhwa
#231031046
#SI23-B



import random

angka = [1,2,3,4,5]

angka_benar = random.choice(angka)

a = True
limit = 3
i = 0

while a:
	i += 1
	pilihan = int(input("Masukan angka acak(1-5) : "))

	if pilihan == angka_benar:
		print("Tebakan anda Benar!!")
		print("angka benar = ",angka_benar)
		a = False
	elif pilihan > len(angka):
		print("Angka harus 1-5 tidak boleh kurang dan lebih!!")
	else:
		if i == limit:
			print("Anda gagal:(")
			a = False
		else:
			print(f"Salah, anda memiliki {limit-i} kesempatan lagi")
