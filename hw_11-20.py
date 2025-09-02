# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def cm_mb(lst1, lst2):
    result = False
    for a in lst1:
        for b in lst2:
            if a == b:
                result = True
                return result


print(cm_mb([ 1, 2, 3, 4 ], [ 4, 5, 6, 7 ]))
print(cm_mb([ 1, 2, 3, 4 ], [ 5, 6, 7 ]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
lyrics = [ 'mat', 'em', 'nhoa', 'di', 'mascara' ]
lyrics = [ c for (i, c) in enumerate(lyrics) if i not in (1, 2, 3) ]
print(lyrics)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
array = [ [ [ '*' for col in range(6) ] for col in range(4) ] for row in range(3) ]
print(array)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [ 28, 12, 23, 11, 5, 7, 14, 1 ]
num = [ i for i in num if i % 2 != 0 ]
print(num)

# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle

lyrics = [ 'season', 'change', 'and', 'our', 'love', 'when', 'cold' ]
shuffle(lyrics)
print(lyrics)

# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def printSqrNum():
    l = list()
    for i in range(1, 30):
        l.append(i ** 2)
    print(l[ :5 ])
    print(l[ -5: ])


printSqrNum()

# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def test(nums):
    return all(is_prime(i) for i in nums)


def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for a in range(2, n):
            if (n % a == 0):
                return False
        return True


nums = [ 28, 12, 0, 6 ]
print('Original list:')
print(nums)
print('Checking prime numbers:')
print(test(nums))

nums = [ 2, 3, 11, 6 ]
print('\nOriginal list:')
print(nums)
print('Checking prime numbers:')
print(test(nums))

nums = [ 1, 5, 7, 14 ]
print('\nOriginal list:')
print(nums)
print('Checking prime numbers:')
print(test(nums))

# 18. Write a Python program to generate all permutations of a list in Python.
import itertools

print(list(itertools.permutations([ 6, 7, 8 ])))

# 19. Write a Python program to calculate the difference between the two lists.
lst1 = [ 0, 1, 2, 5, 7, 8 ]
lst2 = [ 1, 2, 3, 4, 6 ]
diff_lst1_lts2 = list(set(lst1) - set(lst2))
diff_lst2_lts1 = list(set(lst2) - set(lst1))
total_diff = diff_lst1_lts2 + diff_lst2_lts1
print(total_diff)

# 20. Write a Python program to access the index of a list.
nums = [ 1, 5, 6, 7, 11, 12, 14, 23, 28 ]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)
