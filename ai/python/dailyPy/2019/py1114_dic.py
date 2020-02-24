#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 字典
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存
dic = {'name':'hong', 'age':29}
print(dic)
print(dic['age'])

# 修改
dic['age'] = 30
dic['gender'] = 'male'

print(dic)

# 删除
del dic['gender']
print(dic)

# dic.clear()
# print(dic)

# 方法
print(str(dic))












