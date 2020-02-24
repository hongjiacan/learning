#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# if

result = 59
if result >= 60:
	print('及格')
else :
	print('不及格')


num = 6
if num:
	print('default boolean')

cond = ''
if cond:
	print('is not enpty')

cond = None
if cond:
	print('is not None')


score = 89
if score >= 90:
	print('优')
elif score >= 80:
	print('良')
elif score >= 60:
	print('及格')
else:
	print('不及格')


# 循环

for i in [1,2,3]:
	print(i)

for i in ('name','age'):
	print(i)

for i in set([1,2,3,4]):
	print(i)

for i in {'a':1, 'b':222}:
	print(i)

# range函数
# 
for i in range(3):
	print(i)
for i in range(1,9):
	print(i)
for i in range(0,5,2):
	print(i)


# while

cnt = 1
sum1 = 0
while cnt <= 100:
	sum1 = sum1 + cnt
	cnt = cnt + 1
print(sum1)










