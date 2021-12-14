from datetime import *

def diffDate(x):
    Tanggal = datetime.date(datetime.now())
    interval = abs(x - Tanggal)
    print('Selisih tanggal', Tanggal ,'dan',x, 'adalah',interval.days,'hari')

x = date(2018,12,30)
diffDate(x)
