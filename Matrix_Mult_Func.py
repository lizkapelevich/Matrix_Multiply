import numpy as np

def mat_mult(aa, bb):
    """
    This function takes as input two matrices of same shape,
    and computes their product.

    INPUT:
    ------
    aa : Numpy array of first matrix
    bb : Numpy array of second matrix
    cc : Numpy array of product of first and second matrix
    
    RETURNS:
    -------
    A numpy array
    """
    cc = np.zeros(np.shape(aa))
    nn = len(cc)
    for ii in range(0, nn):
        for jj in range(0, nn):
            cc[ii, jj] = np.sum(aa[ii]*bb[:,jj])
    return cc

def mat_mult2(a, b):
    """
    This function takes as input two matrices of same shape,
    and computes their product.

    INPUT:
    ------
    A : Numpy array
    B : Numpy array

    RETURNS:
    --------
    The product of the two numpy arrays
    """
    a_row_cnt, b_col_cnt = np.shape(a)
    a_col_cnt = a_row_cnt
    c = np.zeros((a_row_cnt, b_col_cnt))

    for c_row_ii in range(0, a_row_cnt):
        for c_col_ii in range(0, b_col_cnt):
            for ii in range(0, a_col_cnt):
                c[c_row_ii, c_col_ii] += a[c_row_ii, ii] * b[ii, c_col_ii]

    return c


def mat_sq_col1(ff,gg):
    """
    This function takes as input two matrices of different shapes,
    and computes their product.

    INPUT:
    ------
    ff : Numpy array of first matrix
    gg : Numpy array of second matrix

    RETURNS:
    --------
    The product of the two numpy arrays
    """

    hh = np.zeros((min(np.shape(ff)),min(np.shape(gg))))
    pp = len(hh)
    for ii in range(0, pp):
        for jj in range(0, pp):
            gg == gg.T
            hh[ii, jj] = np.sum(ff[ii]*gg[:,jj])
    return hh

