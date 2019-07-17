a = 10
b = 20
def foo():
    print('='*10 + 'function foo' + '='*10)
    global b
    print(f'inside a: {a}')
    c = a + 1
    b += 1
    # a = c
    print(f'inside c: {c}')
    print(f'inside b: {b}')

def foo_e():
    print('='*10 + 'function foo_e' + '='*10)
    try:
        a = a +1
    except Exception as e:
        print('='*15 + 'error!'+ '='*15)
        print(str(e))

def foo_t():
    print('='*10 + 'function foo_t' + '='*10)
    a = 10
    a += 1
    print(f'a from foo_t : {a}')

foo()
foo_e()
foo_t()
print(f'outer a: {a}')
print(f'outer b: {b}')