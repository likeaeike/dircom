import hashlib
m = hashlib.md5()

list = ['eike', 'eike', 'eike', 'eike']
ergebnis = ""
'''
def get_arrayHash(list):
    #m = hashlib.md5()
    list = list.strip()
    rueckgabe = ""
    for elem in list:
        var = hashlib.md5(list)
        print (var)
    #return rueckgabe

new = get_arrayHash(list)
'''
for elem in list:
        print(elem)
        elem = elem.encode("utf-8")
        m.update(bytes(elem))
        ergebnis += m.hexdigest()
        #ergebnis += var
        print (ergebnis)
