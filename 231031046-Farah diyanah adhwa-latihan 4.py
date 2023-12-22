print ('Nama: Farah Diyanah Adhwa')
print ('Nim: 231031046')

# Membaca input pendapatan dari pengguna
pendapatan = int(input("Pendapatan: "))

# Inisialisasi variabel persentase dan bonus
persentase = 0
bonus = 0

# Menentukan persentase bonus berdasarkan pendapatan
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40
else:
    persentase = 50

# Menghitung bonus dan jumlah total
bonus = (pendapatan * persentase) / 100
total = pendapatan + bonus

# Mencetak output
print(f'Pendapatan: {pendapatan}')
print(f'Persentase: {persentase}%')
print(f'Bonus: {bonus}')
print(f'Jumlah Total: {total}')
