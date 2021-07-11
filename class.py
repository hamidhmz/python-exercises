"""class"""


class Point:
    """class"""

    default_color = "red"

    def __init__(self, x, y):
        self.x_x = x
        self.y_y = y

    def __str__(self):
        """for convertion to string"""
        return f"({self.x_x}, {self.y_y})"

    def __gt__(self, other):
        """we don't need to implement both gt and lt python will figure out by it self"""
        return self.x_x > other.x_x and self.y_y > other.y_y

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

