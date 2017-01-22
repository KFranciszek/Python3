#Zmodyfikuj program Jaka to liczba? tak, aby gracz dysponował ograniczoną
#liczbą prób odgadnięcia wybranej przez komputer liczby. Gdy graczowi nie uda
#się odgadnąć tej liczby w wyznaczonej liczbie prób, program powinien
#wyświetlić odpowiedni komunikat z reprymendą



licznik = True
while licznik:

    import random
    liczba = random.randint(1,100)
    print ("Zgadnij liczbę w przedziała 1-100")
    odp = input("Wylosowana liczba to: ")
    if odp == liczba:
        print("Prawidłowa odpoiedź, liczba wylosowana to " + liczba)
    else:
        print("Źle prawidłowa licza to:" + str(liczba))
        break
#########################################
licznik = True
while licznik:
    import random
    liczba = random.randint(1,100)
    print ("Zgadnij liczbę w przedziała 1-100")
    odp = input("Wylosowana liczba to: ")
    licznik += 1
    if odp == liczba:
        print("Prawidłowa odpoiedź, liczba wylosowana to " + liczba)
    elif odp != liczba:
        print("Źle prawidłowa licza to:" + str(liczba))
    if licznik  >= 4:
        print('KONIE, straciłeś wszystkie próby')
        break

