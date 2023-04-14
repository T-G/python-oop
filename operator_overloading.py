class Point:
    '''A point in coordinate axis.'''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # overload the __str__()
    def __str__(self):
        return f'This is a point at coordinate {self.x}, {self.y}'


# Create two points
p1 = Point(2, 5)
p2 = Point(-1, 4)

print('-------------before overloading')
print(p1)

# __str__() is String representation of object
print(p1.__str__())
