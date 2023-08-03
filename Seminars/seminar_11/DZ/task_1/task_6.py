# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:

    """
        Класс прямоугольника с методами сравнения
    """
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __str__(self):
        return f'{self.p}'

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p

    def __lt__(self, other):
        return self.p < other.p

    def __gt__(self, other):
        return self.p > other.p

    def __le__(self, other):
        return self.p <= other.p

    def __ge__(self, other):
        return self.p >= other.p


r1 = Rectangle(10)
r2 = Rectangle(5)
print(r1 + r2)
print(r2 - r1)
help(Rectangle)
