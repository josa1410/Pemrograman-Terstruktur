Bahasa_Indonesia = input('Nilai Bahasa Indonesia :')
Matematika = input('Nilai Matematika :')
Ipa = input('Nilai Ipa :')

if (int(Bahasa_Indonesia) in range (0,100)) and (int(Matematika) in range (0,100)) and (int(Ipa) in range (0,100)):
    if(int(Bahasa_Indonesia) > 60) and (int(Matematika) > 70) and (int(Ipa) > 60):
        print('Status Kelulusan: LULUS')
    else:
        print('Status Kelulusan: TIDAK LULUS')
        print('Sebab :')
        if(int(Bahasa_Indonesia) < 60):
            print('Nilai Bahasa Indonesianya kurang dari 60')
        if(int(Matematika) <= 70):
            print('Nilai Matematikanya kurang dari 70')
        if (int(Ipa) < 60):
            print('Nilai Ipanya kurang dari 60')
else:
    print ('Maaf input ada yang tidak valid')