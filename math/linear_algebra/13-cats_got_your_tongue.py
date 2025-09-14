#!/usr/bin/env python3
import numpy as np
'''
    This function def np_cat(mat1, mat2, axis=0)
    concatenates two matrices along a specific axis
'''
def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy arrays along a specific axis"""
    return np.concatenate((mat1, mat2), axis=axis)

