baris = 0
total = 0
for a in range(0,100):
    if(a % 2 == 1):
        print(a)
    baris = baris + 1
    total = total + baris

print('Banyaknya bilangan ganjil :', baris)
print ('Jumlah seluruh bilangan:', total)