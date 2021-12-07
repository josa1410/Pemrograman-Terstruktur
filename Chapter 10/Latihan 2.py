file = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/DataMhs.txt', 'a+')

while True:
    nim = input('Masukkan NIM		: ')
    nama = input('Masukkan Nama Mhs	: ')
    alamat = input('Masukkan Alamat     : ')
    Data = nim + '|' + nama + '|' + alamat + '\n'
    file.write(Data)

    print('')
    Repeat = input('Ulangi input lagi (y/n) : ')
    if Repeat in('n', 'N'):
        break

file.close()