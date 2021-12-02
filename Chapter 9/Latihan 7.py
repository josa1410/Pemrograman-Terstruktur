mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('===========================================================================')
print('NIM      NAMA MAHASISWA          TGL LAHIR          TEMPAT LAHIR')
print('---------------------------------------------------------------------------')

x = 0
for isi in mhs:
       nilai = mhs[x].split(':')
       nim = nilai[0]
       nama = nilai[1]
       tanggallahir = nilai[2].split('-')
       tanggallahir = tanggallahir[2] +'/'+ tanggallahir[1] +'/'+ tanggallahir[0]
       tempat = nilai[3]
       x += 1
       print(nim.ljust(9), end='')
       print(nama.ljust(24), end='')
       print(tanggallahir.ljust(19), end='')
       print(tempat.ljust(12))

print('--------------------------------------------------------------')