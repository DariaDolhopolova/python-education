import re

item_with_find = []
for item in dir(re):
    if 'find' in item:
        item_with_find.append(item)

print(sorted(item_with_find))