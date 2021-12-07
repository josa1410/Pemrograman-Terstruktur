file = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/filetext1.txt', 'r')
dalem = file.readlines()

ganjil = 0
genap = 0

for x in range (len(dalem)):
    if int(dalem[x])% 2 == 0:
        genap += 1
    else:
        ganjil += 1

file.close()

print('Jumlah Bilangan Ganjil :', ganjil)
print('Jumlah Bilangan Genap  :', genap)