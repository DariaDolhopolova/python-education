from datetime import datetime
from unittest.mock import Mock
import pytest

def even_odd(x):
    """Checks number if it even or odd.

    Args:
        x (int): number to check.

    Returns:
        str: result of check. `even` if given number is even
            and `odd` if the number is odd.
    """
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"


def sum_all(*numbers):
    """Sums all given numbers together.

    Args:
        *args (int or float): variable length argument list.


    Returns:
        int or float: the result of adding all numbers together.
    """
    result = 0
    for num in numbers:
        result += num
    return result


def time_of_day():
    """Identifies current time of day.

    Returns:
        str: current time of day. Could be: "night", "morning", "afternoon".
    """
    now = datetime.now()
    if now.hour >= 0 and now.hour < 6:
        return "night"
    if now.hour >= 6 and now.hour < 12:
        return "morning"
    if now.hour >= 12 and now.hour < 18:
        return "afternoon"
    return "night"


class Product:
    """Data class representation of a product in a shop.

    Args:
        title (str): title of the product
        price (float): price of one product
        quantity (int, optional): the amount of the product available.
            Defaults to 1
    """

    def __init__(self, title, price, quantity=1):
        self.title = title
        self.quantity = quantity
        self.price = price

    def subtract_quantity(self, num_of_products=1):
        """Subtracts the number of available products.

        Args:
            num_of_products (int, optional): number of products
                available to subtract. Defaults to 1.
        """
        self.quantity -= num_of_products

    def add_quantity(self, num_of_products=1):
        """Adds the number of available products.

        Args:
            num_of_products (int, optional): number of products
                available to add. Defaults to 1.
        """
        self.quantity += num_of_products

    def change_price(self, new_price):
        """Changes price of one product.

        Args:
            new_price (float): the price to change to.
        """
        self.price = new_price


class Shop:
    """Representation of the shop

    Args:
        products (list or Product, optional): products to add to a shop while creating it.
    """

    def __init__(self, products=None):
        if products is None:
            products = []
        elif isinstance(products, Product):
            products = [products]
        self.products = products
        self.money = .0

    def add_product(self, product):
        """Adds product to the shop.

        Args:
            product (Product): product to add to the shop.
        """
        self.products.append(product)

    def _get_product_index(self, product_title):
        """Looks for products in the shop.

        Args:
            product_title (str): title of the product to look for.

        Returns:
            int: the index of the product if it present in the shop else None
        """
        for index, product in enumerate(self.products):
            if product.title == product_title:
                return index
        return None

    def sell_product(self, product_title, qty_to_sell=1):
        """Sells product and returns the final money amount to pay.

        Args:
            product_title (str): the title of the product to sell.
            qty_to_sell (int, optional): the quantity of the product to sell.
                Defaults to 1.

        Raises:
            ValueError: in case if amount of available products
                of that type is less then given.

        Returns:
            float: money amount to pay.
        """
        product_index = self._get_product_index(product_title)
        receipt = .0
        if product_index is not None:
            if self.products[product_index].quantity < qty_to_sell:
                raise ValueError('Not enough products')
            else:
                receipt = self.products[product_index].price * qty_to_sell
                if self.products[product_index].quantity == qty_to_sell:
                    del self.products[product_index]
                else:
                    self.products[product_index].subtract_quantity(qty_to_sell)
                self.money += receipt
            return receipt


# Tests start here



# Test for even_odd() function
def test_even_odd():
    assert even_odd(3) == "odd"
    assert even_odd(6) == "even"
    assert not even_odd(0) == "odd"
    assert even_odd(-9) == "odd"


# Test for sum_all() function
def test_sum_all():
    assert sum_all(1, 5, 9) == 15
    assert round(sum_all(2, 2.6, -2.6)) == 2
    assert sum_all(0) == 0


# Test for time_of_day() function
night = datetime(2021, 7, 15, 4, 0, 0)
night_out_of_scale = datetime(2021, 5, 6, 19, 0, 0)
morning = datetime(2021, 7, 15, 8, 0, 0)
afternoon = datetime(2021, 7, 15, 16, 0, 0)
datetime = Mock()


def test_time_of_day():
    datetime.now.return_value = night
    assert time_of_day() == "night"
    datetime.now.return_value = night_out_of_scale
    assert time_of_day() == "night"
    datetime.now.return_value = morning
    assert time_of_day() == "morning"
    datetime.now.return_value = afternoon
    assert time_of_day() == "afternoon"


# Tests for Product class
@pytest.fixture
def bread():
    """Returns a bread product with quantity 10 and price 1.5"""
    return Product("bread", 1.50, 10)


@pytest.fixture
def milk():
    """Returns a milk product with price 3"""
    return Product("milk", 3)


def test_setting_quantity(bread):
    assert bread.quantity == 10


def test_initial_quantity(milk):
    assert milk.quantity == 1


def test_setting_name(bread):
    assert bread.title == "bread"


def test_setting_price(milk):
    assert milk.price == 3


def test_initial_add_quantity(milk):
    milk.add_quantity()
    assert milk.quantity == 2


def test_setting_add_quantity(bread):
    bread.add_quantity(5)
    assert bread.quantity == 15


def test_initial_subtract_quantity(bread):
    bread.subtract_quantity()
    assert bread.quantity == 9


def test_setting_subtract_quantity(bread):
    bread.subtract_quantity(10)
    assert bread.quantity == 0


def test_setting_subtract_quantity_insufficient_amount(milk):
    milk.subtract_quantity(2)
    assert milk.quantity == -1


def test_change_price(bread):
    bread.change_price(2)
    assert bread.price == 2


# Tests for class Shop
def test_initial_shop():
    shop = Shop()
    assert shop.products == []


def test_shop_with_one_product():
    shop = Shop(bread)
    assert shop.products == bread


@pytest.fixture
def shop():
    """Returns shop with milk and bread"""
    return Shop([bread, milk])


@pytest.fixture
def empty_shop():
    """Returns shop without products"""
    return Shop()


def test_shop_with_multiple_products(shop):
    assert shop.products == [bread, milk]


def test_add_product_to_empty_shop(empty_shop):
    empty_shop.add_product(bread)
    assert empty_shop.products == [bread]
    empty_shop.add_product(milk)
    assert empty_shop.products == [bread, milk]


def test_add_product_to_shop_with_products(shop):
    apples = Product("apples", 3.5, 5)
    shop.add_product(apples)
    assert shop.products == [bread, milk, apples]


# This test didn't pass
# AttributeError: 'function' object has no attribute 'title'
def test__get_product_index_not_there(shop):
    test = shop._get_product_index("apples")
    assert test == None


# Failed with the same error
def test__get_product_index_exists(shop):
    test = shop._get_product_index("milk")
    assert test is None


def test_sell_product_initial_quantity(shop):
    price = shop.sell_product("bread")
    assert round(price, 1) == 1.5

def test_sell_product_raises_value_error(shop):
    with pytest.raises(ValueError):
        shop.sell_product("milk", 10)

def test_sell_product_deletes_item(shop):
    shop.sell_product("bread", 10)
    assert shop.products == [milk]
