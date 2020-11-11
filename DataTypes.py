l=[1,2,3,4,5,6,8,2,3,4,5,9,10,11]
z=set(l)
print(z)
#VARIABLES
x=10
y=20
print(x*y) #Multiply
print(y-x) #Sub
p="hi"
q=" hello"
print(p+q)
#Input
''' In=input() '''
#DATA TYPES
#Number
a=1 #Integer
print(type(a))
b=10.623 #Float
print(type(b))
c=26j #Complex
print(type(c))
#BOOLEAN
num=x>y
print(num)
print(type(num))
#STRING
name="hello worLd"
print('Length:',len(name)) #length Of String
#name[2]='d' #String is immutable
print(name)
print(name[0:7]) # print "hello w"
print(name[-2])# print 2nd word from last in string
print(name[9])# print 9th word from frist in string
print(name.upper()) # print upper case letters
print(name.lower()) # print lower case letters
#LIST is a collection of array which is changable and orderd
list=[1,2,3,'hi','hello',10.2]
list.extend([6,7,8])
print(list[2:6]) # print from 2nd position to last position
list.append(26j)#New element added to the list
print(list)
list.insert(3,'true')#3rd position element is replaced by true
print(list)
print(list.count(1))
list.reverse()#reverse the elements of the list
print(list)
#DICTIONARY
#They are unordered,changable and no duplicates
course={1:'python',2:'data science','thrid':'machine learning'}
print(course[1]) #prints frist element in the dictionary
print(course['thrid'])#reading 3rd element using string
course['thrid']='hadoop'#replacing an element
print(course)
course['four']='machine learning'#adding an element
print(course)
del course['four']
print(course)
#TUPLES
#They are ordred and unchangable and duplicates are present
animals=(10,20,30,20,'Tiger','Zebra','lion','Tiger')
print(animals)
print(animals[2])# print 3rd Element
print(animals.count('Tiger'))#prints the count of Tiger
print(animals.count(20))#print the count of 20
#SET
#It is unordered,no duplicates and not support indexing
set={10,20,30,40,30,'python','edureka','courses'}
print(set)#prints with out duplicate values
###############################################
a=[1,2,3,4,4]
b={4,5,6,7,3,2,4,5}
c=[a,b] #
print(c[0])
print(c[1])
d=(a,b)
print('tuple:',d[0][1]) #tuple support indexting but immuatable
#print('tuple:',d[1][1]) set not support idexing
############################################
#TYPE CONVERSION
# 1.int() 2.float() 3.str() 4.list() 5.tuple() 6.set() 7.dict()
a=10
b='string'
c=10.2
k=[1,2,3,4,5,6,7,8,3,4,2]#List
e=(1,2,3,4,5,6,3,5,6)#Tuple
f={2,3,4,5,6,7,3,4,5,8,9,0}#Set
g={1:"hi",2:'hello','three':'3','four':'4'}#Dictionary
print(a+int(c))#print Integer int()
print(str(a)+b) #print String str()
print(float(a)+c)#print float float()
print('tuple:',tuple(k)) # print list to tuple using tuple()
print(tuple(f))
str="hello santy"
print(list(str))


