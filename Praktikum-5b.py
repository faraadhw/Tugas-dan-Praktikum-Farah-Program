nim = [2,3,1,0,3,1,0,4,6]
print(nim)

# akses item
print('item indeks 0:', nim[0])
print('item indeks 3:', nim[3])
print('item indeks terakhir:', nim[len(nim)-1])

#akses indeks negatif
print('item indeks terakhir:', nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6]', nim[-6])
print('item indeks 5: [-4]', nim[-4])
print('item indeks -7: [2]', nim[2])
print('item indeks 3: [-7]', nim[-7])

#akses indeks batas
print(f'item indeks 1,2,.....: {nim[1:]}')
print(f'item indeks 3,4,.....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[-1]}')
print(f'item indeks [:4]: {nim[-5]}')

#pengirisan
print(f'item indeks 1,2: {nim [1:3]}')
print(f'item indeks []: {nim [3:3]}')
print(f'item indeks 2,3,4: {nim [2:5]}')
print(f'item indeks [1:8]: {nim [1:-1]}')
print(f'item indeks [2:7]: {nim [2:-2]}')

#nested list
kelas = [('Pti',3),('Kalkulus',3)]
print(kelas)
kelas.append(('Pancasila',2))
print(kelas)

#Tambahkan matkul 4 dan 5
kelas.append(('Cinta',2))
print(kelas)
kelas.append(('Sainster',2))
print(kelas)

#buatkan kode
#Mata kuliah 1: Matkul dengan 2 sks
#Mata kuliah 2: Matkul dengan 3 sks
#Mata kuliah 3: Matkul dengan 2 sks
#Mata kuliah 4: Matkul dengan .. sks
#Mata kuliah 5: Matkul dengan .. sks

data = [('Farah Diyanah Adhwa',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Farah Diyanah Adhwa
# Inisial Farah: FDA
# NIM Farah: 231031046
# Program Farah: S1-Reguler Sistem Informasi B
# Angkatan Farah: Ganjil-2023
# Total sks Farah adalah: 11
# Jumlah Nilai Farah: 5
# Nilai tertinggi Farah: 99
# Nilai terendah Farah: 76
# Rata-rata nilai Farah: 92.25
