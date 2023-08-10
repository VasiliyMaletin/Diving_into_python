# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class ValError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное значение  = {self.b}"


class ValFormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Ошибка: Невозможно сложить матрицы, матрицы разных размеров!"
        elif self.operation == '*':
            return f"Ошибка: Невозможно перемножить матрицы: не подходят размерности!"
        else:
            return f"Ошибка: Невозможно сравнить, так как матрицы разных размеров!"
