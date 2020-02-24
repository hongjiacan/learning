#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set

set1 = set([1,2,3])
print(set1)

# 新增
set1.add(1)
set1.add(4)
print(set1)

# 删除
set1.remove(2)
print(set1)


# 运用
set2 = set([1,3,5,7,9]) 
set3 = set([2,4,6,8,10,3])

# 交集
print(set2 & set3)
# 并集
print(set2 | set3)
# 差集
print(set2 - set3)














