#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 反向迭代

list1 = list(range(10))
print(list1)

list2 = list(reversed(list1))
print(list2)


# 同时迭代 zip
# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b
# 迭代长度跟参数中最短序列长度一致
names = ['Kate', 'Tom', 'Jim']
ages = [18, 19, 20]
for name, age in zip(names, ages):
     print(name,age)

dict1= dict(zip(names,ages))
print(dict1)












