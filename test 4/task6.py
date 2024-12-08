
# 6: Find Intersection of Two Lists

def find_intersection(list1, list2):
    list1 = "".join([str(i) for i in list1])
    list2 = "".join([str(i) for i in list2])

    result = []

    string = ""
    for i in list1:
        string += i
        if string in list2:
            result.append(string)
        else:
            string = ""

    max_len_str = ""
    for i in result:
        if len(max_len_str) < len(i):
            max_len_str = i

    return list(max_len_str)

print(find_intersection([1, 2, 3], [2, 3, 4]))
print(find_intersection([1, 1, 2], [1, 3]))
print(find_intersection([], [1, 2]))

# assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
# assert find_intersection([1, 1, 2], [1, 3]) == [1]
# assert find_intersection([], [1, 2]) == []