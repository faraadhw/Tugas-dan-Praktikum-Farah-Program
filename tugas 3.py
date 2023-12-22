print ('tugas 3')
print ('NAMA  : Farah diyanah Adhwa')
print ('KELAS : SI23-B')
print ('NIM   : 231031046')

print ('\n')
#Tugas lanjutkan kode
#Dengan cara yang sama buat operator in
print ('============ NOT IN ============')
nama = 'Farah Diyanah Adhwa'

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek  = not(test1 in nama)
print(test1,'tidak ada di', nama, 'adalah =', cek)

cek  = not(test2 in nama)
print(test2,'tidak ada di', nama, 'adalah =', cek)

cek  = not(test3 in nama)
print(test3,'tidak ada di', nama, 'adalah =', cek)

cek  = not(test4 in nama)
print(test4,'tidak ada di', nama, 'adalah =', cek)

cek  = not(test5 in nama)
print(test5,'tidak ada di', nama, 'adalah =', cek)


print ('\n')
a = 1 #Tanggal lahir
b = 9 #Bulan lahir
a += 60
b += 80

#Tugas untuk or
print ('============OR============')
print('NIlai', a, 'biner adalah      =', format(a,'09b'))
print('NIlai', b, 'biner adalah      =', format(b,'09b'))
print('-----------------------------------------OR')
c = a | b
print('Nilai', a, '||', b, 'biner adalah =', format(c, '09b'))

print('\n')
#Tugas untuk xor
print ('============XOR============')
print('NIlai', a, 'biner adalah      =', format(a,'09b'))
print('NIlai', b, 'biner adalah      =', format(b,'09b'))
print('--------------------------------------------XOR')
c = a ^ b
print('Nilai', a, 'xor', b, 'biner adalah =', format(c, '09b'))


print ('\n')
#Tugas Lanjutan untuk not b
print('\n=========NOT===========')
c = ~b
print('Nilai', b, 'biner adalah     =', format(b, '09b'))
print('Nilai not',b, 'biner adalah =', format(c, '09b'))



print('\n')
#Tugas buat untuk NAD
print('=======NOT AND===========')
print('NIlai', a, 'biner adalah           =', format(a,'09b'))
print('NIlai', b, 'biner adalah           =', format(b,'09b'))
print('-----------------------------------------NOT AND')
c = ~(a & b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))


print('\n')
#Tugas buat untuk NOR
print('=========NOT OR=============')
print('NIlai', a, 'biner adalah            =', format(a,'09b'))
print('NIlai', b, 'biner adalah            =', format(b,'09b'))
print('-----------------------------------------NOT OR')
c = ~(a | b)
print('Nilai', a, 'not and', b, 'biner adalah =', format(c, '09b'))


print('\n')
#Tugas buat untuk NXOR
print('=========NOT XOR=============')
print('NIlai', a, 'biner adalah            =', format(a,'09b'))
print('NIlai', b, 'biner adalah            =', format(b,'09b'))
print('-----------------------------------------NOT XOR')
c = ~(a ^ b)
print('Nilai', a, 'not xor', b, 'biner adalah =', format(c, '09b'))

print('\n')
print('=========NOT << 2=============')
#Tugas buat untuk c = ~(a<<2)
c = ~(a << 2)
print('Nilai', a, 'biner adalah          =', format(a, '09b'))
print('Nilai',a, 'not << 2 biner adalah =', format(c, '09b'))

# Tugas buat untuk c = ~(b<<2)
c = ~(b << 2)
print('Nilai', b, 'biner adalah         =', format(b, '09b'))
print('Nilai',b, 'not << 2 biner adalah =', format(c, '09b'))

print('\n')
print('=========NOT >> 2=============')
# Tugas buat untuk c = ~(a>>2)
c = ~(a >> 2)
print('Nilai', a, 'biner adalah         =', format(a, '09b'))
print('Nilai',a, 'not >> 2 biner adalah =', format(c, '09b'))

# Tugas buat untuk c = ~(b>>2)
c = ~(b >> 2)
print('Nilai', b, 'biner adalah         =', format(b, '09b'))
print('Nilai',b, 'not >> 2 biner adalah =', format(c, '09b'))

