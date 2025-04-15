line = "ab cd\ne\tf\ng hi\nGvR"
word = "napis"

print ("to nasz wielowierszowy napis line:\n",line, "\na to nasz napis word: \n",word)

#zad 2.10

howManyWords=line.split()
print("zad 2.10\nliczba wyrazow: " ,len(howManyWords))

#zad 2.11

separated_word = "_".join(word)
print("zad 2.11\n", separated_word)

#zad 2.12

pierwsze = ''.join([litera[0] for litera in howManyWords])
ostatnie = ''.join([litera[-1] for litera in howManyWords])

print ("zad2.12\nlitery na poczatku wyrazow:",pierwsze, "\nlitery na koncu wyrazow:",ostatnie)

#zad 2.13

arr = []
for i in range(len(howManyWords)):
    arr.append(len(howManyWords[i]))

print ("zad 2.13\nilosc  liter w line to:", sum(arr))

#zad 2.14

longest = max(howManyWords, key= len)

print("zad2.14\nnajdluzsze slowo to:", longest, "\njego dlugosc to:", len(longest))

#zad 2.15

L = [1, 2, 3, 4, 5, 12, 14, 16, 203]
napisL = ''.join(map(str, L))

print("zad 2.15\nnapis L:", napisL)

#zad 2.16

newLine = line.replace("GvR", "Guido van Rossum")

print ("zad 2.16\nnapis po zmianie:\n", newLine)

#zad 2.17

alfabetycznie = sorted(howManyWords, key= str.casefold)
wielkosc = sorted(howManyWords, key= len)

print("zad 2.17\nposortowanie alfabetycznie:", alfabetycznie,"\nposortowanie pod wzgledem wielkosci:", wielkosc)

#zad 2.18

liczba = 13870321000784300
liczbaString = str(liczba)
zera = liczbaString.count('0')

print("zad 2.18\nilosc zer w liczbie:" ,liczba," to:", zera)

#zad 2.19

Lwypelnione = []
Lstring = []
for i in range(len(L)):
    Lstring.append(str(L[i]))
    Lwypelnione.append(Lstring[i].zfill(3))



print("zad 2.18\n", Lwypelnione)