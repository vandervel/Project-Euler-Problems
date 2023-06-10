# Find millionth lexicographic permutation of numbers 0 through 9.


import itertools as it

limit = 1000000
r = 10
digit_permutations = it.permutations(range(r))

digits = next(it.islice(digit_permutations, limit-1, limit))
print(sum([digit * 10 ** (r - 1 - i) for i, digit in enumerate(digits)]
