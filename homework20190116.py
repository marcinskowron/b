def reverse_by_words(text):
    """returns words in reversed order"""
    return ' '.join(reversed(text.split()))

print(reverse_by_words('My dog is big'))

#################################


class Trapezium:
    def __init__(self, lbase, hbase, height):
        self.lbase = lbase
        self.hbase = hbase
        self.height = height

    def area(self):
        return 0.5 * (self.lbase + self.hbase) * self.height


class Parallelogram(Trapezium):
    def __init__(self, base, height):
        super().__init__(base, base, height)


class Rectangle(Parallelogram):
    def perimeter(self):
        return 2 * (self.lbase + self.height)


class Rhombus(Parallelogram):
    def perimeter(self):
        return 4 * self.lbase


class Square(Rhombus):
    def __init__(self, base):
        super().__init__(base, base)


print('\n', Trapezium(1, 3, 2).area())
print(Parallelogram(5, 2).area())
print(Rectangle(4, 2).area())
print(Rhombus(3, 2).area())
print(Square(5).area())

print('\n', Rectangle(4, 2).perimeter())
print(Rhombus(3, 2).perimeter())
print(Square(5).perimeter())

