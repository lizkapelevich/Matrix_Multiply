import numpy as np
import Matrix_Mult_Func as mmf

class Rotation:
    """
    Write discussion for this class and def functions 
    """
    def __init__(self, angle, axis="z"):
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
        return mmf.mat_mult(self.R, vec)
