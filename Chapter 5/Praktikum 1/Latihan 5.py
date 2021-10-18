kodekaryawan = input('Masukkan Kode Karyawan:')
namakaryawan = input('Masukkan Nama Karyawan:')
golongan = input('Masukkan Golongan:')
status = input('Masukkan Status(Menikah/Belum Menikah):')

if (status == 'Menikah') or (status =='menikah'):
    jumlahanak = input('Masukan Jumlah Anak:')
elif (status == 'Belum Menikah') or (status == 'belum menikah'):
    tunjanganmenikah = 0
    tunjangananak = 0
    jumlahanak = 0

if(golongan == 'A') or (golongan == 'a'):
    Gajipokok = 10000000
    Persen = 2.5
elif(golongan == 'B') or (golongan == 'b'):
    Gajipokok = 8500000
    Persen = 2.0
elif(golongan == 'C') or (golongan == 'b'):
    Gajipokok = 7000000
    Persen = 1.5
elif (golongan == 'D') or (golongan == 'd'):
    Gajipokok = 5500000
    Persen = 1.0
if(status == 'Menikah') or (status == 'menikah'):
    tunjanganmenikah = Gajipokok*(10/100)
if int(jumlahanak) >0:
    tunjangananak = int(jumlahanak)*(Gajipokok*(5/100))
elif (jumlahanak == '-'):
    tunjangananak = 0

else:
    print('Golongan Tidak Valid')

Gajikotor = Gajipokok + tunjanganmenikah +tunjangananak
Potongan = Persen/100 * Gajikotor
Gajibersih= Gajikotor - Potongan

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan    :' + namakaryawan + '(Kode   :  ' + kodekaryawan  +')')
print('Golongan :' + golongan)
print('Status Menikah   :' + status)
print('Jumlah Anak  :' + str(jumlahanak))
print('-----------------------------------------------------------')
print('Gaji Pokok   :Rp.',Gajipokok)
print('Potongan (' + str(Persen) + '%)  :Rp.',int(Gajikotor))
print('-------------------------------------------------------------')
print('Gaji Bersih  :Rp.',int(Gajibersih))