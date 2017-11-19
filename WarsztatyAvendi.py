# print ('Mama')
credits()
print('kot')
print(2+2)
print('Hello World')
s=10+10/3
print(round(s))
a = 6
b =3
x=a+b
print(dir())
#zadanie 1.5
print((10+10/3)-5*3)
zadanie 1.6
slowo = 'uczę się'
print(slowo)
x = ' '
slowa = 'ucze' , 'sie' , 'programowania'
print(slowa)
# print(slowa.strip())
j=x.join(slowa)
print(j)
zdanie 1.7
cytat = '"Początek jest najważniejszą częścią pracy"'
print(cytat)
zanie 1.8

cytat = '"Początek jest najważniejszą częścią pracy"'
print(cytat.upper())
print(cytat.lower())
print(cytat.split())

zadanie 1.9

cytat = '"Pocz ątek jest najważnie jszą częś cią pracy"'
print(cytat[0:5] + cytat[6:11] +cytat[11:15]+cytat[15:25]+cytat[26:31]+cytat[31:35]+cytat[36:39]+cytat[39:45])

zdanie 1.10
print('Nauka programowania\nwymaga\nwytwwałej pracy')
napis = """Nauka programowania
wymaga
wytrwałej pracy"""
print(napis)

zdanie 1.11
zdanie = 'Warto się uczyć -programowanie jest ciekawe'
print(zdanie[0:15])
print(zdanie[16:45])

zadanie 1.12
a= "10"
b=   "20"
c=  "30"
str = a+b+c
print(str)
int= int(a)+int(b) +int(c)
print(int)

zadanie 1.13

a = 10
b =20
c = 30
int = a +b +c
print(int)
str = str(a)+  ' oraz ' +str(b)+' oraz ' + str(c)
print(str)

zadanie 1.14
n = 'krzysztof'
print(n)

zdanie 1.15
a = 4
b =7
# a,b = b,a
temp = a
a=b
b=temp
print(a,b)

zadanie 1.16
a =1
b =2
print(a+b)


zaanie 1.17
a =1
b=2
b=3
print(a,b)

zadanie 1.18

a=1
b=2
b=b+5
print(b)
del b
print(b)

zadanie 1.19
a ='kot'
b= 4
c= 1.3
print(a,b,c)

zadnie 1.20
modulo = 17%7
modulo=modulo*(modulo+3)
print(modulo*modulo+modulo*3)

zadanie 1.21
w= float(input('Podaj wysokosc'))
d =float(input('Podaj dlugosc'))
pole = w*d/2
print(pole)

zadanie 1.22
pytanie = str(input("jak masz na imie? "))
print(pytanie)

zadanie 1.23
miasto = input('podaj swoje miasto')
panstwo = input('podaj swoje panstwo')
str = miasto + ' ' + panstwo
print(str)

zadani 1.24
cytat = input("Podaj swój ulubiony cytat")
autor = input("Kto jest jego autorem")
a = cytat +'\n\t\t\t' +autor
print(a)

zadanie 1.25
dane = input("Podaj swoje imię i nazwisko")
dlugosc = (len(dane))
print(dlugosc)
zbior = set()
for i in dane:
    # print(i, end=',')

    if i != ' ':
        zbior.add(i)
        print(i, end=',')
print()
print(len(zbior))

lista = [1,2,3,4]
for i in lista:
    print(i,'fajnie')
    print('cos tam')
print('cos innego')

1.26
imie = input('Podj swoje imie')
lista = []
for i in imie:
    lista.append(i)
print(lista)
lista.sort(reverse=True)
print(lista)
ls=sorted(lista)
print(ls)

1.27
imie = input('podaj swoje imie')
nazwisko = input('podaj swoje nazwisko')
wiek = input('podaj swoj wiek')
dane = imie +' '+ nazwisko+' '+ wiek
print(dane)
print(type(dane))
1.28
suma = float(input("podaj sume rachunku"))
napiwek15=round(suma*0.15)
napiwek20=round(suma*0.20)
print("Twój napiwek wynosie " , napiwek15, 'lub ' , napiwek20, ' PLN')

zadanie 1.29
napis = str(input('podaj jaki napis'))
# napis30= print(''+napis*30)
for z in range(30):
    print(napis, end='')
    if z !=29:
      print(',', end ='')
zadanie 1.30
Mój program

a=int(input("podaj liczbę a"))
b=int(input("podaj liczbę b"))
c=int(input("podaj liczbę c"))
suma = a+b+c
print("Suma liczba wynosi:" ,suma)

zadnie 1.31
a =3
b=4
if a==b:
    print("równe liczby")
else:
    print("nie równe liczby")
c =2
d=2

if c!=d:
    print('nie są równe')
else:
    print('są równe')
zadanie 1.32
a = len('Ala ma kota')
b =len('Ola ma kota')
if a == b:
    print("Długości ciągów  są równe")
else:
    print("Długości ciągów nie są równe")

zadanie 1.33
a.
if 3==5 and 1>0 and 4<5:
    print("True")
else:
    print("False")
a =(3==5 and 1>0 and 4<5)
print(a)
# b.
b=(3==3 or 2>4 or 5>7)
print(type(b))
print(b)
zadanie 1.34
if 2<5:
    print('ok')
zadanie 1.35
if 2==2:
    print('ok')
else:
    print('blad')
zadanie 1.36
a=int(input('podaj liczbe a'))
b=int(input('podaj liczbe b'))
c=int(input('podaj liczbe c'))
if a == 15:
    print("liczba równa 15")
elif a >15:
    print("liczba jest wieksza niż 15 ")
elif a < 15:
    print("liczba jest mniejsza niz 15 ")

zadanie 1.37
odp= input('Czy lubisz podrózować Tak,Nie')
odp=odp.upper()
if odp == 'NIE':
    print('Ciekawe, dlaczego nie?')
elif odp == 'TAK':
    c=input('Jak często')
    c=c.upper()
    if c== 'CZESTO':
        print('Dobra robota')
    else:
        print('Podróżuj więcej')
zadanie 1.38
punkty = int(input('ile masz punków z testu'))
if punkty <= 20:
    print("ocena niedostateczna")
elif punkty >= 21 and punkty <= 40:
    print('ocena dopuszczająca')
elif punkty >= 41 and punkty <= 60:
    print('ocena dosteteczna')
elif punkty >= 61 and punkty <= 80:
    print('ocena bardzo dobra')

1.39
ocena= int(input("podaj ocene"))
if ocena == 5:
    print('Dobry uczeń')
elif ocena < 5:
    print('Pracuj dalej')

1.40
liczba =int(input('Podaj liczbę'))
if liczba %2 == 0:
    print('Parzysta')
elif liczba%2 != 0:
    print("Nieparzysta")
else:
    print("Bład")


1.41
month = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec',
         'sierpien','wrzesien','pazdziernik','listopad','grudzien' ]
pytanieP = input("podaj miesiac 1")
pytanieK = input("podaj miesiac 2")
P=month.index(pytanieP)+1
K=month.index(pytanieK)+1
print(P,K)
czas = K-P
if czas <= 0:
    czas=czas+12
print(czas)

1.42
lista = ['zero', 'jeden','dwa','trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem','dziewiec']
liczba = input('podaj liczbe')
for i in liczba:
    # print(int(i), end=',')
    if i != '-':
        index =int(i)
        print(lista[index], end= ', ')
    else:
        print('minus', end=' ,')
        # break


1.43
lista = []
for i in range(5):
    pytanie = input( 'podaj slowo')
    lista.append(pytanie)
print(lista)
z = ''
for i in lista:
    if len(i) > len(z):
        z = i
print(z)

print(max(lista, key=len))


1.44
wiek = int(input('podaj wiek'))
if wiek <=18:
    print('dzieco')
elif wiek >=18 and wiek < 44:
    print('mlody')
elif wiek >=45:
    print('ok')
1.45

wiek = int(input('podaj wiek'))
plec = str(input('podaj plec'))
plec=plec.upper()

if wiek <=18:
    print('dzieco')
elif wiek > 18 and wiek <60 and plec =='K':
    print('pracujesz')
elif wiek > 18 and wiek <65 and plec =='M':
    print('pracujesz')
else:
    print('emeryt')

1.47
lista = [4,5,6,7]
while lista:
    del  lista[0]
    print(lista)
1.46


while True:
    liczba = int(input('podaj liczbe'))
    if liczba  >=0:
        print('liczba jest dodatnia')
        break

1.60
a= 'a'
b = 'ananas'
pos =0
# c=b.find(a,0)
while True:

    c = b.find(a, pos)
    if c != -1:
        pos = c+1
        print(c)
    else:
        c= -1
        print('koniec')
        break

zadanie  1.49

i =1
temp = list()
for i in range(1000):
    i=i+(i+1)
    temp=i
print(temp)

suma=sum(i for i in range(1001))
print(suma)


 1. 50
for i in range(100):
    i=i+1
    print(i, end=', ')
print('\n')
for i in reversed(range(100)):
    i=i+1
    print(i, end=', ')
print('\n')
for i in range(2,52):
     if i%2==0:
         print(i, end=', ')
print('\n')

for i in range(1,101):
     if i%5==0 or i % 3 == 0:
         print(i, end=', ')





for i in range(1,100):
     if i%3==0:
         print(i, end=', ')


zadanie 1.52
punkty = 30
# a1= sila
# a2 = zdrowie
# a3=madrosc
# a4=zrecznosc
skill = {'siła':0, 'zdrowie':0, 'mądrość':0, 'zręczność':0}
# rozdanie = str(input('Rozdziel punty na atrybuty: siła, zdrowie, madrość, zręczność. Na co chcesz rozdać punkty?'))
while punkty:
    rozdanie = str(input('Rozdziel punty na atrybuty: siła, zdrowie, madrość, zręczność. Na co chcesz rozdać punkty?'))
    if rozdanie == 'siła':
        s=print(int(input("ile punktów  chcesz rozdać")))
        punkty=punkty-s




    1.62
txt = str(3568789)
lista = list(txt)
print('Przed',lista)
for i in range(len(lista)):
        if i % 3 == 0 and i != 0:
           lista.insert(len(txt)-1-i+1,'.')

print(lista)
str =''.join(lista)
print(str)

1.53
lista =[]
for i in  range (-20,45,5):
    lista.append(i)
print(lista)

listaF=[]
for i in lista:
    f = i*1.8+32
    listaF.append(f)
print(listaF)


zadanie 1.49

wartosc = 1.2e3+35.5
# wartosc20= 20*(str(wartosc)+';   ')
# print(wartosc20)`

for i in range(20):
    print(str(wartosc), end=';  ')

zadanie 1.75

a =5
try:
    w=a/0
    print(w)
except:
    print("Przypadek obsłużony")

def avg(lista):
    avg = len(lista)
    return avg

l= [1,4,5,6,7]
print(avg(l))
