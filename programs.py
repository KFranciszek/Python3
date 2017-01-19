#Napisz program Kalkulator napiwku, w którym użytkownik wprowadza sumę
#ogólną z rachunku wystawionego przez restaurację. Program powinien potem
#wyświetlić dwie kwoty napiwku — w wysokości 15 i 20 procent.

napiwek =  float(input('Podaj wysokość swojego rachunku'))
oblicz15  = int(napiwek*15)/100
oblicz20 = int(napiwek*20)/100
print("Możesz zapłacić: 15% napiwku w kwocie: " + str(oblicz15), " lub 20% w kwocie: " + str(oblicz20))
