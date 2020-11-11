from scipy import *
print(help(cluster))
import scipy
scipy.info(cluster)
scipy.source(cluster)
#special functions in scipy
#exponential functions
from scipy import special
a=special.exp10(3)
print(a)
b=special.exp2(2)
print(b)
#trigonametry
c=special.sindg(90)
print(c)
d=special.cosdg(90)
print(d)
#Integraion function
#general integration
from scipy import integrate
e=scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(e)
#Double itegration
f=lambda x,y:x*y**2
g=lambda x:1
h=lambda x:-1
integrate.dblquad(f,0,2,g,h)
#fourier Transformations
from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=fft(x)
z=ifft(x)
print(y)
print(z)
#Linear algebra problems
#inverse of matrix
from scipy import linalg
a=np.array([[1,2],[3,4]])
b=linalg.inv(a)
print(b)
#interpulation functions





