#http://www.practicepython.org
#My solution

ask = int(input('Give a number'))
x= range(0,100)
y =[]

for i in x:
    if i % ask == 0:
        y.append(i)
print(y)
