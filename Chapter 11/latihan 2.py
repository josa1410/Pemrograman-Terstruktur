from datetime import *

TimeSekarang = datetime.date(datetime.now())
TimeKembali = TimeSekarang + timedelta(days=7)
File = open('D://Mata Kuliah/PROTEK/Pertemuan 11/Chapter 11/Text/DataPeminjam.txt', 'a+')

while True:
    print('')
    KodeMem = input('Tolong Masukkan Kode Member :')
    NamaMem = input('Tolong Masukkan Nama Member :')
    Jbuku = input('Tolong Masukkan Judul Buku   :')

    data = KodeMem + '|'+ NamaMem + '|' + Jbuku + '|' + str(TimeSekarang) + '|' + str(TimeKembali) + '\n'
    File.write(data)

    print('')
    Repeat = input('Ulangi lagi (y/n)		: ')
    if Repeat in('n','N'):
        print('Data Sukses Diinput')
        break
File.close()