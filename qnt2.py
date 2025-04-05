import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()  # Polymorphism at work
    return total_area

# Example usage
circle1 = Circle(5)
circle2 = Circle(3)
rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(2, 3)

shapes = [circle1, circle2, rectangle1, rectangle2]
total = calculate_total_area(shapes)

print(f"Total Area: {total:.2f}")  # Output: Total Area: 128.14
