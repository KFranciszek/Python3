magazyn = ['miecz', 'zbroja', 'topór', 'tarcza']
print(magazyn)
for i in magazyn:
    print(i, end =" ,")
print(len(magazyn))
if len(magazyn) < 5:
    print("Brakuje Ci konia")
    p=input("Co dodać")
    magazyn.append(p)
    print("Posiadasz teraz", magazyn)
    if len(magazyn) >= 5:
        print("Jesteś gotów na wojnę")
plecak = ['zioła','mikstury']
magazyn += plecak
print(magazyn)
del magazyn [1]
print(magazyn)
print(magazyn.index('tarcza'))
print(magazyn.count('miecz'))


###############################################
list1 = ['Kasia', 'Jadzia', 'Król']
print(list1)
print(list1[0])
list1.append("Kinga")
print(list1[0])
list1[0] = 'Ewelina'
print(list1)
list1.remove("Król")
print(list1)
################################################
lista =[1,2,"mama", "kot"]
lista.append('działo')
print(lista)
lista.remove(1)
print(lista)
print(lista[3:4])
lista.insert(6,"Kinga")
print(lista)
print(len(lista))
del lista[0:3]
print(lista)
lista[0:2]=['Ja', "Jagoda"]
print(lista)
print(len(lista))
########
tupla = ("Mama", "kot")
print(tupla)
print(len(tupla))
lista.append(tupla)
print(lista)
