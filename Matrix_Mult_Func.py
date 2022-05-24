import numpy as np

def mat_mult(A, B):
c = np.zeros((a_row_cnt, b_col_cnt))
    for c_row_ii in range(0, a_row_cnt):
        for c_col_ii in range(0, b_col_cnt):
            for ii in range(0, a_col_cnt):
                c[c_row_ii, c_col_ii] = c[c_row_ii, c_col_ii] + a[c_row_ii, ii] * b[ii, c_col_ii]

