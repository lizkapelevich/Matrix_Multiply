import sys
import numpy as np

#for ii in range(3):
#    for jj in range(3):
        


A = np.zeros(9)
for ii in range(9):
    A[ii] = input("Enter number {}: ".format(ii))


A[ii, jj] = input...


print(A)


# Comment out this line to let the code progress from here
sys.exit(0)


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
