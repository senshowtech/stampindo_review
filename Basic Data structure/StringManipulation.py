# type of
my_city = "New York"
print(type(my_city))

my_city = 'New York'
print(type(my_city))

my_city = str("New York")
print(type(my_city))

# Concatenate
word1 = 'New '
word2 = 'York'

print(word1 + word2)

# Select a char
word = "Rio de Janeiro"
char = word[0]
print(char)

# value in string
desc_str = "%s %s %s worth $%.2f." % (
    1, 2, 3, 5)
print(desc_str)

# split
my_phrase = "let's go to the beach"
print(my_phrase.split(" "))

val = 1
testfstring = f"{val} cek"
print(testfstring)
