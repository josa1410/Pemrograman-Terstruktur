file = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/Bil1.txt', 'r')
list = []
baca = file.readlines()
hasil = []

for x in range (len(baca)) :
    split = baca[x].split('|')
    isi = [int(split[0]), int(split[1].replace('\n',''))]
    hasil += [isi]

filebaru = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/Bil2.txt', 'w')

for x in range (len(hasil)) :
    jumlah = sum (hasil[x])
    filebaru.write(str(jumlah) + '\n')

file.close()
filebaru.close()