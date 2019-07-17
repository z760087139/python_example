import re
# 关于字符串使用
a = 'tttttttt'
print(type(a))
b = a.encode('utf-8')
print(type(b))

# 写入文件需要bytes
# f = open('...')
with open('test.txt','wb') as f:
    try:
        f.write(b)
        f.write(a)
    except Exception as e:
        print(str(e))

# 正则判断需要str
try:
    print(re.compile('t').search(a).group())
    print(re.compile('t').search(b).group())
except Exception as e:
    print(str(e))

