"""class"""
from abc import ABC, abstractmethod
from collections import namedtuple


class Base(ABC):
    """this is just example for base class and it is abstract"""
    eat_constant = 'eat'

    def __init__(self):
        self.eat_sth = 'eat'

    def eat(self):
        """this is just an example for base method"""
        print(self.eat_constant)

    def do_sth(self):
        """this is just an example for base method"""
        self.eat()

    @abstractmethod
    def implement_this(self):
        """this must be implemented"""


class Point(Base):
    """class"""

    default_color = "red"
    __private_member = "green"
    __price = 0

    def __init__(self, x, y):
        super().__init__()
        self.x_x = x
        self.y_y = y
        self.default_color = 'black'
        self.__private_member_for_self = 'something'

    @property
    def price(self):
        """this is property"""
        return self.__price

    @price.setter
    def price(self, value):
        """price setter"""
        if value < 0:
            raise ValueError("price cannot be negative ")
        self.__price = value

    def implement_this(self):
        print('sth')

    def __str__(self):
        """for convertion to string"""
        return f"({self.x_x}, {self.y_y})"

    def __eq__(self, other):
        """when check for equality of two obj"""
        return self.x_x == other.x_x and self.y_y == other.y_y

    def __gt__(self, other):
        """we don't need to implement both gt and lt python will figure out by it self"""
        return self.x_x > other.x_x and self.y_y > other.y_y

    def get___private_member_for_self(self):
        """access to private member for self"""
        return self.__private_member_for_self

    def get_private_member_atr(self):
        """access to private member"""
        return self.__private_member

    @classmethod
    def zero(cls):
        """this is class method"""
        return cls(0, 0)

    def draw(self):
        """this is instance method"""
        print(f'Point ({self.x_x}, {self.y_y})')


print('before change Point.default_color: ', Point.default_color)
Point.default_color = 'yellow'
print('after change Point.default_color: ', Point.default_color)
regular_point = Point(1, 2)
regular_point.draw()
print('regular_point.default_color: ', regular_point.default_color)
POINT_ZERO = Point.zero()
POINT_ZERO.draw()
print('this is for showing __str__ magic method,POINT_ZERO: ', POINT_ZERO)
print('POINT_ZERO > regular_point', POINT_ZERO > regular_point)
print('POINT_ZERO == regular_point', POINT_ZERO == regular_point)
print('POINT_ZERO.__dict__: ', POINT_ZERO.__dict__)
print('Point.__dict__: ', Point.__dict__)

# -------------------------------- namedtuple -------------------------------- #
PointNamed = namedtuple("Point", ['x', 'y'])
p1 = PointNamed(x=10, y=2)
p2 = PointNamed(x=10, y=2)

print('p1 == p2', p1 == p2)
