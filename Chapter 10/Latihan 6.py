inputfile = input('Masukkan nama file : ')
Sandi = int(input('Masukkan nilai n : '))
file = open(inputfile,'r')
read = file.read()

list = []
for x in read:
    if x.isalpha():
        Pindah = ord(x)
        Pindah += Sandi
        if(Pindah > ord('Z')):
            Pindah -= 26
        Last = chr(Pindah)
    elif x.isspace():
        Last = chr(32)
    list += [Last]

filebaru = open('D://Mata Kuliah/PROTEK/Pertemuan 10/Chapter 10/Text/Text6b.txt', 'w')
filebaru.write(''.join(list))
file.close()
filebaru.close()