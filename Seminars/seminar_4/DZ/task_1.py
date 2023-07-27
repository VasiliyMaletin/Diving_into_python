# Напишите функцию для транспонирования матрицы

def matrix_transposition(matrix):
    new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

matrix = [[1, 3, 5, 8], [2, 4, 6, 4]]
print(matrix_transposition(matrix))