# ambil value array dengan loop biasa
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
for fruit in fruits:
    print(fruit)

# ambil value array dengan loop List Comprehensions
fruit_value = [fruit for fruit in fruits]
print(fruit_value)

# matriks
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])


# list methods
# split
# ubah string menjadi array
list = "a,b,c,d,e,f,g,h"
print(list.split(","))
# append
# sisipkan data ke belakang array di js push
list = [1, 2, 3, 4]
list.append(5)
print(list)

# extend
# sisipkan data ke array dengan array
list = [2, 3, 5]
list.extend([6, 7, 8])
print(list)

# insert
# memasukkan data ke array dengan urutan
list = [1, 2, 3]
list.insert(3, 0)
print(list)

# count
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

# remove
# hapus dari array
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.remove("orange")
fruits.remove("apple")
print(fruits)

# sort
# untuk mengurutkan array yang sama dari A-Z
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort()
print(fruits)

# pop
# hapus array setiap di pop
stack = [3, 4, 5, 6, 7]
stack.pop()
stack.pop()
stack.pop()
print(stack)
