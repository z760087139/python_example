# @a
# def b(*arg,**kwargs) ...
# 等价于
# def a(b):
# #   exc function in a
#   return b(*arg,**kwargs)

import os
def write_log(*_tuple,**_dict):
    def get_func(func):
        def to_do(*args,**kwargs):
            try:
                func(*args,**kwargs)
            except Exception,e:
                log = 'logtest.txt'
                with open(log,'a') as file:
                    file.write(str(e))
                    file.write(str(args))
                    file.write(str(kwargs))
                    file.close()
                raise
        return to_do
    print(f'*_tuple：{_tuple}')
    print(f'**_dict：{_dict}')
    return get_func

class test_class(object):
    @write_log()
    def func(self,a,b,c):
        print '%s,%s,%s' % (a,b,c)

    def test3(self,a,b,c):
            print 'test3:%s,%s,%s' % (a,b,c) 

    def test(self,a,b,c):
        print 'test:%s,%s,%s' % (a,b,c) 
        @write_log(a,b,c)
        def test2(a,b,c):       
            self.test3(a,b,c)
        test2(a,b,c)
a = test_class()
a.test('a','b','c')


# ===========================
# https://blog.csdn.net/five3/article/details/83447467

