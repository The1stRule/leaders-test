
# 4: Longest Substring Without Repeating Characters

def longest_unique_substring(string1):
    result = []

    string2 = ""
    
    for i in string1:
        if i not in string2:
            string2 += i
        else:
            result.append(string2)
            string2 = ""

    result.append(string2)
    
    max_len = 0

    for i in result:
        if max_len < len(i):
            max_len = len(i)
            
    return max_len

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring(""))
print(longest_unique_substring("pwwkew"))


# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3