#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表生成式
# [expr for iter_var in iterable] 
# [expr for iter_var in iterable if cond_expr]
# 

# 一行代码打印九九乘法表
print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))



lsit1=[x * x for x in range(1, 11)]
lsit2=[x * x for x in range(1, 11) if x>5]
print(lsit1)
print(lsit2)

lsit3= [(x,y) for x in range(3) for y in range(3)] 
print(lsit3)

print('\n------------------------')

# 生成器
# 生成式的中括号改成括号
# (expr for iter_var in iterable)
# (expr for iter_var in iterable if cond_expr)

gen= (x * x for x in range(10))
print(gen)

for num  in  gen :
    print(num)

print('\n------------------------')

# 函数的形式实现生成器
# 在每次调用 next() 的时候执行，遇到 yield语句返回，
# 再次执行时从上次返回的 yield 语句处继续执行
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )

print('\n------------------------')

# 打印斐波那契数列
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(10):
    print(x , end = ' ')

print('\n------------------------')

# 递归打印斐波那契数列
def fibon2(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibon2(n-1) + fibon2(n-2)

for x in range(10):
	print(fibon2(x),end=' ')
print('\n------------------------')


# 打印杨辉三角

def tri(n):
    for i in range(n+1):
        yield a
        a, b = b, a + b



for x in tri(1):
    print(x , end = ' ')

print('\n------------------------')




