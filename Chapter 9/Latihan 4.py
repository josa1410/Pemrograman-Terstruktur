import random
def shuffleString(x,n):
    a = []
    x = list(x)
    i = 0
    while i < n:
        random.shuffle(x)
        shuffle = ''.join(x)
        i += 1
        if shuffle not in a:
            a.append(shuffle)
        else:
            i -= 1
    print(a)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
shuffleString('aku', 5)