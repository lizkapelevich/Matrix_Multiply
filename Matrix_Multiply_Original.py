import numpy as np

a_col_cnt = int(input("Input how many columns in Matrix A: "))
a_row_cnt = int(input("Input how many rows in Matrix A: "))

b_col_cnt = a_row_cnt
b_row_cnt = a_col_cnt

a = np.zeros((a_row_cnt, a_col_cnt))
b = np.zeros((b_row_cnt, b_col_cnt))

print("Enter value for item in Matrix A")
for a_row_ii in range(0, a_row_cnt):
    for a_col_ii in range(0, a_col_cnt):
        a[a_row_ii, a_col_ii] = input("[" + str(a_row_ii) + ", " + str(a_col_ii) + "]: ")
        
print("Enter value for item in Matrix B")
for b_row_ii in range(0, b_row_cnt):
    for b_col_ii in range(0, b_col_cnt):
        b[b_row_ii, b_col_ii] = input("[" + str(b_row_ii) + ", " + str(b_col_ii) + "]: ")

c = np.zeros((a_row_cnt, b_col_cnt))

for c_row_ii in range(0, a_row_cnt):
    for c_col_ii in range(0, b_col_cnt):
        for ii in range(0, a_col_cnt):
#            print(str(c_row_ii) + " " + str(c_col_ii) + " = " + str(c_row_ii) + " " + str(ii) + " * " + str(ii) + " " + str(c_col_ii))
            c[c_row_ii, c_col_ii] += a[c_row_ii, ii] * b[ii, c_col_ii]

print("The calculation of your matrix is: ")
print(c)
