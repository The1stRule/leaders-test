
# 3) Remove Duplicates from a List
# Create a program that receives a list and removes duplicate elements while maintaining the original order.

def remove_duplicates(list):
    result = []

    for i in list:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(['a', 'b', 'a', 'c']))

# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

# 4) Factorial Calculation
# Create a program that receives a non-negative integer and returns its factorial.
# The factorial of a number n is the product of all positive integers from 1 to n.
# By definition, the factorial of 0 is 1.

def factorial_caluclarot(number):
    if number == 0 or number == 1:
        return 1
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i
    return factorial

print(factorial_caluclarot(5))
print(factorial_caluclarot(0))

# 5 --> 120
# 0 --> 1


# 5) Palindrome Checker
# Create a program that checks if a given string is a palindrome (reads the same forward and backward).
# The function should ignore spaces, punctuation, and capitalization

def palindrome_checker(string):
    string = "".join(string.lower().split(" "))
    return string == string[::-1]


print(palindrome_checker("A man a plan a canal Panama"))
print(palindrome_checker("Hello"))

# "A man a plan a canal Panama" --> True
# "Hello" --> False

# 6) Convert Pascal Case string into snake_case

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.



def to_snake_case(string):
    if type(string) == int:
        return str(string)
    
    result = ""

    for i in string:
        if i.isupper():
            result+= "_" + i
        else:
            result += i
    return "".join(result[1:].split(" "))

print(to_snake_case("TestController"))
print(to_snake_case("MoviesAndBooks"))
print(to_snake_case("App7 Test"))
print(to_snake_case(1))

# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

# 7) Fibonacci Sequence Generator
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

def fibonacci_sequence(number):
    result = [0, 1]

    while len(result) != number:
        result.append(result[-1] + result[-2])
    return result

print(fibonacci_sequence(5))
print(fibonacci_sequence(7))

# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

# 8) Orders (4 ქულა)

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# NOTE: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def orders(string):
    if string == "":
        return string
    
    string = string.split(" ")

    result = []

    for i in range(1, len(string) + 1):
        for x in string:
            if str(i) in x:
                result.append(x)
    return " ".join(result)

print(orders("is2 Thi1s T4est 3a"))
print(orders("4of Fo1r pe6ople g3ood th5e the2"))
print(orders(""))


# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

# 9) Prime time

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime(stop_index):
    result = []

    for i in range(2, stop_index + 1):
        if is_prime(i):
            result.append(i)
    return result

print(prime(11))


# 11 => [2, 3, 5, 7, 11]

# 10) "Eureka" numbers

# The Eureka numbers are numbers like this: 135 = 1^1 + 3^2 + 5^3. Which means that we have to take a number and sum its digits raised to the consecutive powers.
# First digit to power 1, second to power 2 and so on... If the result of that sum is the same as the number itself that means that number is Eureka.

# Create a function which receives a range like (a, b) and outputs every Eureka number in it.

# NOTE: Every number which has one digit is Eureka, because for example 5 = 5^1...

def is_eureka(number):
    numbers = list(str(number))
    
    sum = 0
    index = 1
    for i in numbers:
        sum += int(i) ** index
        index += 1

    if number == sum:
        return True
    return False

def eureka_nums(start, end):
    result = []

    for i in range(start, end):
        if is_eureka(i):
            result.append(i)
    return result

print(eureka_nums(1, 10))
print(eureka_nums(1, 100))


# Examples:
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]