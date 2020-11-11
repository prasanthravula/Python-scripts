#Lambda arguments:Expression
x=lambda a:a*a
print(x(4))
#Anonymous functions with user define functions
def fun1(x):
    return lambda y: x + y
t=fun1(4)
print(t)
print(t(8))
u=fun1(7)
print(u(6))
#Lambda within filter()
list1=[1,2,3,4,5,6,7]
list2=list(filter(lambda a:(a%2==0),list1))#SYNTAX filter(function,iterables)
print(list2)
#Lambda with in map()
list3=[3,4,5,6,7,8,2,3,4]
list4=list(map(lambda a:(a/3!=2),list3))#SYNTAX map(function,iterables)
print(list4)
#Lamda with in reduce(function,sequence)
from functools import reduce #import functools or from functools import *
print(reduce(lambda a,b:a+b,[23,24,45,47,91,-1]))
#Lambda for Algebra
# for linear equations 3x+4y
exp=lambda x,y:3*x+4*y
print(exp(2,3))
# for quadratic equations
#(a+b)^2
exp1=lambda a,b:(a+b)**2
print(exp1(1,2))



