# open 
with open('example_15.txt','wb') as f:
    f.write('test')

class Sample:
    def __init__(self):
        print(f'__init__')

    def __enter__(self):
        print(f'__enter__')
        return self

    def __exit__(self, type, value, trace):
        print(f'__exit__')
        print (f"type:{type}")
        print (f"value:{value}")
        print (f"trace:{trace}")

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()
    # pass

# contextmanager:
# 通过yield 返回函数的结果给as 后的对象，执行完with 后的语句块后继续执行yield后续代码
# yield 前的部分相当于__enter__   yield 后的相当于 __exit__
from contextlib import contextmanager
@contextmanager
def file_open(path):
    try :
        f_obj = open(path,'w')
        yield f_obj
    except OSError:
        print('We had an error')
    finally:
        print('Closing file')
        f_obj.close()

path  = 'text.txt'
with file_open(path) as obj:
    obj.write('Testing context managers')