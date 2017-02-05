
punkty = 30
siła = input("ile chce przekazać punktów na siłę")
zdrowie = input("ile chce przekazać punktów na zdrowie")
mądrość = input("ile chce przekazać punktów na mądrość")
zręcznosć = input("ile chce przekazać punktów na zręczność")
cechy = {'Siła':siła, 'Zdrowie': zdrowie, "Mądrość":mądrość, "Zręczność":zręcznosć}
###
punkty = 30
print("Witaj w grze Magiczni wojownicy, możesz przyznać sumę 30 punktów na cechy takie jak siła, zdrowie, mądrość i zręczność")
siła = int(input("ile chce przekazać punktów na siłę"))
if siła > 30:
    print("Nie możesz przyznać więcej niż 30 punktów")
   

zdrowie = int(input("ile chce przekazać punktów na zdrowie"))
if zdrowie > 30:
    print("Nie możesz przyznać więcej niż 30 punktów")

mądrość = int(input("ile chce przekazać punktów na mądrość"))
if mądrość > 30:
    print("Nie możesz przyznać więcej niż 30 punktów")

zręcznosć = int(input("ile chce przekazać punktów na zręczność"))
if siła > 30:
    print("Nie możesz przyznać więcej niż 30 punktów")

sumaPTK = siła + zdrowie + mądrość + zręcznosć
zostało =  punkty - sumaPTK
cechy = {'Siła':siła, 'Zdrowie': zdrowie, "Mądrość":mądrość, "Zręczność":zręcznosć}
kontynowac = "Czy chcesz rozdać pozostałe punkty"
if siła > 30:
    print("Nie możesz przyznać więcej niż 30 punktów")

if sumaPTK == punkty:
    print(cechy)
    print("Pozostało Ci 0 punktów")
elif sumaPTK < punkty:
    print(cechy)
    print("Pozstało Ci", zostało, " punktów")
    print(kontynowac)


