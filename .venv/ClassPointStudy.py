import random
class Point:
    def __init__(self, x, y): #def inside of the class is a 'method', not a 'function'
        """
        Initialize a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x #define x attribute via self.x
        self.y = y #and assign the value x to it

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return:  <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #uses the same way of printing as str

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 #square root of the sum of x

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance #returns a boolean result, so either 'True' or 'False'

    def __eq__(self, other): #evaluates if two points are the same distance away from the point of origin. Returns 'True' if yes, 'False' if no
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance




if __name__ == "__main__":
    #now we need to instantiate it
    p = Point(1,2) #p is an instance of 1 and 2
    p2 = Point(2,3)
    p4 = Point(4.4,-55)
    print(f"p.x={p.x} and p.y={p.y}")
    print(f"p4.x={p4.x} and p4.y={p4.y}")
    p.x = 20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)

#create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10),random.randint(-10, 10))) #creates a list of 5 random point objects with x and y values between -10 and 10

print("I got these 5 random points:")
print(points) #expect 5 answers
p = Point(3, 4)
print(p.distance_orig())
p2 = Point(1, 1)
print(f"I am comparing p > p2: {p>p2}") #I expect to have True

#the final purpose is to sort the list of random points
points.sort()
print(points)
