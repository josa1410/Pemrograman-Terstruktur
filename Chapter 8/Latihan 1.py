banyakbil = int(input('Jumlah Bilangan Bulat Yang Ingin Dimasukkan :'))
awal = 0
databanyakbil=[]
for awal in range(banyakbil):
    Mbilangan = input('Input Semua Bilangan Yang Telah Ditentukan : ')
    databanyakbil += [Mbilangan]
    databanyakbil.sort(reverse=True)
    print(databanyakbil)