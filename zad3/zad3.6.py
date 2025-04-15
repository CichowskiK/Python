dlugosc = int(input("jaka dlugosc ma miec siatka?\n"))

miarka = ""

szerokosc = int(input("jaka szerokosc ma miec siatka?\n"))

for i in range(dlugosc):
    for j in range(szerokosc):
        miarka += "+---"
    miarka += "+\n"
    for j in range(szerokosc):
        miarka += "|   "
    miarka += "|\n"

for j in range(szerokosc):
    miarka += "+---"
miarka += "+"
print (miarka)