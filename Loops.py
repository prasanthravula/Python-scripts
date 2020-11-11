#While
# count=0
# while count<9:
#     print(count)
#     count+=1
# print('good bye')
# import random
# n=20
# to_be_guessed=int(n * random.random())+1
# guess=0
# while guess!=to_be_guessed:
#
#      guess=int(input("Enter New Number:"))
#      if(guess>0):
#          if(guess>to_be_guessed):
#              print("Number is too large")
#          elif guess<to_be_guessed:
#              print("Number too small")
#          else:
#              print("congratulations you made it")
#              break
#      else:
#          print("sorry that you are giving up!")

#for Loop
# fruits=['mango','apple','grape','Gova']
# for i in fruits:
#     print(i)
# print('good bye')
inpu=int(input('enter number'))
fact=1
if inpu<0:
    print('must be positive')
elif inpu==0:
    print("factorial is 1")
else:
    for i in range(1,inpu+1):
        fact*=i
print(fact)
#Nested Loops
#pattrens

