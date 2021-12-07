file = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/DataMhs.txt', 'r')
nim = []
nama = []
alamat = []

searchNIM = input('Masukkan NIM yang mau dicari : ')

for x in file:
    pisah = x.split('|')
    nim += [pisah[0]]
    nama += [pisah[1]]
    alamat += [pisah[2]]

if searchNIM in nim:
    index = nim.index(searchNIM)
    print('')
    print('Data Mahasiswa')
    print('NIM      : ', nim[index])
    print('Nama     : ', nama[index])
    print('Alamat   : ', alamat[index])