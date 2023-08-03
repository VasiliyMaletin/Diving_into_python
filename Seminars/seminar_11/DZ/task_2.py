# Создайте класс Матрица. Добавьте методы для:
# вывода на печать, сравнения, сложения, *умножения матриц

class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def get_matrix(self):
        return self.matr

    def __add__(self, other):
        if len(self.matr) != len(other.matr) or len(self.matr[0]) != len(other.matr[0]):
            return f'Error: Матрицы разных размеров!'
        else:
            return Matrix([[self.matr[i][j] + other.matr[i][j] for j in range(len(self.matr[0]))]
                           for i in range(len(self.matr))])

    def __mul__(self, other):
        if len(self.matr[0]) != len(other.matr):
            return f'Error: Невозможно перемножить матрицы!'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other.matr)]
                        for i_row in self.matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self.matr) != len(other.matr) or len(self.matr[0]) != len(other.matr[0]):
            return f'Error: Матрицы разных размеров!'
        else:
            for i in range(len(self.matr)):
                for j in range(len(self.matr[0])):
                    if self.matr[i][j] != other.matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self.matr)):
            s += str(self.matr[i]) + '\n'
        return s


m_1 = [[1, 2, 4],
          [5, 6,  8],
          [2, 5, -2],
          [10, 5, 0]]

m_2 = [[1, 2, 4],
          [5, 6,  8],
          [5, 6,  8],
          [-2, 2, 0]]

m_3 = [[1, 2, 4, 5],
          [5, 6, 8, 0],
          [5, 0, -7, 1]]

m_4 = [[1, 2, 4, 5, 0],
          [5, 6, 8, 0, 0],
          [5, 0, -7, 1, 0]]

matr_1 = Matrix(m_1)
matr_2 = Matrix(m_2)
matr_3 = Matrix(m_3)
matr_4 = Matrix(m_4)

print("Cложение матриц:")
matr_sum = matr_1 + matr_2
print(matr_sum)

print("Умножение матриц:")
matr_mul = matr_1 * matr_3
print(matr_mul)
print(matr_1 * matr_4)

print("Cравнение матриц:")
print(matr_1 == matr_1)
print(matr_1 == matr_2)
