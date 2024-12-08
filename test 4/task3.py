
#  3: Find the Missing Number 
def find_missing_number(numbers):
    if len(numbers) == 1: return []

    result = []

    for i in range(1, len(numbers)):
        if numbers[i - 1] + 1 != numbers[i]:
            return numbers[i - 1] + 1
        
print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([3, 5, 6, 1, 2]))
print(find_missing_number([2]))


# assert find_missing_number([1, 2, 4, 5]) == 3
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
# assert find_missing_number([2]) == []