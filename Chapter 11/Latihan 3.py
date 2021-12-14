from datetime import *

TimeSekarang =datetime.date(datetime.now())
File = open('D://Mata Kuliah/PROTEK/Pertemuan 11/Chapter 11/Text/DataPeminjam.txt', 'r')
Find = input('Mohon Ketik Kode Membernya :')

KodeMem = []
NamaMem = []
Jbuku = []
TanggalPinjam = []
TanggalBalik = []

for list in File:
    Hilang = list.split('|')
    KodeMem += [Hilang[0]]
    NamaMem += [Hilang[1]]
    Jbuku += [Hilang[2]]
    TanggalPinjam += [Hilang[3]]
    TanggalBalik += [Hilang[4]]

if Find in  KodeMem:
    i = KodeMem.index(Find)
    print('Data Peminjaman Buku')
    print('Kode 	        	     :', KodeMem[i])
    print('Nama 		             :', NamaMem[i])
    print('Judul  		             :', Jbuku[i])
    print('Tanggal Mulai Peminjaman :', TanggalPinjam[i])
    print('Tanggal Maks Peminjaman  :', TanggalBalik[i].replace('\n', ''))
    print('Tanggal Pengembalian	 :', str(TimeSekarang))

    Pinjem = TanggalPinjam[i].split('-')
    for isi in Pinjem:
        Tahun = Pinjem[0]
        Bulan = Pinjem[1]
        Tanggal = Pinjem[2]

    Selisih = TimeSekarang - date(int(Tahun),int(Bulan),int(Tanggal))
    Shari =Selisih.days
    if Shari >= 7:
        Terlambat = Shari - 7
    else:
        Terlambat = 0

    print('Keterlambatan            :', Terlambat, 'hari')
    print('Denda			         : Rp',Terlambat*2000)

else:
    print('Data tidak ditemukan')