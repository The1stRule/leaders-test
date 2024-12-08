# 10: Edit Distance 

def min_distance(string1, string2):
    string1 = list(string1)

    for i in string2:
        if i in string1:
            string1.remove(i)
    return len(string1) + 1

print(min_distance("horse", "ros"))
print(min_distance("intention", "execution"))
print(min_distance("kitten", "sitting"))

# assert min_distance("horse", "ros") == 3
# assert min_distance("intention", "execution") == 5
# assert min_distance("kitten", "sitting") == 3