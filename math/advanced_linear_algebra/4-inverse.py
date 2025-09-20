#!/usr/bin/env python3
"""
Module for calculating the inverse of a square matrix.
"""

def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Args:
        matrix (list of lists): matrix whose determinant is to be calculated

    Returns:
        int or float: determinant of the matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a square matrix
    """
    if not isinstance(matrix, list) or \
       any(not isinstance(row, list) for row in matrix):
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
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        minor_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor_matrix)

    return det


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix.

    Args:
        matrix (list of lists): matrix to calculate the cofactor matrix from

    Returns:
        list of lists: cofactor matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    if not isinstance(matrix, list) or \
       any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [matrix[x][:j] + matrix[x][j+1:] for x in range(n) if x != i]
            minor_det = determinant(sub)
            row.append(((-1) ** (i + j)) * minor_det)
        cofactor_matrix.append(row)

    return cofactor_matrix


def adjugate(matrix):
    """
    Calculates the adjugate matrix of a square matrix.

    Args:
        matrix (list of lists): matrix to calculate the adjugate from

    Returns:
        list of lists: adjugate matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    cof = cofactor(matrix)
    adj = [[cof[j][i] for j in range(len(cof))] for i in range(len(cof))]
    return adj


def inverse(matrix):
    """
    Calculates the inverse of a square matrix.

    Args:
        matrix (list of lists): matrix to invert

    Returns:
        list of lists or None: inverse matrix or None if singular

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    if not isinstance(matrix, list) or \
       any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
    return inv
