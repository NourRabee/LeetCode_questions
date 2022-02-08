class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        intSum = int(a, 2) + int(b, 2)
        sumBinary = bin(intSum)
        sumBinary = str(sumBinary)
        slicedString = sumBinary[2:]
        return slicedString
