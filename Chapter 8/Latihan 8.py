buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def ratarata():
    rata = sum(buah.values())/len(buah)
    print('Rata-Rata Harga Buahnya Adalah: Rp.', rata)
ratarata()