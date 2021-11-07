try:
    nama = input('Masukkan nama file:')
    file = open(nama, "r")
    hasil= file.read()
    print('Isi file', nama ,'adalah:\n',hasil)
except FileNotFoundError:
    print('File tidak ditemukan atau salah penulisan')
