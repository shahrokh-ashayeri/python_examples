data = [(3, "a"), (2, "f"), (3, "b"), (1, "e"), (5, "d"), (4, "c")]

print(list(sorted(data, key=lambda n: n[1])))
print(list(filter(lambda n: n[0] > 3, data)))
print(list(map(lambda n: n[0] * 2, data)))
