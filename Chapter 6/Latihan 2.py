import math

def starformation1(n):
    kolom = 1
    i = 0
    while i < n:
        startawal = 0
        while startawal < kolom:
            print('*', end='')
            startawal += 1
        print('')
        i += 1
        kolom += 1

def starformation2(n):
    baris = 5
    i = 0
    while i < baris:
        posisi = 0
        while posisi < n:
            print('* ', end='')
            posisi += 1
        print('')
        i += 1
        n -= 1

def starformation3(n):
    if n % 2 == 0:
        starformation1(n/2)
        starformation2(n/2)
    else:
        starformation1(math.ceil(n / 2))
        starformation2(n//2)

starformation1(4)
starformation2(4)
starformation3(7)