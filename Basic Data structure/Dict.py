tel = {'jack': 4098, 'sape': 4139}
# tambah data e dict
tel['guido'] = 4127
print(tel)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
# ganti data dict jack
tel['jack'] = 4099
print(tel)
# delete data dict sape
del tel['sape']
tel['irv'] = 4127
print(tel)
# rubah dict ke list
{'guido': 4127, 'irv': 4127, 'jack': 4098}
print(list(tel.keys()))
# rubah dict ke list dengan sorted
['irv', 'guido', 'jack']
print(sorted(tel.keys()))
print('guido' in tel)
