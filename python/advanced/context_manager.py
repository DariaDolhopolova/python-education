"""Context manager for managing files"""


class MyContextManager:
    """A simple context manager"""
    def __init__(self, filename, mode):
        """Takes filename and mode in which you'll work with the file"""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """This method opens the file and allows you to work with it in the specified mode"""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """This method is to close file and exit context manager, so you don't forget to do it!"""
        self.file.close()


with MyContextManager('test.txt', 'w') as f:
    f.write("Hello, I'm testing this")

print(f.closed)
