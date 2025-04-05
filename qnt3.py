class Shape:
    def __init__(self, color):
        self.color = color
        print(f"Shape initialized with color: {self.color}")

    def calculate_area(self):
        # Placeholder method; does nothing in the base class
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height):
        # Call the constructor of the Shape class
        super().__init__(color)
        self.width = width
        self.height = height
        print(f"Rectangle initialized with width: {self.width} and height: {self.height}")

    def calculate_area(self):
        # Optionally call the base class's calculate_area (even though it does nothing)
        super().calculate_area()
        # Calculate and return the area specific to Rectangle
        return self.width * self.height


# Example usage
rectangle = Rectangle("blue", 5, 10)
print(f"The area of the rectangle is: {rectangle.calculate_area()}")
