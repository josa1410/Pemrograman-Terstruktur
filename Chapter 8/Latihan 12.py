buah = {'apel':5000, 'jeruk':8500, 'mangga':7800, 'duku':6500}
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
    print('Menu: \nA.Tambah Data \nB.Beli Buah \nC.Hapus data Buah')
    milih = input('Pilihan menu :')
    if milih == 'A' or milih == 'a':
        namabaru = input('Masukkan Nama Buah :')
        if namabaru in buah.keys():
            print('Maaf Buah sudah Terdapat Di List')
        else:
            hargabaru = int(input('Masukkan Harga Satuan : '))
            buah[namabaru]=hargabaru
            for a,b in buah.items():
                print('-' + a +'(Harga Rp '+ str(b) +')')
    if milih == 'B' or milih == 'b':
        for a, b in buah.items():
            print('-' + a + '(Harga Rp ' + str(b) + ')')
        nbuah = input('Nama buah yang dibeli\t: ')
        berat = int(input('Berapa Kg\t\t\t\t: '))
        hargasatuan = berat * buah[nbuah]
        total += hargasatuan
        perintahlanjut = input('Beli buah yang lain (y/n) ?')
        if perintahlanjut == 'y':
            penambahan()
        if perintahlanjut == 'n':
            print('------------------------------')
            print('Total harga :', total)
            break
    if milih == 'C' or milih == 'c':
        hapus =input('Masukkan Nama Buah : ')
        if hapus not in buah.keys():
            print('Maaf Buah Tidak Berada dalam List')
        else:
            del buah[hapus]