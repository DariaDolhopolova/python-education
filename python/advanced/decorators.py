"""Building an example of decorator
which checks if the type that function returns
equals the type in decorator"""

def type_check(correct_type):
    """Outer decorator function
    Receives type that will be checked"""
    def check(old_function):
        """Inside this function is a new function which checks the type
        Takes the old function as an argument
        It returns a new function with type checked"""
        def new_function(old_arg):
            """Checks if the type is correct
            Returns the old function as it is or a message about wrong type"""
            if isinstance(old_arg, correct_type):
                return old_function(old_arg)
            else:
                return 'Wrong type'
        return new_function
    return check


@type_check(int)
def times2(num):
    """Multiplies a number by 2"""
    return num*2

print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    """Returns a first letter of the string"""
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
