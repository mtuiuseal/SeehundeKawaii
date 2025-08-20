# 41. Write a Python program to strip a set of characters from a string.
def strip_chars(str, chars):
    return ''.join(c for c in str if c not in chars)


print( )
print('Original String: ')
print('Se lâcher la main, Silencieusement à tes côtés...')
print('After stripping a,â,à,i,u,e,é,o,ô')
print(strip_chars('Se lâcher la main, Silencieusement à tes côtés...', 'aâàiueéoô'))
print( )

# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
import collections

str1 = 'aufwiedersehenmeineliebe'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1
for c in sorted(d, key = d.get, reverse = True):
    if d[c] > 1:
        print('%s %d' % (c, d[c]))

# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
area = 2805.14
volume = 2311.026
decimals = 2
print('The area of the rectangle is {0:.{1}f}cm\u00b2'.format(area, decimals))
decimals = 3
print('The volume of the cylinder is {0:.{1}f}cm\u00b3'.format(volume, decimals))

# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
str1 = 'desapareces'
for index, char in enumerate(str1):
    print('Current character', char, 'position at', index)

# 45. Write a Python program to check whether a string contains all letters of the alphabet.
import string

alphabet = set(string.ascii_lowercase)
input_string = 'Pack my box with five dozen liquor jugs'
print(set(input_string.lower( )) >= alphabet)
input_string = 'Siento que me cuesta ya respirar'
print(set(input_string.lower( )) >= alphabet)

# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
str1 = 'Its making you cry every time'
print(str1.split(' '))
str1 = 'Its-making-you-cry-every-time'
print(str1.split('-'))

# 47. Write a Python program to lowercase the first n characters in a string.
str1 = 'SEALCINNABUCHAN|BELL'
print(str1[:4].lower( ) + str1[4:])

# 48. Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
amount = '23.112,812'
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)


# 49. Write a Python program to count and display vowels in text.
def vowel(text):
    vowels = 'aiueoAIUEO'
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])


vowel('gaumeobellbell')

# 50. Write a Python program to split a string on the last occurrence of the delimiter.
str1 = 'v,u,n,g,k,i,u,c'
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))
