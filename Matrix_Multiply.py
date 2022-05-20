
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]]

A1_B1 = np.sum(A[0]*B[:,0])
A2_B2 = np.sum(A[0]*B[:,1])
A3_B3 = np.sum(A[1]*B[:,0])
A4_B4 = np.sum(A[1]*B[:,1])

print((A11*B11)+(A12*B21))
print((A11*B12)+(A12*B22))
print((A21*B11)+(A22*B21))
print((A21*B12)+(A22*B22))

# user input and make values printed out
# write function that'll take input value and will do matrix calculation
