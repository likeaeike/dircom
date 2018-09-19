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
def get_dataArray(dir):
    files = []
    # for-Schleife in Funktion auslagern, weil zwei mal benötigt!
    for datei in os.listdir(dir):
                #os.listdir(PFAD)
        files.append(datei)
    return files


# Array hashen

def get_arrayHash(content):
    rueckgabe = ""
    for elem in content:
        elem = elem.encode("utf-8")
        hashlib.md5().update(bytes(elem))
        #print(hashlib.md5().hexdigest())
        rueckgabe += hashlib.md5().hexdigest()
    #print(rueckgabe)
    return rueckgabe


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
    dataArray1 = get_dataArray(dir1)
    dataArray2 = get_dataArray(dir2)
    content1 = get_arrayHash(dataArray1)
    content2 = get_arrayHash(dataArray2)
    #compareHash()


if __name__ == "__main__": main()
