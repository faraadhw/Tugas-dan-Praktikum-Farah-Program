nim = [2,3,1,0,3,1,0,4,6]
nim1 = ['2','3','0','0','3','1','0','4','6']
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
print(f'item indeks 1,2:{nim[1:3]}')
print(f'item indeks []:{nim[3:3]}')
print(f'item indeks 2,3,4:{nim[2:5]}')
print(f'item indeks [1:8]:{nim[1:-1]}')
print(f'item indeks [2:7]:{nim[2:-2]}')

#Nested List
kelas = [('Pemograman',2),
         ('Kaldas',3)]
print(kelas)
kelas.append(('Cinta',2))
print(kelas)
kelas.append(('Bahasa',2))
kelas.append(('Pancasila',2))
print(kelas)
#tambahkan matkul 4 dan 5 dan sksnya


'''Buatkan kode menggunakan (f'')dari tulisan dibawah ini'''
#Mata kuliah 1: Matkul dengan 2 sks
#Mata kuliah 2: Matkul dengan 3 sks
#Mata kuliah 3: Matkul dengan 2 sks
#Mata kuliah 4: Matkul dengan 2 sks
#Mata kuliah 5: Matkul dengan 2 sks

print()
print(f'Mata kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
print(f'Mata kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
print(f'Mata kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
print(f'Mata kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
print(f'Mata kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')
print()

data = [('Farah Diyanah Adhwa',2023,'Aktif'),
        (96,99,98,97,95),
        (2,3,2,2,2),
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

print()
print(f'Nama mahasiswa: {data[0][0]}')
print(f'Inisial {data[0][0]}: {data[0][0][0]}{data[0][0][6]}{data[0][0][-5]}')
ubah = int(''.join(map(str,nim))) 
print(f'NIM {data[0][0]}: {ubah}')
print(f'Program {data[0][0]}: {data[-1][0]} {data[-1][1]}')
print(f'Angkatan {data[0][0]}: {data[-1][-1]}-{data[0][1]}')
print(f'Total sks {data[0][0]} adalah: {sum(data[2])}')
print(f'Jumlah Nilai {data[0][0]}: {len(data[2])}')
print(f'Nilai tertinggi {data[0][0]}: {max(data[1])}')
print(f'Nilai terendah {data[0][0]}: {min(data[1])}')
print(f'Rata-rata nilai {data[0][0]}: {sum(data[1])/len(data[1])}')


#Nama mahasiswa: Farah Diyanah Adhwa
#Inisial Farah Diyanah Adhwa: FDA
#NIM Frankel: 231031039
#Program Frankel: S1-Reguler Sistem Informasi B
#Angkatan Frankel: Ganjil-2023
#Total sks Frankel adalah: 11
#Jumlah Nilai Frankel: 5
#Nilai tertinggi Frankel: 99
#Nilai terendah Frankel: 76
#Rata-rata nilai Frankel: 92.25
