#Collection types
#namedtuple()
from collections import namedtuple
a=namedtuple('course','name, technology')
b=a('data science','python')
print(b)
c=a._make(['AI','python']) #passing a list
print(c)
#deque()
from collections import deque
st='edureka'
l=list(st)
# print(l.count('e')) list also have count bultin function
d=deque(l)
print(d)
d.append('h') # appending element at last
print(d)
d.appendleft('h') #appending element at frist
print(d)
d.pop()  #poping element at last
print(d)
d.popleft()# poping element at frist
print(d)
#ChainMap is used to add two dictionaries
e={1:'python',2:'ML'}
f={3:'DS',4:'AI',5:'DL',6:'DL'}
from collections import ChainMap
g=ChainMap(e,f)
print(g[1])
#Counter for counting lable objects
h=[1,1,2,2,3,3,4,5,6,4,5,7,8,9,0,4,5,0]
str='edureka'
from collections import Counter
i=Counter(h)
j=Counter(str)
print(i)
print(j['e'])
print(list(i.elements()))
print(list(j.elements())) #print counter elements
print(i.most_common()) # print element and count as side by side
sub={4:1,0:1,9:1}
print(i.subtract(sub)) # Decreasing count for element
print(i.most_common())
print(list(i.elements()))
#OrdredDict
from collections import OrderedDict
k=OrderedDict()
k[1]='e'
k[2]='d'
k[3]='u'
k[4]='r'
k[5]='e'
k[6]='k'
k[7]='a'
print(k)
print(k.keys())
print(k.get(3))
k[1]='p'
print(k)
#defualtdict It has Default value 0 for intiger values
from collections import defaultdict
l=defaultdict(int)
l[1]='p'
l[2]='y'
print(l[3])
#UserDict,UserList,UserString



