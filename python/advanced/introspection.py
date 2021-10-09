"""An exercise on introspections"""

# Define the Vehicle class.
class Vehicle:
    """An example of the vehicle class"""
    name = "BMW"
    kind = "car"
    color = "black"
    value = 100.00

    def description(self):
        """Function outputs description of the car"""
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# Print a list of all attributes of the Vehicle class.
# Your code goes here
print(dir(Vehicle))
