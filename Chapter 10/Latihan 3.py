file = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/DataMhs.txt', 'r')

read = file.readlines()
daftar = []

for isi in range (len(read)):
    Lama = read[isi]
    Baru = Lama.split('|')
    Dictionary = {'NIM' : Baru[0], 'Nama' : Baru[1], 'Alamat' : Baru[2].replace('\n', '')}
    daftar += [Dictionary]

print('Data Mahasiswa : ', daftar)
file.close()