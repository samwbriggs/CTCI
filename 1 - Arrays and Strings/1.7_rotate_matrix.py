# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # Are we given a 2D array with integers that represent 4 bytes of data in binary?
    # A great way to try and solve this is to draw an example and discern an optimal algorithm.

    # TODO: I would add some validation here to ensure the matrix given is in fact NxN.

    indexOffset: int = len(matrix) - 1
    # Loop through the entire matrix and swap items in the array.

    for i in range(0, int(len(matrix) / 2)):
        for j in range(i, indexOffset - i):
            temp: int = matrix[i][j]
            # Move left to top.
            matrix[i][j] = matrix[indexOffset - j][i]
            # Move bottom to left.
            matrix[indexOffset - j][i] = matrix[indexOffset - i][indexOffset - j]
            # Move right to bottom.
            matrix[indexOffset - i][indexOffset - j] = matrix[j][indexOffset - i]
            # Move top to right.
            matrix[j][indexOffset - i] = temp

    return matrix

mat: list[list[int]] = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

result: list[list[int]] = rotate_matrix(mat)
print(result)