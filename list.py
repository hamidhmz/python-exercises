"""list"""

letters = ['a', 'b', 'c', 'd']
matrix = [[0, 1], ['a', 'sy']]

zeros = [0] * 5

combined = zeros
print('\nzeros: ', zeros)

chars = list("Hello world")
print('\nchars: ', chars)

letters[0] = "A"
print('\nletters[0:3]: ', letters[0:3])
print('\nletters[::2]: ', letters[::2])

numbers = list(range(20))
print('numbers[::-1]: ', numbers[::-1])


# --------------------------------- unpacking -------------------------------- #
numbers1 = [1, 2, 3, 4, 5]
first, second, *others = numbers1
print('second: ', second)
print('first: ', first)
first, *others, last = numbers1
print('first: ', first)
print('last: ', last)

# ---------------------------- adding and removing --------------------------- #
# add
print('before append letters: ', letters)
letters.append('e')
print('after append letters: ', letters)
letters.insert(1, '_')
print('after insert 1 letters: ', letters)

# remove
letters.pop(0)
print('after pop 0 letters: ', letters)
letters.remove('e')
print('after remove e letters: ', letters)
del letters[0:3]
print('after del 0 till 3 letters: ', letters)
letters.clear()
print('after calling clear method letters: ', letters)

# ----------------------------- find item in list ---------------------------- #
letters = ['a', 'b', 'c']
print('letters.index("a"): ', letters.index('a'))
try:
    print('letters.index("t") will throw an exception: ', letters.index('t'))
except ValueError as error:
    print(error)

# ------------------------ checking if exists in list ------------------------ #
if 't' in letters:
    print('letters.index("t"):', letters.index('t'))

letters.count('d')
print('letters.count("a"): ', letters.count('a'))
letters.count('t')
print('letters.count("t"): ', letters.count('t'))

# ---------------------------------- sorting --------------------------------- #
numbers = [3, 4, 5, 1, 3, -1, -4, -2]

print('numbers.sort(reverse=True)', numbers.sort(reverse=True))
print('sorted(numbers,reverse=True)', sorted(numbers, reverse=True))

items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]


def sort_item(item):
    """sort_item"""
    return item[1]


items.sort(key=sort_item)
print('items: ', items)

items.sort(key=lambda item:item[1])
print('written by lambda items: ', items)
