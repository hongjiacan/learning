#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 判断是否是闰年
year = 1900 #int(input("请输入一个年份: "))

if year%100 == 0:
	if year%400 ==0:
		print('{0}是闰年！'.format(year))
	else :
		print('{0}不是闰年！'.format(year))
elif year%4 == 0:
	print('{0}是闰年！'.format(year))
else :
	print('{0}不是闰年！'.format(year))