"""
NumPy Matrix Operations
Author: Ayush Rajput
Description: Create two matrices and perform addition, subtraction,
matrix multiplication, and transpose operations.
"""

import numpy as np


def read_matrix(name):
    """Read a matrix from the user and return it as a NumPy array."""
    while True:
        try:
            rows = int(input(f"Enter number of rows for {name}: "))
            cols = int(input(f"Enter number of columns for {name}: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue

            print(f"Enter {rows * cols} values for {name}, row by row:")
            matrix = []
            for i in range(rows):
                while True:
                    values = input(f"Row {i + 1}: ").split()
                    if len(values) != cols:
                        print(f"Please enter exactly {cols} values.")
                        continue
                    try:
                        matrix.append([float(value) for value in values])
                        break
                    except ValueError:
                        print("Please enter numeric values only.")
            return np.array(matrix)
        except ValueError:
            print("Please enter valid whole numbers for rows and columns.")


def display_matrix(title, matrix):
    print(f"\n{title}:")
    print(matrix)


def main():
    print("=" * 48)
    print("          NUMPY MATRIX OPERATIONS")
    print("=" * 48)

    matrix_a = read_matrix("Matrix A")
    matrix_b = read_matrix("Matrix B")

    display_matrix("Matrix A", matrix_a)
    display_matrix("Matrix B", matrix_b)

    print("\n--- Addition ---")
    if matrix_a.shape == matrix_b.shape:
        display_matrix("A + B", matrix_a + matrix_b)
    else:
        print("Not possible: both matrices must have the same dimensions.")

    print("\n--- Subtraction ---")
    if matrix_a.shape == matrix_b.shape:
        display_matrix("A - B", matrix_a - matrix_b)
    else:
        print("Not possible: both matrices must have the same dimensions.")

    print("\n--- Matrix Multiplication ---")
    if matrix_a.shape[1] == matrix_b.shape[0]:
        display_matrix("A @ B", matrix_a @ matrix_b)
        print("Explanation: Each result element is the dot product of a row")
        print("from Matrix A and a column from Matrix B.")
    else:
        print("Not possible: columns of A must equal rows of B.")

    print("\n--- Transpose ---")
    display_matrix("Transpose of A (A.T)", matrix_a.T)
    display_matrix("Transpose of B (B.T)", matrix_b.T)


if __name__ == "__main__":
    main()
