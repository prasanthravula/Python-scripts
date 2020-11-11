#class Exp
class car:
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def price_inc(self):
        self.price=int(self.price*1.15)
honda=car('city',2016,1000000) #Objects with data members
swift=car('desire',2017,2000000)
print(honda.price)
honda.cc=1500 #Object with instance varibale
print(honda.__dict__)
honda.price_inc()
print(honda.__dict__)
print(swift.__dict__)
swift.price_inc()
print(swift.__dict__)
#Iheritance exp
class supercar(car):
    pass
Rangerover=supercar('Rangerover',2020,20000000)
print(Rangerover.__dict__)
#print(help(Rangerover))
Rangerover.price_inc()
print(Rangerover.__dict__)
#Exp3
# class ep3(car):
#     def __init__(self,model,year,price,cc):
#         super.__init__(model,year,price)
#         self.cc=cc
# lamborgani=ep3('lamborgani',2021,30000000,2000)
# print(lamborgani.__dict__)
#Inheritance using __init__(self)
#Single Inheritance
class  parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def view(self):
        print(self.name," ",self.age)

class child(parent):
    def __init__(self,fname,fage):
        parent.__init__(self,fname,fage)
        self.lastname="edureka"
    def view(self):
        print(self.name," ",self.lastname," ",self.age)

obj1=child('sai',20)
obj1.view()
#Types of Inheritance
#single
class parent:
    def func1(self):
        print("this is parent function")
class child(parent):
    def fun2(self):
        print("this is child function")
obj1=child()
obj1.fun2()
#Multiple
class parent1:
    def func1(self):
        print("this is parent1 function")
class parent2:
    def fun1(self):
        print("parent2 function")

class child(parent1,parent2):
    def fun2(self):
        print("this is child function")
obj1=child()
obj1.fun1()
#Multilevel
class parent3:
    def func1(self):
        print("this is parent function")
class child1(parent3):
    def fun2(self):
        print("this is child1 function")
class child2(child1):
    def fun3(self):
        print("child 2 function")
obj1=child2()
obj1.fun2()
#Hirarchciy
class parent4:
    def func1(self):
        print("this is parent function")
class child1(parent4):
    def fun2(self):
        print("this is child1 function")
class child2(parent4):
    def fun3(self):
        print("child 2 function")
obj1=child1()
obj2=child2()
obj1.fun2()
obj2.fun3()
#Hybride
#combine two inheritances
#Using super key word
class parent:
    def func1(self):
        print("this is parent function")
class child(parent):
    def fun2(self):
        super().func1()
        print("this is child function")
obj1=child()
obj1.fun2()
#method Overriding
class parent:
    def func1(self):
        print("this is parent function")
class child(parent):
    def func1(self):
        print("this is child function")
obj1=child()
obj1.func1()
#abstract class

