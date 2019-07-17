# in example_2
# a = 10
# def foo_1(a):
#     print(f'before:{a};\nid:{id(a)}')
#     print(f'='*30)
#     a += 1
#     print(f'after:{a};\nid:{id(a)}')
#     print(f'='*30)

b = 1
c = [2,3]
d = [c,4]
a = [b,c,d]  # [1, [2, 3], [[2, 3], 4]]

def foo(x):
    print(f'x in foo(before change):{x}')
    x[1][0] = 'a'
    print(f'x in foo:{x}')

print(f'a before foo:{a}')
print(f'c before foo:{c}')
foo(a)
print(f'a after foo:{a}')
print(f'c after foo:{c}')
print(f'='*30)
def foo_1(x):
    x += 1
    print(f'x in foo:{x}')

print(f'a before foo:{a}')
print(f'b before foo:{b}')
foo_1(b)
print(f'a before foo:{a}')
print(f'b after foo:{b}')
