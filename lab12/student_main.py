class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        self.data[row][column] = value

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.columns)]
        self.data = rotated_data
        self.rows, self.columns = self.columns, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    def diagonal(self):
        if self.rows != self.columns:
            raise ValueError("Matrix must be square to extract diagonal.")
        return [self.data[i][i] for i in range(self.rows)]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        matrix.data = list_of_lists
        return matrix

# Примеры использования:
matrix = Matrix(2, 3)
print(matrix.data)  # [[0, 0, 0], [0, 0, 0]]

matrix = Matrix(2, 3)
matrix.add_element(1, 2, 10)
print(matrix.data)  # [[0, 0, 10], [0, 0, 0]]

matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
print(matrix.sum_of_rows())  # [15, 20]

matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data)  # [[0, 0], [1, 0], [0, 2]]

matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data)  # [[14, 0], [0, 0]]

matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric())  # True

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data)  # [[3, 1], [4, 2]]

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten())  # [1, 2, 3, 4]

list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data)  # [[1, 2], [3, 4]]

matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal())  # [1, 2, 3]
