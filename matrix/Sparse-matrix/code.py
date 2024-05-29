import os

class SparseMatrix:
    """
    A class to represent a sparse matrix.
    """

    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        """
        Initialize a sparse matrix from a file or with given dimensions.

        Args:
            file_path (str, optional): Path to the input file containing the matrix data.
            num_rows (int, optional): Number of rows in the matrix.
            num_cols (int, optional): Number of columns in the matrix.

        Raises:
            ValueError: If the input file has an incorrect format.
        """
        self.data = {}
        self.num_rows = num_rows
        self.num_cols = num_cols
        if file_path:
            self.load_from_file(file_path)
        # else:
        #     self.num_rows = num_rows
        #     self.num_cols = num_cols

    def load_from_file(self, file_path):
        """
        Load a sparse matrix from a file.

        Args:
            file_path (str): Path to the input file containing the matrix data.

        Raises:
            ValueError: If the input file has an incorrect format.
        """
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines()]

            self.num_rows = int(lines[0].split('=')[1])
            self.num_cols = int(lines[1].split('=')[1])

            for line in lines[2:]:
                line = line.strip()
                if line:
                    row, col, val = map(int, line[1:-1].split(','))
                    self.data[(row, col)] = val
        except (IndexError, ValueError) as e:
            raise ValueError(f"Input file has wrong format: {e}")

    def get_element(self, row, col):
        """
        Get the value of an element in the sparse matrix.

        Args:
            row (int): Row index of the element.
            col (int): Column index of the element.

        Returns:
            int: Value of the element at the given row and column indices.
        """
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        """
        Set the value of an element in the sparse matrix.

        Args:
            row (int): Row index of the element.
            col (int): Column index of the element.
            value (int): Value to be set for the element.
        """
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        """
        Add two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to be added to the current matrix.

        Returns:
            SparseMatrix: The result of adding the two matrices.

        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices have different dimensions")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value + other.get_element(row, col))
        for (row, col), value in other.data.items():
            if (row, col) not in self.data:
                result.set_element(row, col, value)

        return result

    def subtract(self, other):
        """
        Subtract one sparse matrix from another.

        Args:
            other (SparseMatrix): The matrix to be subtracted from the current matrix.

        Returns:
            SparseMatrix: The result of subtracting the two matrices.

        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices have different dimensions")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value - other.get_element(row, col))
        for (row, col), value in other.data.items():
            if (row, col) not in self.data:
                result.set_element(row, col, -value)

        return result

    def multiply(self, other):
        """
        Multiply two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to be multiplied with the current matrix.

        Returns:
            SparseMatrix: The result of multiplying the two matrices.

        Raises:
            ValueError: If the matrices have incompatible dimensions for multiplication.
        """
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices have incompatible dimensions for multiplication")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                val = sum(self.get_element(i, k) * other.get_element(k, j) for k in range(self.num_cols))
                if val != 0:
                    result.set_element(i, j, val)

        return result

if __name__ == "__main__":
    input_dir = "/home/collins/DSA-HW01---UniqueInt/matrix/input_files"
    input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".txt")]

    matrices = []
    for file_path in input_files:
        print(f"Loading  matrix from {file_path}")
        matrix = SparseMatrix(file_path)
        matrices.append(matrix)
        print(f"Loaded matrix: {matrix.data}\n")


    # Perform operations on the loaded matrices
    print("\nAddition:")
    for i in range(len(matrices)):
        for j in range(i+1, len(matrices)):
            matrix_i = matrices[i]
            matrix_j = matrices[j]
            if matrix_i.num_rows == matrix_j.num_rows and matrix_i.num_cols == matrix_j.num_cols:
                try:
                    result = matrix_i.add(matrix_j)

                    #do something with the result

                except ValueError as e:
                    print(f"Error adding matrices {i} and {j}: {e}")
            else:
                print(f"Cannot add matrices {i} and {j} because they have different dimensions") 
            #result = matrices[i].add(matrices[j])
            #print(f"Addition of Matrix {i+1} and Matrix {j+1}:")
            #print(result.data)
            #print()

    print("\nSubtraction:")
    for i in range(len(matrices)):
        for j in range(i+1, len(matrices)):
            result = matrices[i].subtract(matrices[j])
            print(f"Subtraction of Matrix {i+1} and Matrix {j+1}:")
            print(result.data)
            print()

    print("\nMultiplication:")
    for i in range(len(matrices)):
        for j in range(i+1, len(matrices)):
            try:
                result = matrices[i].multiply(matrices[j])
                print(f"Multiplication of Matrix {i+1} and Matrix {j+1}:")
                print(result.data)
                print()
            except ValueError as e:
                print(f"Error: {e}")
                print()


