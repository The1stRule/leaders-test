
# 2: Sum of Positive Numbers with Flooring
def sum_of_floored_positives(numbers):
    return sum([int(i) for i in numbers if i > 0])

print(sum_of_floored_positives([1, -4, 7, 12]))
print(sum_of_floored_positives([-1.5, 2.7, -3.3, 4.8]))
print(sum_of_floored_positives([]))
print(sum_of_floored_positives([-1, -2, -3]))

# assert problem_2_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6  # floor(2.7) + floor(4.8) = 6
# assert problem_2_sum_of_positive([]) == 0
# assert problem_2_sum_of_positive([-1, -2, -3]) == 0