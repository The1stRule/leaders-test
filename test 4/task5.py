
# 5: Check if Two Strings are Anagrams

def are_anagrams(string1, string2):
    string1 = list(string1)

    for i in string2:
        if i in string1:
            string1.remove(i)

    return True if len(string1) == 0 else False

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
print(are_anagrams("triangle", "integral"))

# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True