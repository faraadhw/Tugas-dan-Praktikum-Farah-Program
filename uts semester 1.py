'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. XYZ Komputer,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama Lengkap,
        mahasiswa@ith.ac.id,
        Nama Kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['B3301','B3302','B3303','B3304','B3305'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,50,3,10],
        [3,3,3,3,3]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. XYZ KOMPUTER
                          JL. BALAIKOTA NO.2 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|-|--   13    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   B3301       | Barang1           |      Rp15000,-|    3   |     Rp45000,-|
2   B3302       | Barang2           |       Rp5000,-|    3   |     Rp15000,-|
3   B3303       | Barang3           |      Rp50000,-|    3   |    Rp150000,-|
4   B3304       | Barang4           |       Rp3000,-|    3   |      Rp9000,-|
5   B3305       | Barang5           |      Rp10000,-|    3   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |   Rp2490000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|-----------------------------------77--------------------------------------|
Summary:
Harga tertinggi adalah    : Rp50000,-  (B3303 - Barang3)
Harga terendah  adalah    : Rp3000,-   (B3304 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Farah Diyanah Adhwa
NIM\t\t: 231031046
Kelas\t\t: Sistem Informasi B''')
print("\n")
#Answer in below
mdata = ["PT. XYZ Komputer",
        "JL. BALAIKOTA NO.1",
        " Kota Parepare",
        "Farah Diyanah Adhwa",
        "farahdiyanahadhwa@ith.ac.id",
        "junghwan",
        "25 Oktober 2023"]

djual = [['B3301','B3302','B3303','B3304','B3305'],
        ['CPU','Kabel','RAM','Flashdisk','Keyboard'],
        [15,5,50,3,10],
        [3,3,3,3,3]]

spasi = 77
r = 1000

header1 = mdata[0].center(spasi)
header2 = (mdata[1]+mdata[2]).center(spasi)
email = mdata[-3].center(spasi)
print(header1,header2,email)

print("\n")

print(f"""MANAJER           : {mdata[3]}
KASIR             : {mdata[-2]}
Tanggal Pembelian : {mdata[-1]}""")
print("-"*spasi)
print("No. "+"|"+"Kode Barang".center(13)+"|"+"Nama Barang".center(19)+"|"+"H. Satuan".center(15)+"|"+"Jumlah".center(8)+"|"+"Total".center(14))
print("-"*spasi)
print("No.1"+"|"+djual[0][0].center(13)+"|"+djual[1][0].center(19)+"|"+f"Rp{djual[2][0]*r},-".rjust(15)+"|"+"3".center(8)+"|"+f"Rp{3*r*djual[2][0]}".center(14))
print("No.2"+"|"+djual[0][1].center(13)+"|"+djual[1][1].center(19)+"|"+f"Rp{djual[2][1]*r},-".rjust(15)+"|"+"3".center(8)+"|"+f"Rp{3*r*djual[2][1]}".center(14))
print("No.3"+"|"+djual[0][2].center(13)+"|"+djual[1][2].center(19)+"|"+f"Rp{djual[2][2]*r},-".rjust(15)+"|"+"3".center(8)+"|"+f"Rp{3*r*djual[2][2]}".center(14))
print("No.4"+"|"+djual[0][3].center(13)+"|"+djual[1][3].center(19)+"|"+f"Rp{djual[2][3]*r},-".rjust(15)+"|"+"3".center(8)+"|"+f"Rp{3*r*djual[2][3]}".center(14))
print("No.5"+"|"+djual[0][4].center(13)+"|"+djual[1][4].center(19)+"|"+f"Rp{djual[2][4]*r},-".rjust(15)+"|"+"3".center(8)+"|"+f"Rp{3*r*djual[2][4]}".center(14))
print("-"*spasi)

harga_satuan = (djual[2][0] + djual[2][1] + djual[2][2] + djual[2][3] + djual[2][4]) * r 
total_jumlah = sum(djual[3])
total_hasil = (djual[2][0] + djual[2][1] + djual[2][2] + djual[2][3] + djual[2][4]) * r * 3
print(f'SUBTOTAL: |     Rp{harga_satuan},-|   {total_jumlah}   |  Rp{total_hasil},- |'.rjust(77))

print("-"*spasi)
rata_rata = (sum(djual[2]) / total_jumlah) * 3 * r
print(f"""Summary: 
Harga tertinggi adalah    : Rp{r*max(djual[2])},-  ({djual[0][2]} - {djual[1][2]})
Harga terendah adalah     : Rp{r*min(djual[2])},-  ({djual[0][3]} - {djual[1][3]})
Harga Rata-Rata pembelian : Rp{float(rata_rata):.2f}""")
print("\n")

nama_kota = mdata[2]
tanggal = mdata[-1]
gabung = (nama_kota+", "+tanggal).rjust(spasi)
print(gabung)
print("\n"*4)
nama = mdata[3]
strip_akhir = "-"*12
print(nama.rjust(74))
print(strip_akhir.rjust(73))
print("MANAGER".rjust(71))
