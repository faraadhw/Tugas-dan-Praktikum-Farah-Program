print('Nama  : Farah Diyanah Adhwa')
print('Kelas : SI23-B')
print('NIM   : 231031046')
print('Latihan 6')
print()
#Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
        return None
    elif n==0 or n==1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#Program Utama
nilai = int(input("masukan angka : "))
hasil=fibonacci(nilai)
print('Finobacci(%d)= %d' % (nilai,hasil))
