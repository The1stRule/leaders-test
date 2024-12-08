
#  9: Identify Non-Prime Numbers Within a Range

def is_prime(num):
    if num == 1: return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def no_primes(start, end):
    result = []

    for i in range(start, end + 1):
        if not is_prime(i):
            result.append(i)
    return result


print(no_primes(10, 20))
print(no_primes(1, 10))
print(no_primes(24, 25))
print(no_primes(1, 1))

# Example Test Cases:
# Input: start = 10, end = 20
#  Output: [10, 12, 14, 15, 16, 18, 20]
# Input: start = 1, end = 10
#  Output: [1, 4, 6, 8, 9, 10]
# Input: start = 20, end = 30
#  Output: [20, 21, 22, 24, 25, 26, 27, 28, 30]
# Input: start = 24, end = 25
#  Output: [24, 25]
# Input: start = 1, end = 1
#  Output: [1]