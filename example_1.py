
a = 10
def foo_1(a):
    print(f'before:{a}')
    a += 1
    print(f'after:{a}')

print(f'outer before:{a}')
foo_1(a)
print(f'outer after:{a}')



