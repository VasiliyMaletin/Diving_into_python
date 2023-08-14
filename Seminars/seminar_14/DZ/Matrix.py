from Exception import ValFormatError


class Matrix:
    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
