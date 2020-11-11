#Arthimatic operators
x,y=10,20
print(x+y)
print(x/y)
print(y-x)
#Assignment operators
a=10
a**=a
a+=a
a*=a
print(a)
#comparision operators
print(x==a)
print(x!=a)
print(x>9)
print(x<=a)
#conditional Operators
x,y=3,4
if(x==y):
        print('equal')
elif x>y:
    print("x is largest one")
else:
    print('y is largest one')
print(x>y and x!=0)
print(x<y and y!=0)
print(not(x>0 or y>5))
#Identity Operator
list1=[10,20,30]
list2=[10,20,30]
x=list1
print(x is list1)
print(list1 is not list2)
# Membership operators in python
print(10 in list1)
print(40 in list1)
#BITWISE OPERATORS
print(10 & 12)
print(10 | 12)
print(10>>2)
print(10<<2)
print(bin(10))
print(bin(40))
print(10^11)
print(bin(11))
print(~10) # invert all the bits
print(bin(-11))


