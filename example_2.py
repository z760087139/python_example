
a = 10
def foo_1(a):
    print(f'before:{a};\nid:{id(a)}')
    print(f'='*30)
    a += 1
    print(f'after:{a};\nid:{id(a)}')
    print(f'='*30)


print(f'outer before:{a};\nid:{id(a)}')
print(f'='*30)
foo_1(a)
print(f'outer after:{a};\nid:{id(a)}')
