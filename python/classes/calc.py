"""This is a code for the class which implements a calculator.
"""


class Calculator:
    """This is a class for implementing:
    Addition
    Subtraction
    Multiplication
    Division
    """

    @staticmethod
    def add(first, second):
        """This method adds the 1st and the 2nd arguments.
        """
        return first + second

    @staticmethod
    def sub(first, second):
        """This method subtracts the 1st and the 2nd arguments.
        """
        return first - second

    @staticmethod
    def mul(first, second):
        """This method multiplies the 1st and the 2nd arguments.
        """
        return first * second

    @staticmethod
    def div(first, second):
        """This method divides the 1st by the 2nd argument.
        Exception is when you divide by 0.
        """
        if second == 0:
            return "You can t divide by zero!"
        return first / second


print(Calculator.div(10, 2))
