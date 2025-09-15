# 1.Write a Python program to find the maximum and minimum values in a set.
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")

print(setn)
print(type(setn))

print("\nMaximum value of set:")
print(max(setn))

print("\nMinimum value of set:")
print(min(setn))

# 2.Write a Python program to check if a given value is present in a set or not.
nums = {1, 3, 5, 7, 9, 11}
print("Original set (nums): ", nums, "\n")
print("Test if 6 exists in nums:")
print(6 in nums)

print("Test if 7 exists in nums:")
print(7 in nums)

print("Test if 11 exists in nums:")
print(11 in nums)

print("Test if 0 exists in nums:")
print(0 in nums)

print("\nTest if 6 is not in nums")
print(6 not in nums)

print("Test if 7 is not in nums")
print(7 not in nums)

print("Test if 11 is not in nums")
print(11 not in nums)

print("Test if 0 is not in nums")
print(0 not in nums)

# 3.Write a Python program to check if two given sets have no elements in common.
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)

print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare x and y:")
print(x.isdisjoint(y))

print("\nCompare x and z:")
print(z.isdisjoint(x))

print("\nCompare y and z:")
print(y.isdisjoint(z))


# 4.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def word_count( words ):
    word_set = set(words)
    word_counts = {}

    for word in word_set:
        word_counts[word] = words.count(word)
    return word_counts


words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
print(word_count(words))


# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
def missing_numbers( set_nums1, set_nums2 ):
    return set(set_nums1) - set(set_nums2), set(set_nums2) - set(set_nums1)


set_nums1 = {1, 2, 3, 4, 5, 6}
set_nums2 = {3, 4, 5, 6, 7, 8}
result = missing_numbers(set_nums1, set_nums2)
print("Original sets:")
print(set_nums1)
print(set_nums2)

print("Missing numbers in the second set compared to the first:")
print(result[0])
print("Missing numbers in the first set compared to the second:")
print(result[1])

set_nums1 = {1, 2, 3, 4, 5}
set_nums2 = {6, 7, 8}
result = missing_numbers(set_nums1, set_nums2)
print("\nOriginal sets:")
print(set_nums1)
print(set_nums2)

print("Missing numbers in the second set compared to the first:")
print(result[0])
print("Missing numbers in the first set compared to the second:")
print(result[1])
