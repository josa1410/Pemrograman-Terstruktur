def bintang(n):
    spasi = 2*n-1
    for i in range(int(n/2)):
        print(('*'*(2*i+1)).center(spasi))

    for i in reversed (range(int(n/2+1))):
        print(('*' * (2 * i + 1)).center(spasi))


bintang(7)