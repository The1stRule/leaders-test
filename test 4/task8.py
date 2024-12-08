
#  8: Longest Consecutive Sequence

def longest_consecutive(numbers):
    numbers.sort()
    result = [numbers[0]]

    for i in numbers[1:]:
        if i - 1 == result[-1] or i == result[-1]:
            result.append(i)
        else: return result

    return result

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 0]))
print(longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]))
        
        

# Test Cases:
# assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
# assert longest_consecutive([0, 0]) == 1
# assert longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9