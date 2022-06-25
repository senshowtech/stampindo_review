# ambil unique dari suatu string
data = set('abracadabraaaaa')
print(data)

# sama dengan ini
data1 = {x for x in 'abracadabra' if x not in ''}
print(data1)

# tidak ada order
data2 = set('abc')
data2.add("e")
print(data2)

data3 = [1, 2, 3, 4, 5]
print(1 in data3)
