class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #time limit exceeded
        # counter = 0
        # for i in range(low, high + 1):
        #     if i % 2 != 0:
        #         counter += 1
        # return counter

        totalNumbers = len(range(low, high+1))
        lengthIsEven = totalNumbers % 2 == 0
        firstNumberIsOdd = low % 2 != 0

        if lengthIsEven:
            return math.floor(totalNumbers/2)
        else:
            if firstNumberIsOdd:
                return math.floor(totalNumbers / 2) + 1
            else:
                return math.floor(totalNumbers / 2)
