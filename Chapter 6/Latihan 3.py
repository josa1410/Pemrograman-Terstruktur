def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)


rumuskombinasi = faktorial(5)/faktorial(5-3) * faktorial(3)
print('a.C(5,3) =', rumuskombinasi)

rumuspermutasi = faktorial(10)/faktorial(10-7)
print('b.P(10,7) =', rumuspermutasi)

print(faktorial(2))