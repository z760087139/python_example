# iterator
class func1(object):
    def __init__(self):
        self.curr = 1
        self.prev = 0
    
    def __iter__(self):
        return self
#python 3
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

a = func1()
b = iter(a)  # same as a.__iter__()  

# generate
def foo():
    for i in range(10):
        x = yield i
        print(x)

a = foo()
# init
next(a)

b = a.send('a')
