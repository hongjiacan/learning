#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 元组
# 初始化后就不能修改
# tuple 的每个元素，指向永远不变
# 但指向的元素可变
# 更安全

sex = ('male', 'female')
week = ('Monday', 'Tuesday', 'Wensday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(sex)
print(week)

tuple1 = ()
tuple2 = ('single',) # 单元素的元组必须带个逗号
str1 = ('single') # 不是元组
print(tuple1)
print(tuple2)
print(str1)

# 访问
print(sex[0])

# 修改
# 通过修改可变元组元素
str1 = 'aaa'
list1=[123, 456]
tuple3=(str1,list1)

print(tuple3)

str1 = 'bbb'
list1[0]=789
list1[1]=100
print(tuple3)


# 操作
print(len(sex))
print(max(week))
print(sex+week)







