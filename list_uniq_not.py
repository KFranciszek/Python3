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
