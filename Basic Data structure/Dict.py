tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack'] = 4099
print(tel)
del tel['sape']
tel['irv'] = 4127
print(tel)
{'guido': 4127, 'irv': 4127, 'jack': 4098}
print(list(tel.keys()))
['irv', 'guido', 'jack']
print(sorted(tel.keys()))
print('guido' in tel)
