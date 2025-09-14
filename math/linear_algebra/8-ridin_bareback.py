#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for row in mat1:
        new_row = [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
        result.append(new_row)
    return result
