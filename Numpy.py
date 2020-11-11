#Numpy
#One dim
import numpy as np
a=np.array([1,2,3])
print(a)
#two Dim
b=np.array([(1,2,3),(4,5,6)])
print(b)
#numpy vs list memory
import numpy as np
import sys
l=range(1000)
print(sys.getsizeof(5)*len(l))
n=np.arange(1000)
print(n.size*n.itemsize)
#numpy vs list time
import numpy as np
import time
import sys
size=1000000
L1=range(size)
L2=range(size)

A1=np.arange(size)
A2=np.arange(size)
start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
start1=time.time()
result1=A1+A2 #convienent
print((time.time()-start1)*1000)
#
import numpy as np
b=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(b.ndim) # Dimension
print(b.dtype)# data type
print(b.itemsize)# data size
print(b.size)
print(b.shape)
#print(b.reshape(4,2))
#slicing
print(b[0,2])
print(b[0:,2])
print(b[0:,:2])
print(b[1:,:-1])
#linspace()
c=np.linspace(1,10,20)
print(c)
print(np.max(c))
print(c.sum())
#axis
d=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(d.sum(axis=0)) #result in sum colum wise
#Squareroot and standard devation
e=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(np.sqrt(e))
print(np.std(e))
# add,mul,div,sub
f=np.linspace(10,20,10)
g=np.linspace(21,30,10)
print(f+g)
print(g-f)
print(g/f)
#Concatinate two arrays
import numpy as np
h=np.array([(1,2,3),(4,5,6)])
i=np.array(([(7,8,9),(10,11,12)]))
print(np.vstack((h,i)))
print(np.hstack((h,i)))
print(h.ravel()) #to all in single column
#Numpy y Special functions
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x) #np.cos(x) or np.tan(x)
plt.plot(x,y)
plt.show()
#e^x
ar=np.array([1,2,3])
print(np.exp(ar))
#Log
print(np.log(ar))
print(np.log10(ar))



