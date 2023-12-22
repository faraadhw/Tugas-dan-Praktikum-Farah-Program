# Inisialisasi variabel saldo
saldo = 200000

def bahasa_indo():
    global saldo
    print('\nBahasa Indonesia terpilih.')
    print('PILIH OPSI DI BAWA\n')
    print('1. Cek saldo saya')
    print('2. Ambil uang saya')
    print('3. Tabung uang saya')

    option = int(input('Silakan pilih option: '))

    if option == 1:
        print('Saldo Anda: Rp. ', saldo)
    elif option == 2:
        print('Saldo Anda saat ini: Rp. ', saldo)
        ambil_uang = int(input('Mau ambil berapa? '))
        if ambil_uang <= saldo:
            saldo -= ambil_uang
            print('Saldo Anda sekarang: Rp. ', saldo)
        else:
            print('Saldo tidak mencukupi, mohon coba lagi!')
    elif option == 3:
        print('Saldo Anda: Rp. ', saldo)
        tambah_uang = int(input('Masukkan jumlah uang yang ingin ditabung: '))
        saldo += tambah_uang
        print('Berhasil menabung: Rp. ', tambah_uang)
        print('Saldo Anda sekarang: Rp. ', saldo)
    else:
        print('Pilihan Anda salah, silakan coba lagi!')

    lanjut = input("Lanjut transaksi? (ya / tidak): ")
    if lanjut.lower() == "ya":
        return bahasa_indo()
    elif lanjut.lower() == "tidak":
        print("\nTerima kasih sudah transaksi!")
        rating = input(' Berikan rating (1-5): ')
        print('Terima kasih atas ulasan Anda. Kami menghargai masukan Anda!')

def bahasa_inggris():
    global saldo
    print('\nEnglish selected.')
    print('CHOOSE AN OPTION\n')
    print('1. Check my balance')
    print('2. Withdraw money')
    print('3. Deposit money')

    option = int(input('Please select an option: '))

    if option == 1:
        print('Your balance: Rp. ', saldo)
    elif option == 2:
        print('Your current balance: Rp. ', saldo)
        withdraw_amount = int(input('How much would you like to withdraw? '))
        if withdraw_amount <= saldo:
            saldo -= withdraw_amount
            print('Your new balance: Rp. ', saldo)
        else:
            print('Insufficient balance, please try again!')
    elif option == 3:
        print('Your balance: Rp. ', saldo)
        deposit_amount = int(input('Enter the amount you want to deposit: '))
        saldo += deposit_amount
        print('Successfully deposited: Rp. ', deposit_amount)
        print('Your new balance: Rp. ', saldo)
    else:
        print('Invalid choice, please try again!')

    lanjut = input("Continue trading? (yes / no): ")
    if lanjut.lower() == "yes":
        return bahasa_inggris()
    if lanjut.lower() == "no":
        print("\nThank you for transacting!")
        rating = input(' Give a rating (1-5): ')
        print('Thank you for your feedback. We appreciated that!')

def bahasa_gege():
    global saldo
    print('\nBagahagasagah ingndogonegesigiaga tegerpigiligi.')
    print('SIGILAGAKAGAN PIGILIGIH OGOPSIGI DIGIBAGAWAGAH\n')
    print('1. Cegek sagaldogo sagayaga')
    print('2. Agambigil uguagang sagayaga')
    print('3. Tagabugung uguagang sagayaga')

    option = int(input('Sigilagakagan pigiligih ogopsigi: '))

    if option == 1:
        print('Sagaldogo Agandaga: Rp. ', saldo)
    elif option == 2:
        print('Sagaldogo Agandaga sagaagat iginigi: Rp. ', saldo)
        ambil_uang = int(input('Magaugu agambigil begeragapaga? '))
        if ambil_uang <= saldo:
            saldo -= ambil_uang
            print('Sagaldogo Agandaga segekagaragang: Rp. ', saldo)
        else:
            print('Sagaldogo tigidagak megencugukugupigi, mogohogon cogobaga lagagigi!')
    elif option == 3:
        print('Sagaldogo Agandaga: Rp. ', saldo)
        tambah_uang = int(input('Magasugukkagan jugumlagah uguagang yaganggg ingngigin digitagabugung: '))
        saldo += tambah_uang
        print('Begerhagasigil megenagabugung: Rp. ', tambah_uang)
        print('Sagaldo Agandaga segekagaragang: Rp. ', saldo)
    else:
        print('Pigiligihagan Agandaga sagalagah, sigilagakagan cogobaga lagagigi!')

    lanjut = input("Laganjugut tragansagaksigi? (yaga / tigidagak): ")
    if lanjut.lower() == "yaga":
        return bahasa_indo()
    elif lanjut.lower() == "tigidagak":
        print("\nTegerigimaga kagasigih sugudagah begeragansagaksigi!")
        rating = input(' Begerigikagan ragatiging (1-5): ')
        print('Tegerigimaga kagasigih agatagas ugulagasagan Aganndaga. Kagamigi megenghagargaigi magasugukagan Agandaga!')
   
# Program ATM
print('\nSELAMAT DATANG DI ATM')
print('PILIH BAHASA:')
print('1. Bahasa Indonesia')
print('2. English')
print('3. Bugis ')

language_option = int(input('Silakan pilih bahasa: '))


if language_option == 1:
    bahasa_indo()
elif language_option == 2:
    bahasa_inggris()
elif language_option == 3:
    bahasa_gege()
else:
    print('Pilihan bahasa tidak valid.')
