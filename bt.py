# 1. Write python program:
# a) Convert two lists into a dictionary
ci1 = ['Germany', 'Italy']
ci2 = ['Koln', 'Cecilia']

con = dict(zip(ci1, ci2))
print(con)

# b) Merge two Python dictionaries into one
dict1 = {'a': 28, 'b': 12}
dict2 = {'a': 23, 'b': 11}

dict1.update(dict2)
print(dict2)

# c) Print the value of key ‘history’ from the below dict
# {‘id’:4, ’history’:’sample’, ’price’:73}
dict = {
    'id': 4,
    'history': 'sample',
    'price': 73
}

print(dict['history'])

# d) Initialize dictionary with default values
keys = ['x', 'y', 'z']
default_value = 8
dict = {key: default_value for key in keys}
print(dict)

# e) Create a dictionary by extracting the keys from a given dictionary
lst = [{'future': 5, 'bye': 9, 'good': 1},
       {'future': 7, 'hi': 2, 'hai': 3},
       {'true': 1}]
print('Ogriginal list:' + str(lst))
key = 'future'
extract = [dict for dict in lst if key in [k for k, v in dict.items()]]
print('Filtered Dict:' + str(extract))

# f) Delete a list of keys from a dictionary
lst = [{'ffs': 1, 'efg': 2, 'rgfv': 3},
       {'ffs': 3, 'efg': 4, 'rgfv': 5},
       {'ffs': 5, 'efg': 6, 'rgfv': 7}]
del_keys = 'ffs'
for item in lst:
    item.pop(del_keys, None)
print(lst)

# g) Check if a value exists in a dictionary
a = {'rfs': 40, 'vfs': 12, 'ret': 36}
b = 12
if b in a.values():
    print(f'Value {b} exists in dictionary.')
else:
    print(f'Value does not exist in dictionary.')

# h) Rename key of a dictionary
dict1 = {'wwe': 'wert'}
dict1['qwe'] = dict1.pop('wwe')
print(dict1)

# i) Get the key of a minimum value from the following dictionary {‘a’:4, ’b’:18, ’c’:73}
a = {'a': 4, 'b': 18, 'c': 73}
min_value = min(a.values())
mininum = [k for k, v in a.items() if v == min_value]
print(mininum)

# j) Change value of a key in a nested dictionary
b = {
    'name': 'mtu',
    'age': 18,
    'hi': {
        'bye': 'sad',
        'hello': 'ok'
    }
}

b['hi']['hello'] = 'ok'
print(b)

# 2. Write a Python program that counts the number of times characters appear in a text paragraph.
d = ('Create a dictionary by extracting the keys from a given dictionary',
     'Delete a list of keys from a dictionary',
     'Check if a value exists in a dictionary',
     'Rename key of a dictionary')
d = d.lower()
stat = {}
pos = 0
for char in d:
    dem = 1
    if stat.get(char) is None:
        item = {'count': dem, 'position': [pos]}
        stat[char] = item
    else:
        dem = int(stat[char]['count']) + 1
        possi = list(stat[char]['position'])
        possi.append(pos)
        stat[char] = {'count': dem, 'position': possi}

    pos += 1

keys = sorted(stat.keys())
for key in keys:
    print(f'Character "{key}" appears {stat[key]['count']} times, at {stat[key]['position']}')


# 3. Write a program using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True


def prime_dict(n):
    pr_dict = {}
    key_counter = 1
    for num in range(2, n):
        if prime(num):
            pr_dict[key_counter] = num
            key_counter += 1
    return pr_dict


n_value = 80
prime_num = prime_dict(n_value)
print(f'Prime num less than {n_value} with keys start from 1:')
print(prime_num)


























































































