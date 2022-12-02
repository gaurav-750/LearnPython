from abc import ABC, abstractmethod


class Animal:

    def __init__(self):
        print("Animal cons")

        self.age = 1

    def eat(self):
        print("eat!")

# Animal - Base, Parent
# Mammal - Derived, Child


# class Mammal(Animal):  # Mammal class is inheriting Animal class

#     def __init__(self):
#         super().__init__()
#         print("Mammal cons")
#         self.weight = 62

#     def walk(self):
#         print("Walk!")


# class Fish(Animal):

#     def swim(self):
#         print("Swim!")


# m = Mammal()
# m.eat()
# m.walk()
# print(m.age)
# print(m.weight)

# print(dir(m))
# o = object()
# print(dir(o))

# print(isinstance(m, Animal))
# print(issubclass(Mammal, Animal))


class Bird(Animal):

    def fly(self):
        print("Bird Flying.")


class Chicken(Bird):
    pass


# !Multiple Inheritance:
class Employee:
    def __init__(self):
        print('Employee Cons!')

    def greet(self):
        print('Employee Greet!')


class Person:
    def __init__(self):
        print('Person Cons!')

    def greet(self):
        print('Person Greet!')


class Manager(Person, Employee):
    pass


m = Manager()
m.greet()


class InvalidOpError(Exception):
    pass


# todo Inheritance Example:
class Stream(ABC):

    def __init__(self):
        self.open = False

    def open(self):
        if self.open:
            raise InvalidOpError("Stream is already open!")
        self.open = True

    def close(self):
        if not self.open:
            raise InvalidOpError("Stream is already closed!")
        self.open = False

    @abstractmethod
    def read(self):
        print("reading from stream!")


class FileStream(Stream):
    def read(self):
        print("reading data from a file!")


class NetworkStream(Stream):
    def read(self):
        # return super().read()
        pass


class MemoryStream(Stream):
    def read(self):
        print("reading from memory-stream!")


# s1 = Stream()

ns = NetworkStream()
ns.read()

ms = MemoryStream()
ms.read()
