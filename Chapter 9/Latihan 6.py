nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
          {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
          {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
          {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
          {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

x = 0
for isi in nilai:
    mahasiswa = nilai[x]
    nim = mahasiswa['nim']
    nama = mahasiswa['nama']
    mid = str(mahasiswa['mid'])
    uas = str(mahasiswa['uas'])
    nAkhir = round((mahasiswa['mid'] + 2*mahasiswa['uas'])/3)
    stat = ''
    if nAkhir >= 60 :
        stat = 'Lulus'
    else:
        stat = 'Tidak Lulus'


print('==============================================================')
print('NIM		NAMA		 N.MID	 N.UAS		N.AKHIR    STATUS')
print('--------------------------------------------------------------')

for x in range(len(nilai)):
    print(nilai[x]['nim'].ljust(7), end='')
    print(nilai[x]['nama'].ljust(10), end='')
    print(str(nilai[x]['mid']).rjust(8), end='')
    print(str(nilai[x]['uas']).rjust(10), end='')
    print(str(nAkhir).rjust(13), end='')
    print(stat.rjust(13))

print('================================================================')