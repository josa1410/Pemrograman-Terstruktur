buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
nbuah = input('Nama buah yang dibeli\t: ')
berat = int(input('Berapa Kg\t\t\t\t: '))
harga = berat * buah[nbuah]
print('-------------------------------------------')
print('Total Harganya adalah\t: Rp.'+ str(harga))