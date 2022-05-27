import numpy as np
import Matrix_Mult_Func as mmf

class Rotation:
    """
    This class will bundle both data and functionality together to run
    different functions for computing matrix rotations.
    """
    def __init__(self, angle, axis="z"):
        """
        Write about what this code does rather than how it works.
        
        INPUT:
        ------
        angle : any angle theta in radians
        axis  : any axis from the 3D plane
        
        RETURNS:
        -------
        The trigonometric identity matrix.
        """
        assert (axis=="x" or axis=="y" or axis=="z"), "Axis error"
        if axis == "x":
            self.R = np.array([[1, 0, 0],
                     [0, np.cos(angle), np.sin(angle)],
                     [0, -np.sin(angle), np.cos(angle)]])
        if axis == "y":
            self.R = np.array([[np.cos(angle), 0, np.sin(angle)],
                     [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])
        if axis == "z":
            self.R = np.array([[np.cos(angle), np.sin(angle), 0],
                     [-np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

    def rotate(self, vec):
        """
        This function takes as input a vector and runs a function that 
        will output a calculation for the rotation of a matrix.
        
        INPUT:
        ------
        angle : any vector in the 3D plane
        
        RETURNS:
        -------
        The rotation of a matrix.
        """
        return mmf.mat_mult(self.R, vec)
