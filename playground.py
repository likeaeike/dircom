import hashlib
m = hashlib.md5()

list = ['MacOS', 'Install GitKraken']

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
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.md5(hash_string.encode().hexdigest())
    return sha_signature
'''
