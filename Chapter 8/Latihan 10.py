buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
total = 0

def penambahan():
    nbuah = input('Nama buah yang dibeli\t: ')
    berat = int(input('Berapa Kg\t\t\t\t: '))
    global hargasatuan
    hargasatuan = berat * buah[nbuah]
    global total
    total += hargasatuan
    global perintahlanjut
    perintahlanjut = input('Beli buah yang lain (y/n) ?')

while True:
    print('Nama buah yang dibeli\t: ')
    nbuah = input()
    print('Berapa Kg\t\t\t\t: ')
    berat = int(input())
    hargasatuan = berat * buah[nbuah]
    total += hargasatuan
    perintahlanjut = input('Beli buah yang lain (y/n) ?')
    if perintahlanjut == 'y':
        penambahan()
    if perintahlanjut == 'n':
        print('------------------------------')
        print('Total harga :', total)
        break