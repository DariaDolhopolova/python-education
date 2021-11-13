"""The realisation of Restaurant operations from UML diagram"""
import datetime as t
from time import sleep
import random

now = t.datetime.now()


class Restaurant:
    """Restaurant class with attributes: address, phone_number,
    menu, website, opening and closing times
    is_open is a method which checks if it is a working time for the restaurant"""
    address: str = ""
    phone_number = ""
    menu: dict = {}
    website = ""
    open_time = t.datetime(2021, 8, 17, 8, 0)
    close_time = t.datetime(2021, 8, 17, 21, 0)

    def __init__(self, address, phone_number, website):
        self.address = address
        self.phone_number = phone_number
        self.website = website

    @classmethod
    def is_open(cls):
        """The class method that tells you if the restaurant open or closed."""
        if cls.close_time.time() > now.time() > cls.open_time.time():
            return True
        return False

    def __repr__(self):
        return f"Restaurant is located at {self.address}," \
               f"phone number is {self.phone_number}, website - {self.website}"


class Staff:
    """Class that implements a general Staff object."""

    def __init__(self):
        self.is_working = Restaurant.is_open()

    def work_in_restaurant(self):
        """Method that tells you if staff is working already"""
        if self.is_working:
            return "Staff is working"
        return "Staff is not working"


class RestaurantHall(Restaurant):
    """The class that implements restaurant hall object"""
    is_dirty = False
    free_tables = 10
    need_to_clean_at = [t.time(12, 0), t.time(16, 0), t.time(20, 0)]

    @classmethod
    def when_dirty(cls):
        """This method tells if the restaurant hall needs cleaning or not,
        it should be cleaned at specific hours."""
        for time in cls.need_to_clean_at:
            if now.time() >= time and not cls.is_dirty:
                cls.is_dirty = True
        if cls.is_dirty:
            print("It's time to clean the hall!")

    def tables_booked(self):
        """This method tells how many tables are booked"""
        if self.free_tables < 10:
            if 10 - self.free_tables == 1:
                print("1 table is booked.")
            else:
                print(f"{10 - self.free_tables} tables are booked.")


class Kitchen(Restaurant):
    """Class that implements the kitchen of the restaurant"""
    is_dirty = False
    need_to_clean_at = [t.time(10, 0), t.time(12, 0), t.time(14, 0),
                        t.time(16, 0), t.time(18, 0), t.time(20, 0)]
    cooked_orders = 0

    @classmethod
    def when_dirty(cls):
        """This method tells if the kitchen needs cleaning or not,
             it should be cleaned at specific hours."""
        for time in cls.need_to_clean_at:
            if now.time() >= time and not cls.is_dirty:
                cls.is_dirty = True
        if cls.is_dirty:
            print("It's time to clean the kitchen!")


class Bathroom(Restaurant):
    """Class that implements the bathroom of the restaurant"""

    is_dirty = False
    use_count = 0

    @classmethod
    def get_dirty(cls):
        """This method tells if the bathroom needs cleaning or not,
                     it should be cleaned after 5 uses."""
        cls.use_count += 1
        if cls.use_count >= 5:
            cls.is_dirty = True
        if cls.is_dirty:
            print("It's time to clean the bathroom")


class CleaningStaff(Staff):
    """This class implements cleaning staff object which is inherited from Staff"""
    is_cleaning = False
    _people_count = 0

    def __init__(self, name):
        self.name = name
        super().__init__()
        CleaningStaff._people_count += 1

    @staticmethod
    def check_if_dirty(room: str):
        """This method checks if a specific room is dirty or not."""
        if room in ("kitchen", "Kitchen"):
            Kitchen.when_dirty()
            if Kitchen.is_dirty:
                print("Need to  clean the kitchen")
            else:
                print("Kitchen is clean")
        elif room in ("bathroom", "Bathroom"):
            if Bathroom.is_dirty:
                print("Need to clean the bathroom")
            else:
                print("Bathroom is clean")
        elif room in ("hall", "restaurant hall"):
            RestaurantHall.when_dirty()
            if RestaurantHall.is_dirty:
                print("Need to clean the restaurant hall")
            else:
                print("Restaurant hall is clean")
        else:
            print("Wrong input, try one of these: kitchen, bathroom, hall")

    def clean_kitchen(self):
        """Method to make kitchen clean again"""
        if not self.is_cleaning:
            self.is_cleaning = True
            Kitchen.is_dirty = False
            sleep(5)
            print("Kitchen is cleaned.")
            sleep(2)
            self.is_cleaning = False
            print(f"{self.name} is available again.")

    def clean_hall(self):
        """Method to make hall clean again"""

        if not self.is_cleaning:
            self.is_cleaning = True
            RestaurantHall.is_dirty = False
            sleep(5)
            print("Restaurant hall is cleaned.")
            sleep(2)
            self.is_cleaning = False
            print(f"{self.name} is available again.")

    def clean_bathroom(self):
        """Method to make bathroom clean again"""

        if not self.is_cleaning:
            self.is_cleaning = True
            Bathroom.is_dirty = False
            sleep(5)
            print("Bathroom is cleaned.")
            sleep(2)
            self.is_cleaning = False
            print(f"{self.name} is available again.")


class KitchenStaff(Staff):
    """This class implements kitchen staff object which is inherited from Staff"""
    is_cooking = False
    order_counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name

    @classmethod
    def orders_to_cook(cls):
        """This method checks how many orders are there to cook"""
        cls.order_counter = RestaurantHallStaff.orders_in_process + \
                            len(Delivery.available_to_deliver)

    def cook_order(self):
        """With this method a cook is cooking one order"""
        self.orders_to_cook()
        if self.order_counter:
            self.order_counter -= 1
            self.is_cooking = True
            print("Order is in process")
            sleep(3)
            print("Order is ready to be served to the customer")
            Kitchen.cooked_orders += 1
            sleep(1)
            self.is_cooking = False
            print(f"{self.name} is available again")
        else:
            print("There are no available orders")

    def prepare_groceries(self):
        """Kitchen staff prepares groceries for cooking"""
        sleep(2)
        print(f"{self.name} prepared some groceries for cooking")

    def clean_dishes(self):
        """Kitchen staff is cleaning dishes"""
        sleep(2)
        print(f"{self.name} cleaned some dishes")


class RestaurantHallStaff(Staff):
    """This class implements restaurant hall staff object which is inherited from Staff"""
    is_busy = False
    orders_in_process = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.dishes_taken = 0

    def accept_clients(self):
        """Accept customers and help them to find a table"""
        if RestaurantHall.free_tables:
            RestaurantHall.free_tables -= 1
            print(f"{self.name} took customers to the free table")
        else:
            print("There are no free tables now, unfortunately")

    def take_order(self, order_id):
        """Take order from customer"""
        self.orders_in_process += 1
        self.order_id = order_id
        return f"There are {self.orders_in_process} orders in process. Order {order_id} is taken."

    def take_order_to_kitchen(self):
        """Take order to the kitchen"""
        KitchenStaff.orders_to_cook()
        return f"{self.name} brought order {self.order_id} to kitchen"

    def receive_order(self):
        """Receive cooked order from the kitchen"""
        if Kitchen.cooked_orders:
            Kitchen.cooked_orders -= 1
            self.dishes_taken += 1
            print(f"{self.name} took order from kitchen")
        else:
            print("There are no available orders in the kitchen")

    def take_dish_to_customer(self):
        """Serve cooked order to customer"""
        if self.dishes_taken:
            self.dishes_taken -= 1
            print(f"{self.name} brought dish to the customer")


class Customer:
    """Implements customer class"""
    address = ""

    def __init__(self, name):
        self.name = name
        self.my_waiter = random.choice(waiters_list)
        self.total_price = 0

    def book_table(self):
        """Customer can book the table"""
        self.my_waiter.accept_clients()

    @staticmethod
    def leave_restaurant():
        """Customer can leave the restaurant"""
        RestaurantHall.free_tables += 1

    @staticmethod
    def go_to_bathroom():
        """Customer can go to the bathroom"""
        Bathroom.get_dirty()

    def make_order(self, dish: str, hall_or_delivery):
        """Customer can make order"""
        my_order = Order(dish, hall_or_delivery)
        if dish in Restaurant.menu.keys():
            self.total_price += Restaurant.menu[dish]
            if hall_or_delivery == "h":
                self.my_waiter.take_order(my_order.order_id)
            elif hall_or_delivery == "d":
                my_delivery = Delivery()
                my_delivery.deliver()
        else:
            print("We are sorry but this is not on the menu today.")

    def make_payment(self, is_cash, tips):
        """Customer can make payment"""
        my_payment = Payment(is_cash, tips, self.total_price)
        my_payment.payment()


class Payment:
    """A class  for creating a payment object"""
    def __init__(self, is_cash: bool, tips: float, dish_price):
        self.is_cash = is_cash
        self.tips = tips
        self.dish_price = dish_price
        self.all_total_price = self.dish_price + self.tips

    def payment(self):
        """Completing a payment"""
        if self.is_cash:
            print(f"Customer paid {self.all_total_price} in cash")
            self.all_total_price = 0
        elif not self.is_cash:
            print(f"Customer paid {self.all_total_price} with credit card")
            self.all_total_price = 0

    def __repr__(self):
        return f"Payment of total price {self.all_total_price}"


class Order:
    """A class for order"""
    order_id = 0

    def __init__(self, dish, hall_or_delivery):
        self.order_id += 1
        if dish in Kitchen.menu.keys():
            self.dish = dish
            self.price = Restaurant.menu[dish]
            if hall_or_delivery == "h":
                self.hall_or_delivery = "hall"
            elif hall_or_delivery == "d":
                self.hall_or_delivery = "delivery"
        else:
            print("We are sorry but this is not on the menu today.")


class Delivery:
    """Delivery class"""
    orders_and_addresses = {}
    available_to_deliver = []

    def __init__(self):
        self.orders_and_addresses[Order.order_id] = Customer.address

    def deliver(self):
        """A method to deliver"""
        self.available_to_deliver.append(self.orders_and_addresses.keys())
        order_id = random.choice(self.available_to_deliver)
        address = self.orders_and_addresses[order_id]
        my_deliverer = DeliveryStaff(random.choice(deliverers_list))
        my_deliverer.deliver_order(order_id, address)
        self.available_to_deliver.pop(self.available_to_deliver.index(order_id))


class DeliveryStaff(Staff):
    """This class implements restaurant delivery staff object which is inherited from Staff"""

    is_delivering = False

    def __init__(self, name):
        super().__init__()
        self.name = name

    def deliver_order(self, order_id, address):
        """A method to deliver order"""
        self.is_delivering = True
        sleep(3)
        print(f"{self.name} has delivered order {order_id} to the address {address}")
        self.is_delivering = False


waiters_list = []
waiters_names = ['Jack', 'Jason', 'Jacob', 'Jorge', 'Jill']
for waiter in waiters_names:
    waiters_list.append(RestaurantHallStaff(waiter))

customer_list = []
customers_names = ['Mary', 'Matt', 'Mads', 'Michael', 'Molly']
for customer in customers_names:
    customer_list.append(Customer(customer))

deliverers_list = []
deliverers_names = ['Peter', 'Pam', 'Patrick', 'Penelope', 'Parker']
for deliverer in deliverers_names:
    deliverers_list.append(DeliveryStaff(deliverer))
Restaurant.menu["soup"] = 2.5
Restaurant.menu["dessert"] = 3
Restaurant.menu["main course"] = 5
Restaurant.menu["drink"] = 1.5

cook1 = KitchenStaff("Bella")
customer1 = customer_list[0]

print(customer1.name)
print(customer1.my_waiter.name)
print(customer1.make_order('soup', 'h'))
customer1.my_waiter.take_order_to_kitchen()
print(cook1.orders_to_cook())
