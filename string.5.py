cnp=input("Dati CNP-ul unei persoane: ")
nr=0
if (len(cnp)<13)or(len(cnp)>13):
    print("Nu corespunde cerintei")
else:
    for i in cnp:
        if ord(i) in range(48,58):
            nr+=1
    if (nr==13):
        print("CNP-ul e corect")
    else:
        print("CNP-ul este corect")
