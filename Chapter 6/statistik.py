def sum(*bilangan):
    hasil = 0
    for isi in bilangan:
        hasil += isi
    return (hasil)

def average(*bilangan):
    i = 0
    for isi in bilangan:
        i += 1
    hasil = sum(*bilangan)/i
    return hasil

def maximal(*bilangan):
    nilai = max(*bilangan)
    return nilai

def minimal(*bilangan):
    nilai = min(*bilangan)
    return nilai
