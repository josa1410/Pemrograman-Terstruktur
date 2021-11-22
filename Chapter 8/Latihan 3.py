banyakbil = int(input('Jumlah Data Yang Ingin Dimasukkan :'))
awal = 0
datasemua = []

for awal in range (banyakbil):
    print('Nama Mahasiswa :')
    nama = input()
    banyakKarakter = len(nama)
    gabungan = nama + '(' + str(banyakKarakter) + ' karakter)'
    datasemua.append(gabungan)
datasemua.sort()

for hasil in datasemua:
    print(hasil)