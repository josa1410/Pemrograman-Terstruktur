from random import randint
Bilangan = randint(0,100)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
while True:
    Tebakan = int(input('Tebakan Anda:'))
    if Tebakan < Bilangan:
        print('Hehehe… Bilangan tebakan anda terlalu kecil Coba Lagi Deh')
    elif Tebakan > Bilangan:
        print('Hehehe… Bilangan tebakan anda terlalu besar Coba Lagi Deh')
    elif Tebakan == Bilangan:
        print('Yeeeeaaaayy… Bilangan tebakan anda BENAR :-)')
        break