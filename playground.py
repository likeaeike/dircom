import os
import hashlib
'''
dir1 = input("Verzeichnis 1: ")

for data in os.listdir(dir1):
    print(data)
'''

# aktuelles Verzeicnis ausgeben
#print(os.getcwd())


# array Hashen
def get_arrayHash(bla):
    val = hashlib.md5(b's').hexdigest()
    return val


string = "123"
print(get_arrayHash(string))

#print(hashlib.sha224(b"Nobody inspects the spammish repetition!").hexdigest())
