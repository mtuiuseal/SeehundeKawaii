# 1. Write a Python program to sum all the items in a list.
# 2. Write a Python program to multiply all the items in a list.
import random

lst = [ ]
for i in range(20):
    lst.append(random.randint(1, 1000))


def print_list():
    print(lst)


def hw_1_2():
    sum = 0
    product = 1
    for i in lst:
        sum += i
        product *= i
    print(f'Sum of items: {sum}')
    print(f'Product of items: {product}')


if __name__ == '__main__':
    print_list()
    hw_1_2()

# 3. Write a Python program to get the largest number from a list.
import random

lst = [ ]
for i in range(20):
    lst.append(random.randint(1, 100))


def print_list():
    print(lst)


def hw_3():
    largest = lst[ 0 ]
    for i in lst:
        if i > largest:
            largest = i
    print(f'Largest item: {largest}')


if __name__ == '__main__':
    print_list()
    hw_3()

# 4. Write a Python program to get the smallest number from a list.
import random

lst = [ ]
for i in range(20):
    lst.append(random.randint(1, 1000))


def print_list():
    print(lst)


def hw_4():
    smallest = lst[ 0 ]
    for i in lst:
        if i < smallest:
            smallest = i
    print(f'Smallest item: {smallest}')


if __name__ == '__main__':
    print_list()
    hw_4()

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def hw_5():
    str = [ 'strings', 'hachiware', 'seal', 'phep' ]
    dem = 0
    for st in str:
        if len(st) < 2:
            continue
        if st[ 0 ] == st[ -1 ]:
            dem += 1
    print(f'Item with same first char and last char: {dem}')


if __name__ == '__main__':
    hw_5()

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def last(n):
    return n[ -1 ]


def hw_6(tuples):
    return sorted(tuples, key=last)


print(hw_6([ (2, 3), (1, 4), (0, 5), (2, 8), (3, 7) ]))

# 7. Write a Python program to remove duplicates from a list.
dup = [ 2, 8, 1, 2, 0, 5, 0, 7, 1, 4, 0, 1 ]
rmv_dup = [ ]
for i in dup:
    if i not in rmv_dup:
        rmv_dup.append(i)
print(rmv_dup)

# 8. Write a Python program to check if a list is empty or not.
empt = [ 'neu co the quay lai tu dau' ]
if not empt:
    print('Empty!')
else:
    print('Not empty~')

# 9. Write a Python program to clone or copy a list.
lts = [ 28, 12, 5, 7, 14, 1, 23, 11 ]
new_lts = list(lts)
print(lts)
print(new_lts)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def long_wrd(n, str):
    wrd_len = [ ]
    txt = str.split(' ')
    for i in txt:
        if len(i) > n:
            wrd_len.append(i)
    return wrd_len


print(long_wrd(4, 'xin em thoi ve trong nhung giac mo dem nay'))
