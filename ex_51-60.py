# 51. Write a Python program to find the first non-repeating character in a given string.
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None


print(first_non_repeating_character('hallo'))
print(first_non_repeating_character('tschüss'))
print(first_non_repeating_character('ddaannkkee'))

# 52. Write a Python program to print all permutations with a given repetition number of characters of a given string.
from itertools import product


def all_repeat(str1, rno):
    char = list(str1)
    results = []
    for c in product(char, repeat = rno):
        results.append(c)
    return results


print(all_repeat('lavie', 3))
print(all_repeat('merci', 2))
print(all_repeat('bonjour', 4))


# 53. Write a Python program to find the first repeated character in a given string.
def first_repeated_char(str1):
    for index, c in enumerate(str1):
        if str1[:index + 1].count(c) > 1:
            return c
    return 'None'


print(first_repeated_char('tenerte'))
print(first_repeated_char('olvidarme'))


# 54. Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
        if ch in temp:
            return ch, str1.index(ch)
        else:
            temp[ch] = 0
    return 'None'


print(first_repeated_char_smallest_distance('micasa'))
print(first_repeated_char_smallest_distance('sunset'))
print(first_repeated_char_smallest_distance('heavenly'))
print(first_repeated_char_smallest_distance('sweet'))


# 55.Write a Python program to find the first repeated word in a given string.
def first_repeated_word(str1):
    temp = set( )
    for word in str1.split( ):
        if word in temp:
            return word
        else:
            temp.add(word)
    return 'None'


print(first_repeated_word('mt um tu mt'))
print(first_repeated_word('mt um tu mt um mt tu'))
print(first_repeated_word('mt um tu um mt tu '))
print(first_repeated_word('mt um tu'))


# 56. Write a Python program to find the second most repeated word in a given string.
def word_count(str):
    counts = dict( )
    words = str.split( )
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    counts_x = sorted(counts.items( ), key = lambda kv: kv[1])
    return counts_x[-2]


print(word_count('Bá tước Monte Cristo (Le Comte de Monte Cristo) là một tiểu thuyết phiêu lưu của Alexandre Dumas. Cùng với một tác phẩm khác của ông là Ba người lính ngự lâm, tác phẩm thường được xem là tác phẩm văn học nổi tiếng nhất của Dumas. Cuốn sách này đã được viết xong năm 1844. Giống như nhiều tiểu thuyết khác của ông, tiểu thuyết này đã được mở rộng từ cốt truyện do người giúp việc cho nhà văn Auguste Maquet cộng tác. Câu chuyện xảy ra tại Pháp, Ý, các đảo trong Địa Trung Hải và Levant trong thời kỳ các sự kiện lịch sử trong năm 1815–1838 (ngay trước sự kiện Một trăm ngày dưới sự cai trị của Louis-Philippe của Pháp). Sự sắp đặt lịch sử là yếu tố cơ bản của cuốn sách. Câu chuyện chủ yếu liên quan đến các chủ đề công lý, sự báo thù, lòng từ bi, và lòng khoan dung, và được kể theo phong cách một câu chuyện phiêu lưu.'))

# 57.Write a Python program to remove spaces from a given string.
z = 'Bocchan is a seal'
z = z.replace(' ', '')
print(z)


# 58. Write a Python program to move spaces to the front of a given string.
def move_Spaces_front(str1):
    noSpaces_char = [ch for ch in str1 if ch != ' ']
    spaces_char = len(str1) - len(noSpaces_char)
    result = ' ' * spaces_char
    result = '"' + result + ''.join(noSpaces_char) + '"'
    return result


print(move_Spaces_front('christmas . last  '))
print(move_Spaces_front('  christmas.last  '))


# 59. Write a Python program to find the maximum number of characters in a given string.
def max_char_count(str1):
    max_char = ''
    max_count = 0
    for char in str1:
        count = str1.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char


print(max_char_count('bocchanbell'))


# 60. Write a Python program to capitalize the first and last letters of each word in a given string.
def capitalize_first_letter(str1):
    str1 = result = str1.title( )
    result = ''
    for word in str1.split( ):
        result += word[:-1] + word[-1].upper( ) + ' '
    return result[:-1]


print(capitalize_first_letter('pipopipopi'))
print(capitalize_first_letter('nobody new'))

