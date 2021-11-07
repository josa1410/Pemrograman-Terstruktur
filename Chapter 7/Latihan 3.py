print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

bdata = 0
jumnilai = 0
mbilangan= True

while mbilangan:
    try:
        bbulat = int(input('Masukkan bilangan bulat :'))
        jumnilai += bbulat
        bdata += 1
        lagi = input('Lagi (y/n)? : ')
        if (lagi == 'y') or (lagi == 'Y'):
            mbilangan = True
        elif (lagi == 'n') or (lagi == "N"):
            mbilangan = False
        else:
            print('Maaf Input Tidak Valid')
    except ValueError:
        print('Bukan bilangan bulat')

ratarata = jumnilai/bdata
print('Rata-ratanya adalah:', ratarata)