#
def fun1(name):
    return f"Hello {name}"
def fun2(name):
    return f"{name} ,How you doing"
def fun3(fun4):
    return fun4("Dear Learner")
print(fun3(fun1))
print(fun3(fun2))
#Inner Function
def fun():
    print('frist function')
    def fun1():
        print("frist child function")
    def fun2():
        print("child fun2")
    fun1()
    fun2()
fun()
#Decorators adding new functonality for present one
def fun1(fun):
    def wrapper():
        print("hello")
        fun()
        print("welcome to python edureka tutorial")
    return wrapper
def fun2():
    print('pythonista')
expfun=fun1(fun2)
expfun()
#Alternative for above one
def fun1(fun):
    def wrapper():
        print("hello")
        fun()
        print("welcome to python edureka tutorial")
    return wrapper
@fun1 # Syntactic sugar Syntax
def fun2():
    print('pythonista')
fun2()
#Decoraters with arguments

#Fancy Decoraters in Python
#class decoraters


