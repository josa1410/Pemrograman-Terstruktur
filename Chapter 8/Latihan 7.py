buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
sortharga = sorted(buah.items(), key=lambda x:x[1], reverse=True)
for i in sortharga:
    print(i)