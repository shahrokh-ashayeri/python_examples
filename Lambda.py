"""
    Lambda in Python
"""

# a sequence for traversing on it
data = [(3, "a"), (2, "f"), (3, "b"), (1, "e"), (5, "d"), (4, "c")]

# Sort above sequnce based on second value on each tuple
print(list(sorted(data, key=lambda n: n[1])))

# return elements if first value is greater than 3
print(list(filter(lambda n: n[0] > 3, data)))

# reaturn a list that consist of values * 2
print(list(map(lambda n: n[0] * 2, data)))
