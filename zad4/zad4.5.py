lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def odwracanieI(L, left, right) :


    zasieg = int((right-left+1)/2)

    for i in range(zasieg):
        temp = L[left+i]
        L[left+i] = L[right-i]
        L[right-i] = temp
    return L

def odwracanieR(L, left, right):
    if right<=left:
        return L
    else :
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        return odwracanieR(L, left+1, right-1)

print ("poczatkowa lista\n", lista)

print("lista po wywolaniu fukncji iteracyjnej left= 0, right=19\n", odwracanieI(lista, 0, 19))
print("lista po ponownym odwroceniu, tym razem rekurencyjne, left = 3, right= 12\n",odwracanieR(lista, 3, 12))