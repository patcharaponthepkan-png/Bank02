class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class square:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def print_area(shape):
        print(f'Area: {shape.area()}')

circle = Circle(5)
square = square(4,6)

print_area(circle)
print_area(square)