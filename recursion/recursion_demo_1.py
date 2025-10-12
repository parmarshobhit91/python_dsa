# RECURSION

# Function calling itself is called recursion
# A recursive method solves a problem by calling a copy of itself to work on a smaller problem.
# It is important to terminate recursion.
# Whenever function call itself it will call with slightly simpler version of itself.
# Base case is a condition when you are not calling function again


# Example: First n natural number

def print_n(n):
    if n == 0:  # base case
        return
    print_n(n - 1)  # recursive case
    print(n)
# print_n(5)

def reverse_print_n(n):
    if n == 0:
        return
    print(n)
    reverse_print_n(n-1)
# print("Reverse print")
# reverse_print_n(10)

def print_even_upto_n(n):
    if n == 0:
        return
    print_even_upto_n(n-1)
    if n % 2 == 0:
        print(n)
# print_even_upto_n(8)

def print_n_evens(n):
    if n == 0:
        return
    print_n_evens(n-1)
    print(n*2)
# print_n_evens(5)

def sum_of_n_natural_number(n):
    if n == 1:
        return n
    return n + sum_of_n_natural_number(n-1)
# k = sum_of_n_natural_number(2)
# print(k)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
# k = factorial(5)
# print(k)

def sum_of_n_even_numbers(n):
    if n == 1:
        return 2
    return 2*n + sum_of_n_even_numbers(n-1)
# print(sum_of_n_even_numbers(5))

def sum_of_n_odd_numbers(n):
    if n == 1:
        return 1
    return (2*n)-1 + sum_of_n_odd_numbers(n-1)
# print(sum_of_n_odd_numbers(10))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))

def decimal_to_binary(n):
    if n > 0:
        decimal_to_binary(n//2)
        print(n%2, end='')
# decimal_to_binary(6)

def decimal_to_octal(n):
    if n > 0:
        decimal_to_octal(n//8)
        print(n%8, end='')
# decimal_to_octal(65)

def reverse_number(n):
    if n>0:
        print(n%10, end='')
        reverse_number(n//10)
reverse_number(12)