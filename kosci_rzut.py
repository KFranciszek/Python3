import random
kosc = random.randint(1,6)
kosc2 =random.randint(1,6)
if kosc > kosc2:
    print ("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), ' Gracz 1 wygywa')
elif kosc < kosc2:
    print("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), 'Gracz 2 wygywa')
elif kosc == kosc2:
    print("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), "Remis")
else:
    print("Brak wyniku")
#######
rzut = True
while rzut:
 import random
 kosc = random.randint(1,6)
 kosc2 =random.randint(1,6)
 if kosc > kosc2:
     print ("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), ' Gracz 1 wygywa')
 elif kosc < kosc2:
    print("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), 'Gracz 2 wygywa')
 elif kosc == kosc2:
    print("Gracz1: " +  str(kosc), "Gracz2: " + str(kosc2), "Remis")
 else:
    print("Brak wyniku")
 a =  input("Grasz dalej?")
 if a == "Nie":
     break
