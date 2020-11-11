#import array #a=array.array('i',[1,2,3,4])
#from  array import * #a=array('i',[1,2,3,4])
#Arrays are mutable and have same type of data
import array as arr
a=arr.array('i',[1,2,3,4,5])
#Acessing Elements
print(a)
print(a[1])
print(a[-4])
#Adding elements
print(len(a))# print the length of array
a.append(6) # adding one element to array
print(a)
a.extend([7,8,9])# adding more than one element to array
print(a)
a.insert(0,10)# insert element at particular position
print(a)
#Removing Elements
print(a.pop()) # remove and return element
print(a)
print(a.pop(8)) # remove and return element at particular index
print(a)
print(a.pop(-1)) # remove and return element at particular index
print(a)
a.append(10)
print(a)
print(a.remove(10)) # remove particular element at frist occurance
print(a)
#Concatination of elements
b=arr.array('i',[5,6,7,8,92,3,4,1])
c=arr.array('i',[1,2,3,4,5])
d=a+b
print("conat:",d)#print(type(d)) array type:array.array
#slicing elements
print(d[0:5]) #print frist four elements
print(d[0:-1]) #pritn all elements except last one
print(d[0:-2]) #pritn all elements except last two
print(d[::-1]) # prints the reverse form of array but original one remains same and exhuast the memory
print(d)
#Looping through array
#for loop
for i in d:
    print(i)
for i in d[0:2]:
    print(i)
for i in d[0:-10]:
    print(i)
#While loop
temp=0
while temp<len(d):
    print(d[temp])
    temp+=1
#HashMaps,HashTabels
#example Dictionaries also type of hashtables
my_dict={1:'py',2:'Ai',3:'Dl'}
print(type(my_dict))
new_dict=dict()
print(new_dict)
print(type(new_dict))
new_dict=dict(dave='001',sai='002')
print(new_dict)
# Example nested Dectionaries
emp_details={'Employee':{'Dave':{'Id':'007','salary':'2000','Age':'19'},
                        'subba':{'Id':'008','salary':'23000','Age':'29'}}}
print(emp_details)
#Accessing values in dictionaries or hashtables
print(my_dict[1])
print(my_dict.keys())
print(my_dict.values())
print(new_dict.get('dave'))
for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
for x in my_dict.items():
    print(x)
#Updating values in Dictionaries
my_dict[2]='ML'
my_dict[4]='AI'
print(my_dict)
#Deleating Dictionaries
my_dict.pop(3)
my_dict.popitem()
del my_dict[2]
print(my_dict)
# Dict to Data Frames(df)
import pandas as pd
df=pd.DataFrame(emp_details['Employee'])
print(df)





