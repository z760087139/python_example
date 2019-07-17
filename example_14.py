def foo(a,b=None,c):
    return a + c

def foo_1(a,c,b=None):
    return a + c
    
foo_1(1,2)

def foo_2(a,b,c):
    return a + c

# foo_2(a=1,2)
foo_2(a=1,c=2,b=0)


def foo_3(a,b=None,*args,z,**kwargs):
    # print(*args)
    print(**kwargs)
    return a + b

# foo_3(1,2,3,b=4,c=5)
foo_3(1,2,3,4,c=5,d=6,z=10)
k = (3,4) 
j = {'c': 5, 'd': 6}
foo_3(1,2,*k,**j,z=10)



