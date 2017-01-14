h = float(input("Podaj swój wzrost"))
w =float(input('Podaj swoją wagę'))
bmi = w/h
print("Twoje BMI wynosi: " + str(bmi))
#####


h = float(input("Podaj swój wzrost"))
w =float(input('Podaj swoją wagę'))
bmi = w/h

if bmi > 20:
    odp="Niedowaga"
elif bmi <= 20 and bmi > 25 :
    odp="Norma"
elif bmi < 25:
    odp="Nadwaga"

print("Twoje BMI wynosi: " + str(bmi) + "jest to: " + odp)
######


