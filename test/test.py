from unittest import result


def get_count(value):
    result = []
    for i in value:
        if i in "aiueo":
            result.append("i")
    return(len(result))


def upper_sentence(value):
    result = []
    text_split = value.split(" ")
    for i in text_split:
        if(i[0]):
            result.append(i[0].upper()+i[1:])
    return " ".join(result)


print(upper_sentence("How can mirrors be real if our eyes aren't real"))
print(get_count("vowel"))

# Mask string, show only last 4 chars
# maskify("4556364607935616")
# ############5616
# maskify("64607935616")
# #######5616
# maskify("1")
# maskify("")


# Add number
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
# number_list(["a", "b", "c"])


# sum two lowest integer
# sum_integers([19, 5, 42, 2, 77])
