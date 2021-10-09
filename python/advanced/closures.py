"""Exercise on closures"""

def multiplier_of(multiply_by):
    """creates a function which can multiply a number by a"""
    def multiplier(number_to_multiply):
        """Takes number b and multiplies b by a"""
        return number_to_multiply * multiply_by
    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))


# can be also done with lambda
def multiplier_of1(multiply_by):
    """The same as above but with lambda"""
    return lambda x: x * multiply_by


multiplywith4 = multiplier_of1(4)
print(multiplywith4(10))
