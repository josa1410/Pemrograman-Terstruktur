myData = ['apel', 'rambutan', 'jeruk ']
myDataTup = tuple(myData)

def sortStringByChar(x):
    sort = sorted(x , key=len, reverse=True)
    return sort
print(sortStringByChar(myDataTup))