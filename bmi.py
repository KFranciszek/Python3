h = float(input("Podaj swój wzrost"))
w =float(input('Podaj swoją wagę'))
bmi = w//h**2
print("Twoje BMI wynosi: " + str(bmi))
#####


h = float(input("Podaj swój wzrost"))
w =float(input('Podaj swoją wagę'))
bmi = w//(h**2)

if bmi < 20:
    odp="Niedowaga"
elif bmi >= 20 and bmi <= 25 :
    odp="Norma"
elif bmi > 25:
    odp="Nadwaga"

print("Twoje BMI wynosi: " + str(bmi) + "jest to: " + odp)

#######
g = str(input('Podaj płeć wpisując K lub M'))
h = float(input("Podaj swój wzrost"))
w =float(input('Podaj swoją wagę'))
bmi = w//(h**2)

if g == "K":
     if bmi < 16.5:
        odp="Niedowaga"
     elif bmi >= 16.5 and bmi <= 20 :
        odp="Norma"
     elif bmi >= 20 and bmi <= 25:
        odp="Nadwaga"
     elif bmi > 25:
        odp= 'Otyłość'
else:
    if bmi < 18.5:
        odp = "Niedowaga"
    elif bmi >= 18.5 and bmi <=  22.5:
        odp = "Norma"
    elif bmi >= 22.5 and bmi <= 27.5:
        odp = "Nadwaga"
    elif bmi > 27.5:
        odp = 'Otyłość'

print("Twoje BMI wynosi: " + str(bmi) + " jest to: " + odp)
