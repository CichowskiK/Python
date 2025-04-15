dlugosc = int(input("jaka dlugosc ma miec miarka?\n"))

miarka = ""

for i in range(dlugosc):
    miarka += "|...."
miarka += "|\n"




for i in range(dlugosc + 1):
    if i>=9 :
        miarka +=str(i) +"   "
    else :
        miarka += str(i).ljust(5)
    
    # Wyświetlanie pełnej miarki
print(miarka)
