# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# short hand / ternary

# if
if a > b:
    print("a is greater than b")

# if else
a = 2
b = 330
print("a is greater than b") if a > b else print("b is greater than a")

# js
# {a == b ? "cek" : a < b ? "cek" : "cek"}
a = 390
b = 330
print("a is greater than b") if a > b else print(
    "equal") if a == b else print("b greater than a")
