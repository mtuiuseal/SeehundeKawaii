# 51. Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
from idlelib.pyshell import fix_x11_paste

k = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' ]


def l(m, step):
    return [ m[ n::step ] for n in range(step) ]


print(l(k, 5))

# 52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
from collections import Counter

o = [ 'is', 'she', 'all', 'that', 'you', 'want', '?' ]
p = [ 'is', 'she', 'all', 'that', 'you', 'need', '?' ]
q = Counter(o)
r = Counter(p)

print('1-2:', list(q - r))
print('2-1:', list(r - q))

# 53. Write a Python program to create a list with infinite elements.
import itertools

s = itertools.count()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# 54. Write a Python program to concatenate elements of a list.
t = [ 'giac', 'mo', 'khac' ]
print('_'.join(t))
print('/'.join(t))
print('.'.join(t))

# 55. Write a Python program to remove key-value pairs from a list of dictionaries.
u = [ {'v1': 'w1', 'v2': 'w2'}, {'v1': 'w3', 'v2': 'w4'} ]
print('Og list:')
print(u)
x = [ {y: z for y, z in a.items() if y != 'v1'} for a in u ]
print('New list:')
print(x)

# 56. Write a Python program to convert a string to a list.
b = ('Gleymdu mér aldrei þó ég héðan flýg')
c = b.split()
print(c)

# 57. Write a Python program to check if all items in a given list of strings are equal to a given string.
d1 = [ 'the', 'winner', 'takes', 'it', 'all' ]
d2 = [ 'the', 'winner', 'elskan', 'mín' ]

print(all(e == 'winner' for e in d1))
print(all(e == 'all' for e in d2))

# 58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
f1 = [ 1, 2, 3 ]
f2 = [ 4, 5, 6 ]
f1[ -1: ] = f2
print(f1)

# 59. Write a Python program to check whether the n-th element exists in a given list.
g = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]
glen = len(g) - 1
print(g[ glen ])

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
h = [ (2, 3), (4, 7), (8, 2) ]
print(min(h, key = lambda i: (i[ 1 ], -i[ 0 ])))
