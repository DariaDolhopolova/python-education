"""Decorator to make uppercase"""


def make_upper(function):
    """Outward layer of decorator, returns wrapper"""
    def wrapper():
        """Wrapper of the decorator, returns uppercase output"""
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@make_upper
def hello():
    """Prints hello and asks how are you"""
    return "Hello! How are you?"


print(hello())
