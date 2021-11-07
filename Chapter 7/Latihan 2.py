import os
namafile = input('Masukkan nama file: ')
direktori = os.path.exists(namafile)
try:
    if direktori is True:
        datatambah = open(namafile, 'a')
        datatambah.write(input('Data yang mau ditambahkan: '))
        lagi = input('Mau lagi (y/n): ')

        while (lagi == 'y') or (lagi == 'Y'):
            datatambah.write(input('Data yang mau ditambahkan: '))
            lagi = input('Mau lagi (y/n): ')

            if (lagi == 'n') or (lagi == 'N'):
                datatambah.close()
                break
    else:
        print('Maaf File Tidak Ditemukan')
except PermissionError:
    print('Maaf Tidak Diperbolehkan')