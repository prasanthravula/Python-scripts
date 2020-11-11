#coustem Modules
import Mod1 as md
add=md.add(10,15)
sub=md.sub(15,10)
mul=md.mul(10,15)
print(add)
print(sub)
print(mul)
from Mod1 import *
mul=mul(10,15)
print(mul)
#help('modules') #Gives list of bultin modules
#Bultin Modules
#Time Modules
import time
print(time.time()) #returns sec
print(time.ctime(1603453850.936645)) #returns Time
print(time.localtime())# return whole time parameters
t=time.localtime()
print(time.mktime(t))
x=time.strftime("%m/%d/%y")
#date Time module
import datetime as dt
print(dt.datetime(2020,4,5,6,7,30,54))  #convert to date and time
v=dt.datetime.now()#to get current date and time now
print(v)
print(v.year)#to get year
print(v.month)#to get month
u=dt.date(2020,5,7) #to convert to date
print(u)
w=dt.time(3,45,23)
print(w) #To convert time
#Ttimedelta for to calculate time diff
a=dt.timedelta(days=30)
b=dt.timedelta(days=40)
c=a-b
print(c)

