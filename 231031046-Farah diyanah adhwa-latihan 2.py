print ('Nama: Farah Diyanah Adhwa')
print ('Nim: 231031046')
print ()

inp = input('Masukan suatu input: ')

if len(inp) != 3:
    print('Panjang string', len(inp),'tidak sama dengan 3')

else:
    print('Panjang input sesuai yang diinginkan')

print()
nilai = int(input('Masukan nilai: '))

if nilai >= 90:
    print('Nilai huruf: A')
elif nilai > 75:
    print('Nilai huruf: B')
elif nilai > 55:
    print('Nilai huruf: C')
else:
    print('Nilai huruf: D')
