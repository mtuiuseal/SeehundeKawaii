# 1.Write a Python function to find the maximum of three numbers.
a = 28
b = 5
c = 14
m = max(a, b, c)
print(m)

# 2.Write a Python function to sum all the numbers in a list.
lst = [ 2, 8, 1, 2, 2, 3, 1, 1, 0, 5, 0, 7, 1, 4, 0, 1 ]
s = sum(lst)
print(s)

# 3.Write a Python program to reverse a string.
str = 'Bocchan Kawaii'[ ::-1 ]
print(str)


# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('Insert number: '))
print(factorial(n))


# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def check_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


print(check_prime(59))


# 6.Write a Python function to print
# 2.the first N prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def the_first_n_primes(N):
    count = 0
    num = 2
    prime = [ ]

    while count < N:
        if is_prime(num):
            prime.append(num)
            count += 1
        num += 1

    return prime


if __name__ == '__main__':
    N = 20
    print(the_first_n_primes(N))


# 1.all prime numbers that less than a number (enter prompt keyboard).
def primes_under_n(n):
    for i in range(2, n):
        if is_prime(i):
            print(i)


if __name__ == '__main__':
    print(primes_under_n(20))


# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.
def is_perfect(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


print(is_perfect(20))
print('Perfect numbers less than 1000:')
print([ num for num in range(2, 1000) if is_perfect(num) ])

# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog")
import string

s = 'Pack my box with five dozen liquor jugs'
p = all(letter in s.lower() for letter in string.ascii_lowercase)
print(p)

