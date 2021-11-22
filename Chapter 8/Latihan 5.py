bil = [2, 4, 5, 6]
tuple = tuple(bil)

def kuadrat(x):
    hasil =[]
    for i in range(len(x)):
        hasil.append(x[i]**2)
    return hasil

print(kuadrat(tuple))