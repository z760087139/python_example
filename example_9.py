b = 1
c = [2,3]
d = [c,4]
a = [b,c,d]
aa = [1,[2,3],[[2,3],4]]

# step 1
ca = a
print(f'step 1 \nid ca:{id(ca)} \nid a:{id(a)}\nid aa:{id(aa)}')

# step 2
a[1][0] = 'a'
aa[1][0] = 'a'
print(f'step 2 \na:{a} \nca:{ca}\naa:{aa}')


# step 3
d[0][1] = 'b'
print(f'step 3 \na:{a} \nca:{ca}\naa:{aa}')



