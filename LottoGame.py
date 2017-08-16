wynik=[]
count = 6
while count:
    import random
    lotto =random.randint(1,49)
    wynik.append(lotto)
    if len(wynik) >=6:
        print("Twoje szczęśliwe liczby to: " + str(wynik))
        break
