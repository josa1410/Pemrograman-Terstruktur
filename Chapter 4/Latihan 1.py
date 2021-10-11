import math
tarifawal =200000
tarifselanjutnya =10000
jamawalrental =6.00
jamakhirrental =23.50
lamarental =math.ceil(jamakhirrental-jamawalrental)
lamarentallanjutan =lamarental - 12
tarifrentallanjutan =lamarentallanjutan * tarifselanjutnya
totalharga =tarifawal + tarifrentallanjutan
print(totalharga)

