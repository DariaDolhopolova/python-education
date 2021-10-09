"""An example of iterator which changes string to the uppercase"""
class UppercaseIterator:
    """Iterator for changing characters in string to uppercase."""
    def __init__(self, data: str):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        new_letter = self.data[self.index].upper()
        self.index = self.index + 1
        return new_letter

uppercase = UppercaseIterator('not lowercase anymore')
print(iter(uppercase))
for char in uppercase:
    print(char)
