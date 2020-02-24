#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表 
# 查找和插入的时间随着元素的增加而增加
# 占用空间小
names = ['Tom', 'Jim', 'Kate']
print(names)
print(names[0])
print(names[0:2])
print(names[:2])
print(names[:])

# 更改
names[0] = 'Tomas'
print(names)

# 添加
names.append('Lily')
print(names)

# 删除
del names[0]
print(names)

# 运算符
print(len(names))
print(max(names))
print(min(names))




