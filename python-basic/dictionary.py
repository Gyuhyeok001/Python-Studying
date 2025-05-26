# dictioanry
dic = {'name': 'lee', 'age': '22', 'phone': '123456789'}
print(dic)

# dictionary with list
dic = {'name': 'lee', 'age': '22', 'phone': ['123456789', '987654321']}
print(dic)
print(dic['phone'])
print(dic['phone'][0])
print(dic['phone'][1])

# dictionary(adding)
a = {1:'a'}
a[2] = 'b'
print(a)

# dictionary(delete)
a = {1:'a', 2:'b'}
del a[1]
print(a)

# dictionary(merge)
a = {1:'a', 2:'b'}
b = {3:'c', 4:'d'}
a.update(b)
print(a)

# dictionary(get value form Key)
NBA = {'lebron': 'LAL', 'curry': 'GSW', 'kawhi': 'LAC'}
print(NBA['lebron'])
print(NBA['curry'])
print(NBA['kawhi'])

# dictionary(keys, values, items, clear)
NBA = {'lebron': 'LAL', 'curry': 'GSW', 'kawhi': 'LAC'}
print(NBA.keys())
print(NBA.values())
print(NBA.items())
print(NBA.clear())

# dictionary(get)
dic = {'name': 'lee', 'age': '22', 'phone': '123456789'}
print(dic.get('name'))
print(dic.get('GENDER',"none"))
print(dic.get('age',"none"))

# dictionary(in)
dic = {'name': 'lee', 'age': '22', 'phone': '123456789'}
print('name' in dic)
print('gender' in dic)








