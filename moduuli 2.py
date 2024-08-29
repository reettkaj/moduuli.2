#tehtävä1
käyttäjä=input('Anna nimesi: ')
print("Terve, " + käyttäjä + "!")

#tehtävä2
import math
säde=float(input("Anna säde: "))
pinta_ala= math.pi * säde * 2
print(f"Ympyrän pinta-ala on {pinta_ala: .2f}")

#tehtävä3
kanta=float(input("Anna kanta: "))
korkeus=float(input("Anna korkeus:"))
pinta_ala= kanta*korkeus
piiri=kanta*2+korkeus*2

print("Suorakulmion pinta_ala on " + str(pinta_ala))
print("Suorakulmion piiri on " + str(piiri))

#tehtävä4
Ensimmäinen_luku= int(input("Anna ensimmäinen luku: "))
Toinen_luku=int(input("Anna toinen luku: "))
Kolmas_luku= int(input("anna kolmas luku:"))

summa= Ensimmäinen_luku + Toinen_luku + Kolmas_luku
tulo= Ensimmäinen_luku * Toinen_luku * Kolmas_luku
keskiarvo= summa / 3

print("Summa on " + str(summa))
print("Tulo on " + str(tulo))
print("keskiarvo on " + str(keskiarvo))


#tehtävä5
print('Anna leiviskät: ')
leiviskä= float(input())
print('Anna naulat: ')
naula= float(input())
print('Anna luodit: ')
luoti = float(input())

leiviskät = leiviskä * 20 * 32 * 13.3
naulat = naula * 32 * 13.3
luodit = luoti * 13.3

Laskutulos = leiviskät + naulat + luodit

kilot = Laskutulos / 1000
kilo = int(kilot)

grammat = (kilot+kilo) * 1000
print(f"Massa nykymittojen mukaan on {kilo} kiloa ja {grammat:.2f} grammaa.")

#(tehtävä6)
#kesken
import random
kolmenumeroinen_koodi = ""
nelinumeroinen_koodi = ""

for _ in range(3):
kolmenumeroinen_koodi += str(random.randint(0,9))

for _ in range(4):
nelinumeroinen_koodi += str(random.randint(1,6))

print(f"Kolminumeroinen koodi {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi {nelinumeroinen_koodi}")


#tehtävä6
import random
koodi1 = random.randint(0,9)
koodi1str = str(koodi1)
koodi2 = random.randint(0,9)
koodi2str = str (koodi2)
koodi3 = random.randint(0,9)
koodi3str = str (koodi3)

nro1 = random.randint(1,6)
nro1str = str(nro1)
nro2 = random.randint(1,6)
nro2str = str (nro2)
nro3 = random.randint(1,6)
nro3str = str (nro3)
nro4 = random.randint(1,6)
nro4str = str (nro4)


koodi = koodi1str + koodi2str + koodi3str
print (f"Tässä kolmenumeroinen koodi: {koodi}")

toinenkoodi = nro1str + nro2str + nro3str + nro4str
print(f"Tässä nelinumeroinen koodi:  {toinenkoodi}")




