
# 1: Sum of Positive Numbers

def sum_of_positives(numbers):
    return sum([i for i in numbers if i > 0])

print(sum_of_positives([1, -4, 7, 12]))
print(sum_of_positives([-1, -2, -3, -4]))
print(sum_of_positives([]))
# Test Cases:
# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
# assert problem_1_sum_of_positive([]) == 0