# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
x = 28.1205071401
y = -2.31106
print( )
print('Original Number:', x)
print('Formatted Number with sign:' + '{:+.2f}'.format(x))
print('Original Number:', y)
print('Formatted Number with sign:' + '{:+.2f}'.format(y))
print( )

# 32. Write a Python program to print the following positive and negative numbers with no decimal places.
x = 28.1205071401
y = -2.31106
print( )
print('Original Number:', x)
print('Formatted Number with no decimal places:' + '{:.0f}'.format(x))
print('Original Number:', y)
print('Formatted Number with no decimal places:' + '{:.0f}'.format(y))
print( )

# 34. Write a Python program to print the following integers with '*' to the right of the specified width.
x = 8
y = 528
print( )
print('Original Number:', x)
print('Formatted Number (right padding, width 2):' + '{:*< 3d}'.format(x))
print('Original Number:', y)
print('Formatted Number (right padding, width 6):' + '{:*< 7d}'.format(y))
print( )

# 35. Write a Python program to display a number with a comma separator.
x = 8000000
y = 80000000
print( )
print('Original Number:', x)
print('Formatted Number with comma separator:' + '{:,}'.format(x))
print('Original Number:', y)
print('Formatted Number with comma separator:' + '{:,}'.format(y))
print( )

# 36. Write a Python program to format a number with a percentage.
x = 0.23
y = -0.28
print( )
print('Original Number:', x)
print('Formatted Number with percentage:' + '{:.2%}'.format(x))
print('Original Number:', y)
print('Formatted Number with percentage:' + '{:.2%}'.format(y))
print( )

# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
x = 23
print( )
print('Original Number:', x)
print('Left aligned (width 10):' + '{:< 10d}'.format(x))
print('Right aligned (width 10):' + '{: 10d}'.format(x))
print('Center aligned (width 10):' + '{:^ 10d}'.format(x))
print( )

# 38. Write a Python program to count occurrences of a substring in a string.
str1 = 'Am D7 G Em Am D7 G Bm Em Am D7 G Bm Em'
print( )
print(str1.count('G'))
print( )

# 39. Write a Python program to reverse a string.
m = 'BoCcHaN iS cApRiCoRn!'[::-1]
print(m)

# 40. Write a Python program to reverse words in a string.
t = 'BoCcHaN iS cApRiCoRn!'
reversed_words = ''.join(t.split( )[::-1])
print(reversed_words)
