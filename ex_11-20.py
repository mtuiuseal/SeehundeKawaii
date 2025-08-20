# 11. Write a Python program to remove characters that have odd index values in a given string.
def odd_values_string(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


print(odd_values_string('hijklmop'))
print(odd_values_string('thoretxiti'))


# 12. Write a Python program to count the occurrences of each word in a given sentence.
def word_count(str):
    counts = dict( )
    words = str.split( )
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count('i love my school for 4 days spring summer fall winter.'))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
user_input = input('Do you love chonky seal? ')
print('No need to ask, ', user_input.upper( ))
print('No need to ask, ', user_input.lower( ))

# 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
items = input('Input comma-separated sequence of words: ')
words = [word for word in items.split(',')]
print(','.join(sorted(list(set(words)))))


# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, word):
    return '<%s>%s</%s>' % (tag, word, tag)


print(add_tags('i', 'FatCat'))
print(add_tags('b', 'ChonkyFatCat'))


# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle(str, word):
    return str[:2] + word + str[2:]


print(insert_string_middle('[[]]', 'seehunde'))
print(insert_string_middle('{{}}', 'SeAl'))
print(insert_string_middle('<<>>', 'SIEGEL'))


# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def insert_end(str):
    sub_str = str[-2:]
    return sub_str * 4


print(insert_end('Chóquế'))
print(insert_end('Bưchan'))


# 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
def first_three(str):
    if len(str) > 3:
        return str[:3]
    else:
        return str


print(first_three('yippy'))
print(first_three('hmu'))
print(first_three('mt'))

# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
str1 = 'https://www.youtube.com/watch?v=lMKfZwnHzig&list=RDlMKfZwnHzig&start_radio=1'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

# 20. Write a Python function to reverse a string if its length is a multiple of 4.
str = input('Write sth: ')
if len(str) % 4 == 0:
    print(''.join(reversed(str)))
else:
    print(str)
