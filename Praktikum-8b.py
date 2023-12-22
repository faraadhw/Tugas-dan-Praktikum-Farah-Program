pwd_benar = 'si23B'
a = True
i = 0
Limit = 3
while a:
    i += 1
    pwd = input ('Masukkan password: ')
    if pwd == pwd_benar:
        print('Selamat anda login!')
        a = False
    else:
        if i == Limit:
            a = False
            print('Anda kehabisan kesempatan!')
        else:
            print('Password salah, Coba lagi!')


print()
pwd_benar = 'si23'
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah')
        if i == limit:
            a = False
            print('Anda Kehabisan Kesempatan')
        else:
            print(f'Kesempatan Anda Tersisa {limit-i} Kali')
