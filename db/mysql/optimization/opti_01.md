#### 数据库优化

##### 设计篇
1. 选取最适用的字段属性
```
a. 字段宽度尽量小
b. 长度确定时， char > VARCHAR
c. 大小确定时， TINYINT > ... > BIGINT
tinyint: 1字节=8位，-128~127
smallint: 2字节，-32768~32767
int: 4字节，-2147483648~2147483647
bigint： 8字节，-2^63~2^63-1
```
2. 字段尽量设置为not null
```
将来执行查询的时候，数据库不用去比较NULL值
```

##### 索引篇
1. 在合适的字段上建索引
```

```
2. 不对含有大量重复的值的字段建立索引

##### to do or not to do篇
1. join 替代 子查询
2. 不要对有索引的字段做函数操作
3. 可以不用like的时候就不用like
```
select * from book where name like 'mysql%'
select * from book where name >= 'mysql' and name < 'mysqm'
```


