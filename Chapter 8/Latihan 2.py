def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    nilaibalikan = [a,b,c]
    return nilaibalikan
datanya = []

input1 = int(input('Jumlah Bilangan Bulat Yang Ingin Dimasukkan : '))
x = 0
while (x < input1):
    input2 = int(input('Input Semua Bilangan Yang Telah Ditentukan : '))
    datanya.append(input2)
    x += 1
    continue

hasil= dataStat(datanya)
print('Nilai rata-ratanya, nilai tertinggi, dan nilai terendah dari :', datanya ,'adalah', hasil)