#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代


# for循环迭代字符串
for char in 'hello world':
	print(char, end = ' ')
print('\n')

# for循环迭代list
nums = [1, 2, 3, 4]
for num in nums:
	print(num, end = ' ')
print('\n')

# 迭代dictionary
dic = {'name':'hong', 'age':29}
for key in dic:
	print('{0}:{1}'.format(key,dic[key]), end=' ')
print('\n')

for value in dic.values():
	print(value, end = ' ')
print('\n')


# 其他
for x,y in [(1,'a'), (2,'b')]:
	print(x,y)

print('\n------------------------')

# 迭代器

# 字符迭代器
str1 = 'hello'
iter1 = iter(str1)

# list迭代器
list1 = ['a','aa','aaa']
iter2 = iter(list1)

# tuple迭代器
tuple1 = ('father','mother','son','daughter')
iter3 = iter(tuple1)

# 遍历迭代器
for x in iter1:
	print(x, end=' ')
print('\n')

while True:
	try:
		print(next(iter3))
	except StopIteration:
		break








