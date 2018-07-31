"""
trial 1
multiple = "1 + "+\
		   "2 = "+\
		   "3"	
print(multiple)		  
"""
###########################################################
"""
trial 2 
a,b,c=1,"2",'this is a testing string'
print(a,b,c)
"""
###########################################################

#print(string[-1:])
"""
trial 3
a = 11.21
print(isinstance(a,float))
del a
#print(a)  #error message: a is not defined
#print(21/4) # / return a float number
#print(21//4) # // return a integer
#print(r"testing\n") #print out \n
#new concept: tuples
tuples=('123','kar98',123)
print(tuples) #elements in a tuple cannot be replaced
a="abcde"
a[1]='h' #string is like tuple, its characters cannot be replaced as well
print(a)
"""

###########################################################

"""
trial 4
tup=(20,) #a comma is needed when defining a one element tuple
#print(tup)
#new concept: set {} (different from Dictionary)

st={'abcde'}  #'abcde'
st=set('abcde') #{'d', 'e', 'c', 'a', 'b'}
print(st) #自动去掉set中重复的元素

a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个 empty Dictionary。
"""
###########################################################

"""
#trial 5 Dictionary
#1st intro
dic={}
dic["one"]=1
dic[2]=2
print(dic) #{'one': 1, 2: 2}
#2nd keys and values
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys()) #dict_keys(['name', 'code', 'site'])
print(tinydict.values()) #dict_values(['runoob', 1, 'www.runoob.com'])
tinydict.clear()
print(tinydict)  #clear the dictionary

#3rd constructing a dictionary
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])) #{'Runoob': 1, 'Google': 2, 'Taobao': 3}
#dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组
print({x: x**2 for x in (2, 4, 6)}) #{2: 4, 4: 16, 6: 36}
print(dict(Runoob=1, Google=2, Taobao=3)) #{'Runoob': 1, 'Google': 2, 'Taobao': 3}
"""

#trial 6
a= """i am a multi
-line sentence"""
print(a)