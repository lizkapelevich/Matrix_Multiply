import numpy as np

def rows_and_cols(x):
    """
    This function takes as input one matrix and runs  an if-else
    statement that computes the length of the necessary matrix for the
    following definition function. If the matrix is a 2x1, it will print 
    in the proper format. Otherwise, the function will print out the proper
    format automatically.

    INPUT:
    -------
    x : Numpy array of a matrix

    RETURNS:
    --------
    The length of the Numpy array
    """

    y = np.shape(x)
    z = len(y)
    if z > 1:
        return y
    else:
        return (y[0], 1)


def mat_mult(aa, bb):
    """
    This function takes as input two matrices that may or may not be
    of the same shape/size, and computes their product. If the arrays
    are incomputible, an assertion error will pop up; otherwise, the
    function will produce the product of the multiplication of the 
    two matrices.

    INPUT:
    ------
    aa : Numpy array of first matrix
    bb : Numpy array of second matrix
    cc : Numpy array of product of first and second matrix
    
    RETURNS:
    -------
    A numpy array
    """
dim_aa = rows_and_cols(aa)
    dim_bb = rows_and_cols(bb)
    assert dim_aa[1] == dim_bb[0], print("Matrices cannot be multiplied")
    
    cc = np.zeros((dim_aa[0], dim_bb[1]))
    if dim_bb[1] == 1:
        cc = cc.flatten()
        for ii in range(0, dim_aa[0]):
            cc[ii] = np.sum(aa[ii]*bb)
    else:
        for ii in range(0, dim_aa[0]):
            for jj in range(0, dim_bb[1]):
                cc[ii, jj] = np.sum(aa[ii]*bb[:,jj])
    return cc

