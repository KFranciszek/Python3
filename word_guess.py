
##### Version 1 #####
import random
words = ['cat', 'dog', 'house','love', 'computer']
print('Zacznijmy grę w zgadywanie słów')
i=random.choice(words)
proby = 5
guese = True
while True:
    print("Słowo to ma " , len(i), 'liter')
    liter=input('Wybierz literkę do podpowiedz')
    if liter in i:
       print("Ta litera znajduje się w słwoie")
       zgadnij=input("Czy chcesz zgadnąć słowo? Tak/Konty")
       if zgadnij == "Tak":
           slowo=input("Podaj słowo")
           if slowo in words:
               print("Brawo zgadłeś!")
               break
       elif zgadnij =="KOnty":
           continue
           roby -= 1
           print("Pozstało ci ", proby)



    else:
        print("Litera nie znajduje się w słowniku")
        proby -= 1
        print("Pozstało ci ", proby)
        if proby > 5:
            break
            print("koniec gry Przegrałeś")


###### Version 2 #######
import random
words = ['cat', 'dog', 'house','love', 'computer']
print('Zacznijmy grę w zgadywanie słów')
i=random.choice(words)
proby = 5
guese = True
while True:
    print("Słowo to ma " , len(i), 'liter')
    liter=input('Wybierz literkę do podpowiedz')
    if liter in i:
       print("Ta litera znajduje się w słwoie")
       zgadnij=input("Czy chcesz zgadnąć słowo? Tak/Konty")
       if zgadnij == "Tak":
           slowo=input("Podaj słowo")
           if slowo in words:
               print("Brawo zgadłeś!")
               break
       elif zgadnij =="KOnty":
           continue
           roby -= 1
           print("Pozstało ci ", proby)



    else:
        print("Litera nie znajduje się w słowniku")
        proby -= 1
        print("Pozstało ci ", proby)
        if proby  ==0:
            break
print("koniec gry Przegrałeś")
