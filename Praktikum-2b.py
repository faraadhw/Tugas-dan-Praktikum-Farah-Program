print('praktikum-b2')
print('Nama Lengkap: Farah diyanah adhwa')
print('NIM         : 231031046')
print('Prodi       : Sistem informasi')

print()
a = 15
print('Nilai a adalah=',a)
a = a + 2
print('Nilai a menjadi=',a)

print()
a = 15
print('Nilai a adalah=',a)
a += 2
print('Nilai a += menjadi=',a)

print()
a = 15
print('Nilai a adalah=',a)
a -= 2
print('Nilai a -= menjadi=',a)

print()
a = 15
print('Nilai a adalah=',a)
a *= 2 #ini operasi a = a * 2
print('Nilai a *= menjadi=',a)

print()
a = 15
print('Nilai a adalah=',a)
a /= 2 #ini operasi a = a / 2
print('Nilai a /= menjadi=',a)

print()
a = 5
print('Nilai a adalah=',a)
a **= 2 #ini operasi a = a ** 2
print('Nilai a **= menjadi=',a)

print()
a = 35
print('Nilai a adalah=',a)
a %= 31 #ini operasi a = a % 31
print('Nilai a %= menjadi=',a)

print()
a = 35
print('Nilai a adalah=',a)
a //= 31 #ini operasi a = a // 31
print('Nilai a //= menjadi=',a)

##########
print()
bi = True
print('Nilai bi menjadi=',bi)
bi = bi | False
print('Nilai bi menjadi=',bi)

print()
bi = False
print('Nilai bi menjadi=',bi)
bi = bi | False
print('Nilai bi menjadi=',bi)

print()
bi = False
print('Nilai bi menjadi=',bi)
bi = bi | True
print('Nilai bi menjadi=',bi)

print()
bi = False
print('Nilai bi menjadi=',bi)
bi &= True
print('Nilai bi menjadi&=',bi)

print()
bi = False
print('Nilai bi menjadi=',bi)
bi ^=  True
print('Nilai bi menjadi^=',bi)

print()
bi = True
print('Nilai bi menjadi=',bi)
bi ^= True
print('Nilai bi menjadi^=',bi)

# ###############
print()
a = 7
hasil = a == 5
print('Apakah a=5 ?', hasil)
hasil = a>9
print('Apakah a>9 ?', hasil)
hasil = a == 5
print('Apakah a=5 ?', hasil)
hasil = a<9
print('Apakah a<9 ?', hasil)
hasil = a != 7
print('Apakah a!=7 ?', hasil)
hasil = a>7
print('Apakah a>7 ?', hasil)
hasil = a<7
print('Apakah a<7 ?', hasil)

##########
a = True
b = False

hasil = a and a
print(a,'and',a,'adalah =',hasil)
hasil = a and b
print(a,'and',b,'adalah =',hasil)
hasil = b and a
print(b,'and',a,'adalah =',hasil)
hasil = a and b
print(b,'and',b,'adalah =',hasil)

print()
hasil = a or a
print(a,'or',a,'adalah =',hasil)
hasil = a or b
print(a,'or',b,'adalah =',hasil)
hasil = b or a
print(b,'or',a,'adalah =',hasil)
hasil = b or b
print(b,'or',b,'adalah =',hasil)

print()
hasil = not a
print('not',a,'adalah=',hasil )
hasil = not b
print('not',b,'adalah=',hasil )
