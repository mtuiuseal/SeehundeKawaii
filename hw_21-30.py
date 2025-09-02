# 21. Write a Python program to convert a list of characters into a string.
d = [ '胸', 'が', 'は', 'ち', '切', 'れ', 'そ', 'う', 'で' ]
str = ''.join(d)
print(str)

# 22. Write a Python program to find the index of an item in a specified list.
num = [ 28, -12, 23, -11, 5, -7, 14, -1, 0, 6 ]
print(num.index(0))

# 23. Write a Python program to flatten a shallow list.
import itertools

og_list = [ [ 2, 8, 1 ], [ 2, 3, 1, 1 ], [ 4, 1 ], [ 5, 7, 6 ] ]
new_merged_list = list(itertools.chain(*og_list))
print(new_merged_list)

# 24. Write a Python program to append a list to the second list.
lst1 = [ 2, 3, 1, 1 ]
lst2 = [ 'ce', 'tl', 'hd', 'st' ]
fn_list = lst1 + lst2
print(fn_list)

# 25. Write a Python program to select an item randomly from a list.
import random

letters_lst = [ 'n', 'v', 'h', 'd', 'l', 'l', 'm', 't', 't', 'n', 'm', 'n', 'n', 'h', 'n', 'b' ]
print(random.choice(letters_lst))

# 26. Write a Python program to check whether two lists are circularly identical.
m = [ 10, 1, 0, 0, 10 ]
n = [ 10, 1, 0, 0, 10 ]
rotations = [ m[ i: ] + m[ :i ] for i in range(len(m)) ]
print(n in rotations)

# 27. Write a Python program to find the second smallest number in a list.
d = [ 28, -12, 23, -11, 5, -7, 14, -1, 0, 6 ]
h = set(d)
print(sorted(h)[ 1 ])

# 28. Write a Python program to find the second largest number in a list.
n = [ 28, -12, 23, -11, 5, -7, 14, -1, 0, 6 ]
n.sort(reverse = True)
print(n[ 1 ])

# 29. Write a Python program to get unique values from a list.
v = [ 28, -12, 23, -11, 5, -7, 14, -1, 0, 6 ]
print('Original list: ', v)
m = set(v)
t = list(m)
print('Unique numbers:', t)

# 30. Write a Python program to get the frequency of elements in a list.
import collections

l = [ 2, 8, 1, 2, 2, 3, 1, 1, 0, 5, 0, 7, 1, 4, 1, 0, 6 ]
print('Original list: ', l)
mt = collections.Counter(l)
print('Frequency in list:', mt)
