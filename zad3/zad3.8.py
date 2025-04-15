sekw1 = [1, 2, 2, 2, 3, 4, 5, 6, 6]
sekw2 = [2, 4, 6, 7, 7, 8, 10, 9]

set1=  set(sekw1)
set2= set (sekw2)

commonElements =  set(set1 & set2)


print ("elementy wspolne:", commonElements)

allElements = set(set1 | set2)

print("\nwszystkie elementy:", allElements)