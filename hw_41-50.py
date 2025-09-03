# 41. Write a Python program to create multiple lists.
p = {}
for i in range(1, 11):
    p[ str(i) ] = [ ]
print(p)

# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
q = [ 'd', 'n', 'v', 'h', 'm', 't' ]
r = [ 't', 'n', 'm', 'h', 'b' ]
qr = set(q).difference(r)
print('Missing value in 2nd list:', ','.join(qr))
rq = set(r).difference(q)
print('Additional values in 2nd list:', ','.join(rq))

# 43. Write a Python program to split a list into different variables.
s = [ ('neu', 'tinh', 'minh', 'chua', 'thanh', 'hinh', 'hai'), ('neu', 'co', 'the', 'quay', 'lai', 'tu', 'dau'),
      ('lan', 'cuoi', 'ay', 'cung', 'qua', 'mat', 'roi') ]
t1, t2, t3 = s
print(t1)
print(t2)
print(t3)

# 44. Write a Python program to generate groups of five consecutive numbers in a list.
u = [ [ 5 * v + w for w in range(1, 6) ] for v in range(5) ]
print(u)

# 45. Write a Python program to convert a pair of values into a sorted unique array.
x = [ (2, 8), (1, 2), (2, 3), (1, 1), (0, 5), (0, 7), (1, 4), (0, 1), (2, 6) ]
print('Og list:', x)
print('Sorted list:', sorted(set().union(*x)))

# 46. Write a Python program to select the odd items from a list.
y = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
print(y[ ::2 ])

# 47. Write a Python program to insert an element before each element of a list.
z = [ 'its', 'making', 'you', 'cry' ]
print('Og list:', z)
z = [ a for elt in z for a in ('b', elt) ]
print('Updated list:', z)

# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
c = [ [ 'apo' ], [ 'ca' ], [ 'lypse' ] ]
print('\n'.join([ str(lst) for lst in c ]))

# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
d = [ 'wish', 'i ', 'was', 'good' ]
e = [ '1', '2', '3', '4' ]
print([ {'str': f, 'int': g} for f, g in zip(d, e) ])

# 50. Write a Python program to sort a list of nested dictionaries.
h = {'eyes': {'starry': 23}, 'nose': {'starry': 11}, 'lips': {'starry': 6}}
i = dict(sorted(h.items(), key = lambda j: j[ 1 ][ 'starry' ]))
print(i)
