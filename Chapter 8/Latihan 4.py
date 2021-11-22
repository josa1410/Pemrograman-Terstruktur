try:
    List = ['bayam', 'kangkung', 'wortel', 'selada']
    print('Daftar Sayuran :', List)
    print('PILIHAN :','\nA. Menambah data sayur','\nB. Menghapus data sayur','\nC.Menampilkan data sayur')
    while True:
        pilihan1 = input('Pilihan (A/B/C) : ')
        if pilihan1 == 'A' or pilihan1 == 'a':
            print('Tambahkan data sayur : ', end=' ')
            a = input()
            List.append(a)
        elif pilihan1 == 'B' or pilihan1 == 'b':
            print('Data sayur yang ingin dihapus : ', end=' ')
            b = input()
            if b in List:
                List.remove(b)
            else:
                print('Maaf data tidak ditemukan ')
        elif pilihan1 == 'C' or pilihan1 == 'c':
            c = set(List)
            d = list(c)
            print('Daftar data sayur : ', )
            for datad in d:
                print(datad)
        else:
            print('input tidak valid!!')
            continue
        pilihan2 = input('Ingin memilih lagi? (y/n) : ')
        if pilihan2 == 'Y' or pilihan2 == 'y':
            print('PILIHAN :','\nA. Menambah data sayur','\nB. Menghapus data sayur','\nC.Menampilkan data sayur')
            continue
        if pilihan2 == 'n' or pilihan2 == 'N':
            break
        else:
            print('input tidak valid!!')
            continue
except NameError:
    print('Maaf data Nama Salah')