# 1. Write a Python program to calculate the length of a string.
from collections import Counter

a = 'Hello World'
print(len(a))

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
b = 'SealSoCute'
freq = Counter(b)
print(dict(freq))

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
c = str(input('Write something: '))
if len(c) >= 2:
    result = c[:2] + c[-2:]
else:
    result = 'Empty'
print(result)


# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1


print(change_char('mèoméomeo'))


# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def d(string1, string2):
    return string2 + '' + string1


print(d('botrack', 'topdam'))


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def e(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    return string + 'ing'


print(e('oii'), e('trinhlaji'))


# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort( )
    return word_len[-1][0], word_len[-1][1]


result = find_longest_word(['TOIGAY', 'ILeT', 'yeusealnhuttgioi', 'RingaRingaRing'])
print('\nLongest word: ', result[1])
print('Length of the longest word: ', result[0])


# 9. Write a Python program to remove the nth index character from a nonempty string.
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))


# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchange.
def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]


print(change_string('qrstuv'))
print(change_string('56789'))
