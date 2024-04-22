# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # First track what rows/cols need to be zeroed out.
    rowsToZero = {}
    colsToZero = {}
    for i, row in enumerate(matrix):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                rowsToZero[i] = 1
                colsToZero[j] = 1

    # Format the matrix to be zeroed out.
    for i, row in enumerate(matrix):
        for j in range(0, len(matrix[0])):
            if i in rowsToZero or j in colsToZero:
                matrix[i][j] = 0

    return matrix

result: list[list[int]] = zero_matrix([[0, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 12]])
print(result)