a = []
# 增加序列内容
a.append(1)
a.insert(0,0)

b = [2,3]
a.extend(b) # 等同于 a = a + b
a.insert(3,b)

# 分片
c = a[:] # 可以用于复制
# c = a[1::3]
# c = a[-3:-1]
a[1:1] = b
a[1:4] = b

# 索引 只返回第一个找到的值
a.index(b)

# 删除
a.remove(b)
# del a[0]

# 排序\
a = [
    [1,2,3,4],
    [2,3,4,5],
    [7,6,4,2]
]
a.sort(key=lambda x: x[0])
a.reverse()


