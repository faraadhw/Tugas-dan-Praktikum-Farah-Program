print('Nama Lengkap: Farah Diyanah Adhwa')
print('Nim         : 231031046')
print('Prodi       : Sistem Informasi')
print()
print(f'2. Program Selisih Waktu')
print()

jam1 = int(input("masukan jam : "))
menit1 = int(input("masukan menit : "))
print(f"waktu yang di input = {jam1}:{menit1}")

print("\nMENGHITUNG SELISIH DARI\n")

jam2 = int(input("masukan jam : "))
menit2 = int(input("masukan menit : "))
print(f"jumlah waktu yang mau diselisihkan = {jam2}:{menit2}")

hasil_jam = (jam1 - jam2)
hasil_menit = (menit1 - menit2)

if hasil_menit <= 0:
    hasil_jam -= 1
    hasil_menit += 60

print(f"\nhasilnya adalah = {hasil_jam}:{hasil_menit}")
print("="*20)
