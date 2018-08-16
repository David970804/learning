#Strings
a=1
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!') #字符截取，字符串连接
print(a,var1,var1+str(a)) #逗号分隔
print(var1*2) #字符串重复输出
print ("我叫 %s 今年 %04d 岁!" % ('小明', 10)) #字符串格式化 0n表示用用0填充成n位数
#我叫 小明 今年 0010 岁!
print ("我叫 %s 今年 %.3f 岁!" % ('小明', 10))
