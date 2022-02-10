# import np as np
import numpy as np

class Solution:
    def Valid(list) -> List:
        dict = {}
        for i in list:
            if i not in dict and "0" <= i <= "9":
                dict[i] = 1
            elif i in dict and "0" <= i <= "9":
                dict[i] += 1
        return dict


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validation = []
        for i in board:
            x = Solution.Valid(i)
            for j in x:
                if x[j] != 1:
                    validation.append("False")
                    break
        if "False" not in validation:
            validation.append("True")

        numpy_array = np.array(board)
        transpose = numpy_array.T
        transpose_list = transpose.tolist()

        for i in transpose_list:
            x = Solution.Valid(i)
            for j in x:
                if x[j] != 1:
                    validation.append("False")
                    break
        if "False" not in validation:
            validation.append("True")

        # print(validation)
        np_array1 = np.asarray(board)
        reshaped_array1 = np.hsplit(np_array1, 3)
        np_array2 = np.asarray(reshaped_array1)

        for i in np_array2:
            reshaped_array2 = np.vsplit(i, 3)
            reshaped_array2 = np.asarray(reshaped_array2)
            for i in reshaped_array2:
                newarr = i.reshape(-1)
                x= Solution.Valid(newarr)
                for j in x:
                    if x[j] != 1:
                        validation.append("False")
                        break
            if "False" not in validation:
                validation.append("True")

        if "False" in validation:
            return False
        else:
            return True
