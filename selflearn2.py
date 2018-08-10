"""
#Trial 1 some operators
a =20; c=2
b=6
c **=b
print(a/b) #除
print(a//b) #整除
print(a**b) #乘幂
print(a%b) #除余
print(c) #c=c**b
"""

#####################################

"""
#Trial 2 binary operations
a=0b1101 #13
b=0b0110 #6
print(a) #十进制形式
print(bin(a)) #二进制形式
print(type(bin(a))) #bin() is a string
print(bin(a&b)) #and
print(bin(a|b)) #or
print(bin(a^b)) #xor true if only one side is true
print(bin(~a))  #not
print(~a) #-a-1
"""

#####################################

"""
#trial 2 logical operators
a = 10
b = 20
 
if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")
 
if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")

a = 0
if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")
"""

#####################################

"""
#trial 3 member operator成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
"""

#####################################


#trial 3 identity operator 身份运算符 is / is not 
#if (x is y ) 等同于 if(id(x)==id(y))

a = 20
b = 20
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 #1 - a 和 b 有相同的标识
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 #2 - a 和 b 有相同的标识

# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 #3 - a 和 b 没有相同的标识
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")
 #4 - a 和 b 没有相同的标识