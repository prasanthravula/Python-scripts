#Generators
def fun1(dict):
     for x,y in dict.items():
         yield x,y #similar to return statment
a={1:'welcome',2:'to',3:'python'}
b=fun1(a)
print(next(b)) # for output return value by value
print(next(b))
print(next(b))
#exp2 for generators
def fun2(x):
    while x<=4:
        yield x
        x=x+1
c=fun2(0)
print(next(c))
#exp3 for generators
def fun3():
    n=3
    yield n
    yield n*n
k=fun3()
print(next(k))
#exp3 using for loop
def fun4():
    n=3
    yield n
    yield n*n
l=fun4()
for i in l:
    print(i)
#Generator expressions
m=range(6)
print('list comp',end=":")
q=[x+2 for x in m]
print(q)
r=(x+2 for x in m)
print(r)
for i in r:
    print(i)
#Exp
s=[x+2 for x in m]
print(s)
print(min(s))
#Use Cases for generators
def fun5():
    f,s=0,1
    while True:
       yield f
       f,s=s,f+s
for x in fun5():
    if x>50:
        break
    print(x,end=" ")
#Number series
a=range(10)
t=[x for x in a ]
for i in t:
    print(i,end=" ")
# Exp SINE wave
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip=2):
    x=np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * 0.5)*(7-i) * flip)
sb.set()
s()
plt.show()
# Generate sine wave using generator
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip=2):
    x=np.linspace(0, 14, 100)
    for i in range(1, 10):
        yield(plt.plot(x, np.sin(x + i * 0.5)*(7-i) * flip))
sb.set()
s=s()
plt.show()





