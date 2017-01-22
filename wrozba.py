
#Napisz program, który symuluje ciasteczko z wróżbą. Program powinien
#wyświetlić jedną z pięciu niepowtarzalnych przepowiedni, dokonując losowego
#wyboru przy każdym uruchomieniu.
#

import random
print("Witaj w aplikacji wróżba")
print("Wylosuj dla siebie unikalną wróżbę")
wrozba = random.randint(1,5)
if wrozba == 1:
    print("To twój dzień dziś odezwie się do Ciebie miłość")
elif wrozba ==2:
    print("W pracy same sukcesy, nie mart się")
elif wrozba == 3:
    print("POdwyższa 700 zł już niedługo")
elif wrozba == 4:
    print("Python developer junior i 3500 zł na rękę już za rok to ty będziesz")
elif wrozba == 5:
print("Twoja rodzinna odnajdzie Boga")
