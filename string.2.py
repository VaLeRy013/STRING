s=input("Dati un sir: ")
nrmaj=0
nrc=0
nrs=0
for i in s:
    if ord(i) in range(65,91):
        nrmaj+=1
print(nrmaj)
for i in s:
    if ord(i) in range(97,123):
        nrmaj+=1
print(nrc)
for i in s:
    if ord(i) in range(33,42):
        nrs+=1
print(nrs) 
