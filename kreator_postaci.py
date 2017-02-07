#Do poprawy jeszcze!!!

punkty = 30
print("Witaj w grze Magiczni wojownicy, możesz przyznać sumę 30 punktów na cechy takie jak siła, zdrowie, mądrość i zręczność")


siła = int(input("ile chce przekazać punktów na siłę"))
if siła > punkty:
    print("Nie możesz przyznać więcej niż 30 punktów")
elif siła < punkty:
    print("Pozostał Ci", punkty-siła)
    After_siła=punkty -siła


zdrowie = int(input("ile chce przekazać punktów na zdrowie"))
if zdrowie > punkty:
    print("Nie możesz przyznać więcej niż 30 punktów")
elif zdrowie < punkty:
    print("Pozostał Ci", After_siła-zdrowie)
    After_zdrowie = After_siła - zdrowie


mądrość = int(input("ile chce przekazać punktów na mądrość"))
if mądrość > punkty:
    print("Nie możesz przyznać więcej niż 30 punktów")
elif mądrość < punkty:
    print("Pozostał Ci", After_zdrowie-mądrość)
    After_mądrość = After_zdrowie - mądrość


zręcznosć = int(input("ile chce przekazać punktów na zręczność"))
if zręcznosć > punkty:
    print("Nie możesz przyznać więcej niż 30 punktów")
elif zręcznosć < punkty:
    print("Pozostał Ci", After_mądrość- zręcznosć)
    After_zręcznosć= After_zdrowie - zręcznosć

sumaPTK = siła + zdrowie + mądrość + zręcznosć
zostało =  punkty - sumaPTK
cechy = {'Siła':siła, 'Zdrowie': zdrowie, "Mądrość":mądrość, "Zręczność":zręcznosć}
kontynowac = "Czy chcesz rozdać pozostałe punkty"



if sumaPTK == punkty:
    print("Lista twoich cech wgląda natępująco ", cechy, end=" ")
    print("Pozostało Ci 0 punktów")
elif sumaPTK != punkty:
    print("Pozstało Ci", zostało, " punktów")
    print(kontynowac)




