import math


class Shape(object):
    def __init__(self, color="red"):
        self.color = color


class Circle(Shape):
    def __init__(self, radius, color="blue"):
        super().__init__(color=color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width=1.0, length=1.0, color="orange"):
        super().__init__(color)
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    class Square(Shape):
        def __init__(self, side=1.0, color="white"):
            super().__init__(color)
            self.side = side

        def area(self):
            return self.side**2


# Create objects
sh = Shape('purple')
print(f'Color of Shape sh: {sh.color}')

ci = Circle(radius=5)
print(f'Radius of Circle ci: {ci.radius}')
print(f'Color of Circle ci: {ci.color}')

re = Rectangle(width=2, length=8, color='yellow')
print(f'Color of Rectangle: {re.color}')
print(f'Area of Rectangle re: {re.area()}')

# Proof , is Shape a sub class of object
print(f'Is Shape a sub class of object: {isinstance(sh, object)}')

# proof, is Circle a sub class of Shape
print(f'Is Circle a sub class of Shape: {issubclass(Circle, Shape)}')
