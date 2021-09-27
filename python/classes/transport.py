"""These are the transport classes.
There are Transport, Car, Bus, Truck, Race Car and Engine.
"""


class Transport:
    """This is the basic transport class.
    It can drive, it can stop and it can break."""

    people_capacity = 0
    cargo_capacity = 0

    def __init__(self, speed):
        self.speed = speed

    def drive(self, max_speed):
        """This is the drive method with the maximum speed restriction.
        """
        if self.speed == max_speed:
            print('Drives with the maximum speed')
        elif self.speed > max_speed:
            print('Cannot go so fast!')
        elif self.speed < max_speed:
            print(f'Drives with the speed {self.speed}')
        else:
            print('The speed value is wrong')

    @staticmethod
    def stop():
        """This is just the stop method
        """
        print('The transport stops')

    @staticmethod
    def breaks():
        """This is the break method. How unfortunate...
        """
        print('The transport breaks')


class Car(Transport):
    """This is the Car class, it is the child of the Transport.
    It does pretty much the same as Transport, nothing too crazy.
    """

    people_capacity = 5
    cargo_capacity = 5


    def drive(self, max_speed):
        """The same drive method with a bit different text.
        """
        if self.speed == max_speed:
            print('The car goes with the maximum speed')
        elif self.speed > max_speed:
            print('The car cannot go so fast!')
        elif self.speed < max_speed:
            super().drive(max_speed)
        else:
            print('The speed value is wrong')


class Truck(Transport):
    """This is a truck, also a child of Transport.
    You can load cargo in it if you want to!
    """
    people_capacity = 2
    cargo_capacity = 50

    @staticmethod
    def load_cargo():
        """You can load cargo!
        """
        print('Cargo is loaded')


class RaceCar(Car, Transport):
    """The RaceCar is a child of Car and a grandchild of Transport.
    A bit fancier than a Car, it can speed up, slow down and even outrace someone!"""
    people_capacity = 1
    cargo_capacity = 0

    @staticmethod
    def speed_up(max_speed):
        """Speed up to the maximum speed!
        """
        print(f'The car speeds up to the maximum speed {max_speed}')

    @staticmethod
    def slow_down():
        """Slow down a bit.
        """
        print('The car slows down a bit.')

    @classmethod
    def outrace(cls):
        """You can always outrace someone!
        """
        print('The car outraces one car.')


class Bus(Transport):
    """The Bus is a child of Transport.
    It also can stop at the stops and let people in and out.
    """
    people_capacity = 50
    cargo_capacity = 10

    @staticmethod
    def stop():
        """Stop the bus!
        """
        print('The bus stops at the bus stop')

    @staticmethod
    def people_in():
        """Let the people in!
        """
        print('The bus lets people in')

    @staticmethod
    def people_out():
        """Let the people out!!!
        """
        print('The bus lets people out')


class Engine(Car, Transport):
    """This class is a child of a Car and of a Transport.
    It's just an engine, so it can be turned on and off
    and go to the maximum power."""

    def __init__(self):
        print('Initialize engine')
        super().__init__(0)

    @staticmethod
    def turn_on():
        """Turn it on.
        """
        print('The engine turns on.')

    @staticmethod
    def max_power(power):
        """Go to the max power!
        """
        print(f'The engine accelerates to the maximum power {power}')

    @staticmethod
    def turn_off():
        """Turn it off!
        """
        print('The engine turns off.')


my_car = Car(50)
my_car.drive(150)
my_car.drive(150)

my_truck = Truck(80)
my_truck.load_cargo()
my_truck.stop()
my_bus = Bus(50)
my_bus.drive(52)

my_bus.people_in()

my_race_car = RaceCar(55)
my_race_car.breaks()
my_race_car.speed_up(250)

my_engine = Engine()
my_engine.turn_on()
my_engine.max_power(500)
