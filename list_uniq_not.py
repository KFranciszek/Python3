# Example 1
w="Ala ma kota, i kot ma ale"
s=w.split()
w = len(s)
# print(w)
for i in s:
    if s.count(i) > 1:
        print(i,'true')
    else:
        print(i,'False')



# Example  2
w="Ala ma kota, i kot ma ale"
s=w.split()
w = len(s)
u=[]
# print(w)
for i in s:
    if i in s and s.count(i) >1:
        u.append(i)
print(True)


# Example 3
w="Ala ma kota, i kot ma ale"
s=w.split()
w = len(s)
# print(w)
for i in s:
    if s.count(i) > 1:
        print('Słowo uniklane to:', i,'występuje aż', s.count(i), 'razy')
        break

        
#  Example 4
w="Ala ma kota, i kot ma ale. Ala ma psa także"
w=w.replace('.', '')
w=w.replace(',', '')
print(w)
s=w.lower().split()
print(s)
w = len(s)
for i in s:
    if s.count(i) > 1:
       e= 'Słowo uniklane to:', i,'występuje aż', s.count(i), 'razy'
       print(e)
