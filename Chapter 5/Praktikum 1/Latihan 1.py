Bahasa_Indonesia = input('Nilai Bahasa Indonesia :')
Matematika = input('Nilai Matematika :')
Ipa = input('Nilai Ipa :')

if(int(Bahasa_Indonesia) > 60) and (int(Matematika) > 70) and (int(Ipa) > 60):
    print('Status Kelulusan: LULUS')
else:
    print('Status Kelulusan: TIDAK LULUS')