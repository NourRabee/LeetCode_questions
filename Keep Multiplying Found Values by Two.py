class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
    
            loop = True
            while loop:
                if original in nums:
                    original = 2 * original
                elif original not in nums:
                    loop = False
                    return original
