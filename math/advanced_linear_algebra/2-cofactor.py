#!/usr/bin/env python3
"""
Module to calculate the cofactor matrix of a square matrix.
"""


def determinant(matrix):
    """
    Calculates the determinant of a square matrix.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 0:
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        sub = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)
    return det


def minor(matrix):
    """
    Calculates the minor matrix of a square matrix.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [matrix[x][:j] + matrix[x][j+1:] for x in range(n) if x != i]
            row.append(determinant(sub))
        minor_matrix.append(row)
    return minor_matrix


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [matrix[x][:j] + matrix[x][j+1:] for x in range(n) if x != i]
            minor_det = determinant(sub)
            row.append(((-1) ** (i + j)) * minor_det)  # <-- fixed minus
        cof.append(row)
    return cof
