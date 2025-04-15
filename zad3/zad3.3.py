R1= range(1,30,3)
R2= range(2,30,3)

L1=list(R1)
L2=list(R2)

L= L1+L2

L.sort()

for i in L :
    print(i)