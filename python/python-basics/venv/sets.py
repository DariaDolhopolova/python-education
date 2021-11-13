a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
a_set = set(a)
b_set = set(b)
a_only = a_set.difference(b_set)
print(f"People who did not attend event B: {a_only}")
