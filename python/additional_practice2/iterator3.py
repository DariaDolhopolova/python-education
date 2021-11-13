"""An example of iterator which changes string to the lowercase and prints it backwards"""
class BackwardsLowercaseIterator:
    """Iterator for changing characters in string to backward lowercase."""
    def __init__(self, data: str):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        new_letter = self.data[self.index].upper()
        return new_letter


lower = BackwardsLowercaseIterator('Live spals Namtab')
print(iter(lower))
for char in lower:
    print(char)
