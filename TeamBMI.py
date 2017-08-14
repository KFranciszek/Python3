team = []
def DicBMI_data():
    member= True
    while member:
        name = input('Podaj imie')
        weight = int(input('Podaj swoją wage'))
        height = float(input('Podaj swój wzrost'))
        bmi = weight//(2*height)
        bmiDic = {'name': name,
                  'bmi': bmi}

        team.append(bmiDic)
        pytanie = input('Czy policzyć jeszcze raz  T/N')
        if pytanie == 'N':
            member = False
            return team


def BMI_print ():

    for i in team:
        print(i)





DicBMI_data()
BMI_print()
