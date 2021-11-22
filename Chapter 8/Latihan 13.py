nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaiakhir():
    for x in range(len(nilaiMhs)):
        nilai = (nilaiMhs[x]['mid'] + nilaiMhs[x]['uas']*2)/3
        nilaiMhs[x]['akhir'] = nilai
    print(sorted(nilaiMhs, key= lambda x: x['akhir'], reverse=True))

nilaiakhir()