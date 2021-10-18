kodekaryawan = input('Masukkan Kode Karyawan:')
namakaryawan = input('Masukkan Nama Karyawan:')
golongan = input('Masukkan Golongan:')

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

else:
    print('Golongan Tidak Valid')

Gajikotor = Persen / 100 * Gajipokok
Gajibersih= Gajipokok - Gajikotor

print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan    :' + namakaryawan + '(Kode   :  ' + kodekaryawan  +')')
print('Golongan :' + golongan)
print('-----------------------------------------------------------')
print('Gaji Pokok   :Rp.',Gajipokok)
print('Potongan (' + str(Persen) + '%)  :Rp.',int(Gajikotor))
print('-------------------------------------------------------------')
print('Gaji Bersih  :Rp.',int(Gajibersih))