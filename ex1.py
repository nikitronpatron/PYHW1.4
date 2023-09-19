# Напишите функцию для транспонирования матрицы

original_matrix = [
    [1, 2, 3],
    [4, 5, 6]]

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

transposed_result = transpose_matrix(original_matrix)
for row in transposed_result:
    print(row)