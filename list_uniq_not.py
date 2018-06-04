
# Example 0
from collections import  Counter

w = "Ala ma kota, i kot ma ale. Ala ma psa także"
w = w.replace(',', '')
w = w.replace('.', '')
li = w.lower().split()

c = Counter(li)
print('Frazy które występują najczęciej  nazwa/ilość:' )
for i, count in c.most_common(2):
    print(i,':', count)



# Example 1
w="Ala ma kota, i kot ma ale"
w = w.replace(',', '')
w = w.replace('.', '')
s=w.lower().split()
w = len(s)
# print(w)
for i in s:
    if s.count(i) > 1:
        print('Wyraz', i, 'występuje więcej niż 1 raz?:', 'true')
    else:
        print('Wyraz', i, 'występuje więcej niż 1 raz?:', 'false')


# Example  2
w="Ala ma kota, i kot ma ale"
w = w.replace(',', '')
w = w.replace('.', '')
s=w.lower().split()
w = len(s)
u=[]
# print(w)
for i in s:
    if i in s and s.count(i) >1:
        u.append(i),print(True)
        
        
#  Example 3
w="Ala ma kota, i kot ma ale ma, kot kot kot"
w = w.replace(',', '')
w = w.replace('.', '')
s=w.lower().split()
w = len(s)
# print(w)
for i in s:
    if s.count(i) > 1:
        i, s.count(i)
print('Frazy które występują najczęciej  nazwa/ilość:', i, s.count(i))

        
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

        
#  Example 5       
    
from collections import  Counter

w="Ala ma kota, i kot ma ale. Ala ma psa także"
w=w.replace(',','')
w=w.replace('.', '')
li=w.lower().split()

c=Counter(li).most_common(2)
for i in c:
    p='W podanym zdaniu występuje fraza/razy', i
    print(p)
    

