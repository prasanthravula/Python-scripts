#map() for user define fun()
#Exp1 for map()
def fun(x):
    return x*x
x=map(fun,[1,2,3,4])
print(x)
print(list(x))
#Exp2 for map()
def fun2(x,y):
    return x*y
z=map(fun2,[1,2,3,4],[5,6,7,8])
print(tuple(z))
#EXP3 using lambda for map
x=[1,2,3,4,5,6,7]
a=list(map(lambda k:k+3,x))
print(a)
#Exp1 for filter()
b=[1,2,3,4,5,6,7]
c=tuple(filter(lambda x:x>=3,b))
print(c)
#exp2 for filter()
def fun1(x):
    return x>=3
d=tuple(filter(fun1,[1,2,3,4,5,6]))
print(d)
#exp1 for reduce()
from functools import reduce
def fun2(x,y):
    return x+y
e=reduce(fun2,[1,2,3,4])
print(e)
#exp2 for reduce()
from functools import reduce
li=[23,45,6,7]
f=reduce(lambda x,y:x+y,li)
print(f)
#example filter() within the map() Nd wise versa
g=list(map(lambda x:x+x,filter(lambda x:x>=3,[1,2,3,4,5])))
print(g)
#example reduce() with in the map() and filter()
from functools import reduce
h=reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda x:x>=3,[1,2,3,4,5])))
print(h)