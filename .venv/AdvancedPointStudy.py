from ColorPointStudy import ColorPoint, PointException

class AdvancedPoint(ColorPoint): #inherits all functionality from ColorPoint
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise TypeError("Invalid color, must be one of {self.COLORS}")
        super().__init__(x, y, color) #calls the 'def' in ColorPoint and initializes x, y, and color

    @property #we make 'x' accessible as a variable, but it is actually being controlled by methods. 'x' can take on a range of values, but we want to have it as 'given'
    def x(self):
        return self._x  # getter method

    @property
    def y(self):
        return  self._y

    @x.setter #allows you to change the value of 'x' even after it has been created
    def x(self, value):
        self._x = value  # "setter" method - you can set as per the rules we decide

    @y.setter
    def y(self, value):
        return self._y = value

    @property #lets color be read as a property
    def color(self):
        return self._color

    @classmethod #use class method for changing something about the class, not the instance
    def add_color(cls, color): #cls stands for class; this allows a new color to be added to the COLORS list
        """
        Adds a new valid color for our class
        :param cls:
        :param color:
        :return:
         """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color = "red"): #lets you create a point using a tuple such as (2,4) instead of having to write two separate arguments
        """
        Creates a new point from a tuple rather than 2 individual values
        :param coordinate:
        :param color:
        :return:
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod #makes it so that every time you use 'distance_2_points' the Euclidean distance formula is automatically applied instead of having to re-write it every time
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

AdvancedPoint.add_color("rojo")

p = AdvancedPoint(1,2,"red")
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))