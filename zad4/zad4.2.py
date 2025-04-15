def miarka(len):
    miarka = ""
    for i in range(len):
        miarka += "|...."
    miarka += "|\n"

    for i in range(len + 1):
        if i>=9 :
            miarka +=str(i) +"   "
        else :
            miarka += str(i).ljust(5)

    return miarka

def siatka(len, width) :
    siatka = ""
    for i in range(len):
        for j in range(width):
            siatka += "+---"
        siatka += "+\n"
        for j in range(width):
            siatka += "|   "
        siatka += "|\n"

    for j in range(width):
        siatka += "+---"
    siatka += "+"
    return siatka

dlugosc = int(input("jaka dlugosc ma miec miarka?\n"))

print(miarka(dlugosc))

dlugoscS = int(input("jaka dlugosc ma miec siatka?\n"))
szerokosc = int(input("jaka szerokosc ma miec siatka?\n"))

print(siatka(dlugoscS, szerokosc))