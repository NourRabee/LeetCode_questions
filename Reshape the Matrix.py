import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:\
        
        np_array = np.asarray(mat)
        row = len(np_array)
        columns = len(np_array[0])
        numberOfElements = row * columns
        if numberOfElements == (r * c):
            newMatrix = np.reshape(np_array, (r, c))
            return newMatrix
        else:
            return mat
