a=input("Dati primul cuvant: ")
b=input("Dati al doilea cuvant: ")
c=input("Dati al treilea cuvant: ")
d=input("Dati al patrulea cuvant: ")
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print("Are loc o eroare")
litera1=a[:2]
litera2=b[0]
litera3=c[:3]
litera4=d[:(len(d)//2)]
print("Cuvintele sunt: ",a, b, c, d, sep="  ")
print("Cuvantul format este: ",litera1+litera2+litera3+litera4)
