#!/usr/bin/env python3
import os
import subprocess as sub
import hashlib


# Verzeichnisse 1 und 2 eingeben und als Rückgabe zurück geben
def get_directory(dir):
    dir = input("Ersten Verzeichnispfad eingeben: ")
    return dir

    '''
    rückgabe aus get_directory ausgeben und mit get_dataHash fortfahren!
    '''

# in for-Schleife jede (nicht Versteckte?) Datei Hashen und in Array schreiben
def get_dataHash(dir):
    files = []
    # for-Schleife in Funktion auslagern, weil zwei mal benötigt!
    for datei in os.listdir(dir):
                #os.listdir(PFAD)
        files.append(datei)
    return files
    #print(files)

# Array hashen

def get_arrayHash(content):
    #print(content)
    for x in content:
        x += hashlib.md5(content.encode()).hexdigest()
        print(x)
        return x



# Hashes vergleichen mit Ausgabe
def compareHash():
    if aHash1 == aHash2:
        print("Success! Directory1 equals Directory2!")
    else:
        print("Directorys are not equal")

# Main Methode, ruft alle Funktionen auf
def main():
    dir1, dir2 = "", ""
    #counter = 0 IN get_directory EINGABE VERSCHÖNERN
    dir1 = get_directory(dir)
    dir2 = get_directory(dir)
    content1 = get_arrayHash(dir1)
    content2 = get_dataHash(dir2)
    #print(content1)
    #get_arrayHash()
    #compareHash()


if __name__ == "__main__": main()
