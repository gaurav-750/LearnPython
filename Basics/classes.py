# class Point:
#     default_clr = "red"

#     # !constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     # overriding the implementation for == operator
#     def __eq__(self, other) -> bool:
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x+other.x, self.y+other.y)


# p1 = Point(10, 12)
# # p1 = Point.zero()
# p1.draw()
# print(p1.x, p1.y)

# print(type(p1))
# print(isinstance(p1, Point))

# print('Object p1 is:', p1)


# p2 = Point(1, 2)
# print(p1 == p2)
# print(p2)

# # print(p1 > p2)

# print(p1+p2)


# class TagCloud:

#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem_(self, tag):
#         print(self.__tags.get(tag.lower(), 0))

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# print(cloud.__dict__)
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud._TagCloud__tags)
# print(cloud.tags)
# print(cloud.tags["python"])
# print(len(cloud))

# print(cloud.__iter__())

# print(cloud.__tags["Python"])


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise Exception("Price cannot be -ve!")

        self.__price = value

    price = property(get_price, set_price)


pro1 = Product(-20)
print(pro1.price)
