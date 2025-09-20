#!/usr/bin/env python3
"""
Module to determine the definiteness of a square numpy matrix.
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a square numpy.ndarray.

    Args:
        matrix (numpy.ndarray): matrix to check

    Returns:
        str or None: 'Positive definite', 'Positive semi-definite',
                     'Negative definite', 'Negative semi-definite',
                     'Indefinite', or None if invalid
                     
    Raises:
        TypeError: if matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if matrix.size == 0:
        return None

    try:
        eigvals = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None

    pos = np.all(eigvals > 0)
    pos_semi = np.all(eigvals >= 0)
    neg = np.all(eigvals < 0)
    neg_semi = np.all(eigvals <= 0)

    if pos:
        return "Positive definite"
    if pos_semi and not pos:
        return "Positive semi-definite"
    if neg:
        return "Negative definite"
    if neg_semi and not neg:
        return "Negative semi-definite"
    if not pos_semi and not neg_semi:
        return "Indefinite"

    return None
