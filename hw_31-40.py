# 31. Write a Python program to count the number of elements in a list within a specified range.
def count_num(lst, min, max):
    hd = 0
    for a in lst:
        if min <= a <= max:
            hd += 1
    return hd


lst1 = [ 28, 12, 11, 23, 0, 5, 0, 7, 14, 0, 1 ]
print(count_num(lst1, 0, 100))
lst2 = [ 'h', 'd', 'm', 't', 'm', 'n', 'n', 'b' ]
print(count_num(lst2, 'm', 'n'))

# 32. Write a Python program to check whether a list contains a sublist.
t = [ 2, 8, 1, 2, 0, 5, 0, 7, 1, 4, 0, 1 ]
u = [ 2, 3, 1, 1 ]

mtu = str(u)[ 1:-1 ] in str(t)[ 1:-1 ]
print(mtu)

# 33. Write a Python program to generate all sublists of a list.
d = [ 2, 8, 1 ]
hd = [ d[ i:j ] for i in range(len(d)) for j in range(i + 1, len(d) + 1) ]
print(hd)


# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
def prime_eratosthenes(n):
    prime_lst = [ ]
    for i in range(2, n + 1):
        if i not in prime_lst:
            print(i)
            for j in range(i * i, n + 1, i):
                prime_lst.append(j)


prime_eratosthenes(100)

# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q'], n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
a = [ 'b', 'c' ]
i = 3
d = [ '{}{}'.format(e, f) for f in range(1, i + 1) for e in a ]
print(d)

# 36. Write a Python program to get a variable with an identification number or string.
g = 100
print(format(id(g), 'g'))
h = 'always'
print(format(id(h), 'g'))

# 37. Write a Python program to find common items in two lists.
i = [ 1, 2, 4, 5, 7, 8 ]
j = [ 0, 1, 2, 3, 6, 8 ]
common = list(set(i) & set(j))
print(common)


# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def change(lst):
    for a in range(0, len(lst) - 1, 2):
        lst[ a ], lst[ a + 1 ] = lst[ a + 1 ], lst[ a ]
    return lst


k = [ 1, 2, 3, 4, 5, 6 ]
l = change(k)
print(l)

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
m = [ 28, 23, 5, 14 ]
n = int(''.join(map(str, m)))
print(n)

# 40. Write a Python program to split a list based on the first character of a word.
from itertools import groupby
from operator import itemgetter

o = [ 'But', 'I', 'can', 'see', 'us', 'lost', 'in', 'the', 'memory', 'August', 'slipped', 'away', 'into', 'a', 'moment',
      'in', 'time', 'Cause', 'it', 'was', 'never', 'mine' ]
for letter, words in groupby(sorted(o), key = itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
