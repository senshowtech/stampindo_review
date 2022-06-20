# ambil unique dari suatu string
data = set('abracadabraaaaa')
print(data)

# sama dengan ini
data1 = {x for x in 'abracadabra' if x not in ''}
print(data1)
