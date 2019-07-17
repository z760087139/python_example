# 关于字典结构
d = {
    "a":['value a']
}
d['b'] = 'value b'
# 字典方法
print('='*30)
print(f'current d: {d}')
print(f"get key c : {d.get('c','value c')}")
print(f"setdafault key d : {d.setdefault('d','value d')}")
print('='*30)
print(f'current d: {d}')
print(f'popitem : {d.popitem()}')
print('='*30)
print(f'after popitme ,current d: {d}')
d.update(c)
print('='*30)
print(f'after update ,current d: {d}')

d.keys()