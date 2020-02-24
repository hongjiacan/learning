#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数
# 求和
def sum(a, b):
	return a+b

print(sum(1,2))


# 求商与余数
def division ( num1, num2):
	a = num1 % num2
	b = (num1-a) / num2
	return b , a

num1 , num2 = division(9,4)
tuple1 = division(9,4)

print (num1,num2)
print (tuple1)


# 参数列表
# 
# 默认参数
# 默认参数必须放参数列表最后
def param_default(name, age = 18, sex = 'male'):
	return name, age, sex

print(param_default('Kate', 10,'female'))
print(param_default('Tom'))


# 不定长参数

def param_unknow(name, age, * extras):
	print(' name:{0},'.format(name), end='')
	print(' age:{0},'.format(age), end='')
	print(' extra info:{0}'.format(extras))
	return;

param_unknow('Kate', 10, 'female', '165cm', '50kg')


# 强制关键字参数

def param_key(*,name, age):
	print(' name:{0}, age:{1}'.format(name,age))
	return;

param_key(age = 10, name = 'Kate')


# 匿名函数 lambda
# 代码块

lamSum = lambda a,b : a+b;
print(lamSum(1,2))



# 
num2 = 100
sum1 = lambda num1 : num1 + num2 ;

num2 = 10000 
sum2 = lambda num1 : num1 + num2 ;

# lambda表达式中的参数num2是自由变量
# 在运行时绑定值，而不是定义时就绑定
# 所以取 10000 而不是 100

print( sum1( 1 ) )
print( sum2( 1 ) )
