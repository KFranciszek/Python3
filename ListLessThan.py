#Taks from  http://www.practicepython.org##
#My solution#
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i >= 5:
        b.append(i)
print (b)


#######
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
ask = int(input('Give a muber'))


for i in a:
    if i > int(ask):
        b.append(i)
print(b)
