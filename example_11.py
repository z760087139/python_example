# 一般情况
for i in range(4):
    print(i)
    # i = 10

i = 0 
while i < 4:
    print(i)
    i += 1

# 判断语法，中断/跳过循环语句
for i in range(10):
    if i == 3:
        print(f'skip 3')
        continue
    elif i == 5:
        print(f'break at 5')
        break
    elif i % 2 or i ==1 :
        print(i) 
    else :
        print(f'even :{i}')

# i = 0
# if not i == 4
# do
# i += 1

