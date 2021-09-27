""" This class is an example of heritage.
And an accurate description of some coffee science!
"""


class Robusta:
    """This is a parent of all classes.
    And of all coffees. Not so good by itself though.
    """
    caffeine = 'A lot of caffeine.'

    def __init__(self):
        """Initialises the class and puts in the description and
        biological name of robusta coffee species.
        """
        self.description = 'Coffea canephora. It was discovered in late-19th century in ' \
                           'Democratic Republic of Congo.'
        self.cup_taste = 'Put in the description of your coffee.'

    def coffee_description(self):
        """Prints the description.
        """
        print(self.description)

    @staticmethod
    def brew(brew_method):
        """Brew yourself some coffee.
        This method is heritable through all classes
        """
        return f'You brewed yourself some coffee using {brew_method} method.'

    @classmethod
    def variety_taste(cls):
        """Describes broadly speaking the taste of the whole species
        """
        return 'It tastes woody, bitter, a bit like a burnt-rubber.'

    @property
    def taste_of_cup(self):
        """Defines the taste of your robusta coffee as a property
         """
        return self.cup_taste

    @taste_of_cup.setter
    def taste_of_cup(self, taste):
        """You can set the description of your robusta coffee through this method.
        """
        self.cup_taste = taste

    @taste_of_cup.deleter
    def taste_of_cup(self):
        """ You can delete your description.
        """
        del self.cup_taste


class Arabica(Robusta):

    """This is a child of Robusta and some other species.
    """
    caffeine = "2 times less caffeine than in Robusta"

    def __init__(self):
        """Initialises the class and puts in the description and
        biological name of arabica coffee species.
        """
        self.description = """Coffea arabica. It was discovered in 19th century in Ethiopia.
        Genetically it is a child of Robusta."""
        super().__init__()

    def coffee_description(self):
        """Prints the description.
        """
        print(self.description)

    @classmethod
    def variety_taste(cls):
        """Describes broadly speaking the taste of the whole species
        """
        return 'It can taste floral, fruity, sweet and somewhat acidic,' \
               ' depends on the origin country.'

    @property
    def taste_of_cup(self):
        """Defines the taste of your arabica coffee as a property
         """
        return 'Your arabica coffee tastes like:' + self.cup_taste

    @taste_of_cup.setter
    def taste_of_cup(self, taste):
        """You can set the description of your arabica coffee through this method.
        """
        self.cup_taste = taste

    @taste_of_cup.deleter
    def taste_of_cup(self):
        """ You can delete your description.
        """
        del self.cup_taste


my_coffee = Arabica()
print(my_coffee.description)
my_coffee.taste_of_cup = 'Sweet, pleasant, a bit like strawberry'
print(my_coffee.taste_of_cup)

my_robusta = Robusta()
my_robusta.coffee_description()
