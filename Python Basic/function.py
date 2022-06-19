# function tanpa return langsung hasil

def my_function():
    print("Hello From My Function!")


def math(a, b):
    perkalian = a * b
    print(perkalian)

# function dengan return


def mathreturn(a, b):
    return a*b


# gabungan dari function tambah dan kurang

def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def tambahkurang():
    return tambah(2, 3) - kurang(2, 1)


print(tambahkurang())
print(mathreturn(6, 3))
math(6, 3)
my_function()
