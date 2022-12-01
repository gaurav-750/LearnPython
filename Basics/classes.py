class Point:
    default_clr = "red"

    # !constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x}, {self.y})")


# p1 = Point(1, 2)
p1 = Point.zero()
p1.draw()
print(p1.x, p1.y)

print(type(p1))
print(isinstance(p1, Point))
