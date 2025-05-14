from ClassPointStudy import Point
import random

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)): #checks if x and y are integers or floats. if not, PointException is raised with a message
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x,y) #this replaces the self.x and self.y
        self.color = color

    def __str__(self): #creates a new str different from ClassPoint so it can add in the 'color' attribute
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p.distance_orig())
print(p)
colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "white", "burgundy", "periwinkle", "marsala"]
color_points = []
for i in range(10):
    color_points.append(ColorPoint(random.randint(-10, 10), random.randint(-10, 10), random.choice(colors)))

print(color_points)
color_points.sort() #sorts the list by distance from the origin, from closest to farthest
print(color_points)